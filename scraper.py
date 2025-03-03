#!/usr/bin/env python3
"""
Google Site Scraper for GitBook

This script scrapes Google Site pages listed in a SUMMARY.md file and converts them
to markdown files organized in a GitBook-compatible directory structure.
"""

import os
import sys
import re
import requests
import time
import hashlib
import json
import shutil
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote, parse_qs, urljoin
from tqdm import tqdm
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import socket


class GoogleSiteScraper:
    def __init__(self, summary_file, output_dir, download_images=False, max_workers=10):
        """
        Initialize the scraper with the path to the SUMMARY.md file and output directory.
        
        Args:
            summary_file (str): Path to the SUMMARY.md file
            output_dir (str): Directory where the GitBook structure will be created
            download_images (bool): Whether to download images during scraping
            max_workers (int): Maximum number of concurrent image download workers
        """
        self.summary_file = summary_file
        self.output_dir = output_dir
        self.download_images = download_images
        self.max_workers = max_workers
        self.links = []
        self.visited_urls = set()
        
        # Configure socket timeout
        socket.setdefaulttimeout(30)  # 30 seconds timeout
        
        # Set up the session with robust connection pooling
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            max_retries=5,
            pool_connections=self.max_workers * 2,
            pool_maxsize=self.max_workers * 4
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        
        # Request headers to mimic a browser
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        
        # Create assets directory if downloading images
        if self.download_images:
            self.assets_dir = os.path.join(self.output_dir, 'assets')
            os.makedirs(self.assets_dir, exist_ok=True)
            
            # Initialize the thread pool for image downloads
            self.executor = ThreadPoolExecutor(max_workers=self.max_workers)
            self.download_futures = []
        
    def parse_summary(self):
        """
        Parse the SUMMARY.md file to extract all Google Site links and their hierarchy.
        
        Returns:
            list: List of dictionaries containing page info (title, url, level, path)
        """
        print("Parsing SUMMARY.md file...")
        with open(self.summary_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract all markdown links with their indentation level
        pattern = r'^(\s*)[-*]\s+\[(.*?)\]\((https://sites\.google\.com/.*?)\)'
        matches = re.finditer(pattern, content, re.MULTILINE)
        
        pages = []
        for match in matches:
            indent, title, url = match.groups()
            # Calculate hierarchy level based on indentation and list marker
            level = len(indent) // 2
            
            # Clean the title for use as a filename/directory
            clean_title = self.clean_filename(title)
            
            # Determine the path components based on the URL structure
            path_components = self.get_path_from_url(url)
            
            pages.append({
                'title': title,
                'clean_title': clean_title,
                'url': url,
                'level': level,
                'path_components': path_components
            })
        
        print(f"Found {len(pages)} pages to scrape.")
        return pages
    
    def get_path_from_url(self, url):
        """
        Extract path components from the Google Site URL.
        
        Args:
            url (str): Google Site URL
            
        Returns:
            list: Path components for the file structure
        """
        parsed_url = urlparse(url)
        path = parsed_url.path
        
        # Remove the domain part and split by '/'
        parts = path.split('/')
        # Filter out empty parts and the first part (usually the domain)
        parts = [p for p in parts if p and p != 'stanford.edu']
        
        # The last part is usually the page name
        return parts
    
    def clean_filename(self, name):
        """
        Clean a string to make it suitable for use as a filename.
        
        Args:
            name (str): String to clean
            
        Returns:
            str: Cleaned string suitable for filenames
        """
        # Replace characters that are problematic in filenames
        name = re.sub(r'[\\/*?:"<>|]', '_', name)
        # Replace spaces with hyphens
        name = name.replace(' ', '-')
        # Remove any other non-alphanumeric characters
        name = re.sub(r'[^\w\-.]', '', name)
        return name
    
    def create_directory_structure(self, pages):
        """
        Create the directory structure based on the page hierarchy.
        
        Args:
            pages (list): List of page dictionaries
        """
        print("Creating directory structure...")
        
        # Create the base output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Create README.md in the root directory if it doesn't exist
        readme_path = os.path.join(self.output_dir, 'README.md')
        if not os.path.exists(readme_path):
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write('# Introduction\n\nThis is the introduction to the GitBook.\n')
        
        # Create directories for each level of the hierarchy
        for page in pages:
            # Build the directory path based on path components
            dir_path = self.output_dir
            for i, component in enumerate(page['path_components'][:-1]):  # Exclude the last component (page name)
                clean_component = self.clean_filename(component)
                dir_path = os.path.join(dir_path, clean_component)
                os.makedirs(dir_path, exist_ok=True)
                
                # Create README.md in each directory if it's a parent page
                if i < len(page['path_components']) - 2:  # Not the immediate parent of the current page
                    readme_path = os.path.join(dir_path, 'README.md')
                    if not os.path.exists(readme_path):
                        with open(readme_path, 'w', encoding='utf-8') as f:
                            f.write(f'# {component}\n\nThis is the {component} section.\n')
    
    def get_image_filename(self, img_url):
        """
        Generate a consistent filename for an image URL.
        
        Args:
            img_url (str): Image URL
        
        Returns:
            str: Filename for the image
        """
        # Try to get the filename from the URL path
        parsed_url = urlparse(img_url)
        path = parsed_url.path
        
        # Get the basename without query parameters
        basename = os.path.basename(path.split('?')[0])
        
        # If there's no valid basename, create one using a hash of the URL
        if not basename or basename == '/' or '.' not in basename:
            # Create a hash of the URL
            url_hash = hashlib.md5(img_url.encode()).hexdigest()[:10]
            
            # Try to determine extension from Content-Type
            try:
                response = requests.head(img_url, timeout=5)
                content_type = response.headers.get('Content-Type', '')
                
                if content_type == 'image/jpeg':
                    ext = '.jpg'
                elif content_type == 'image/png':
                    ext = '.png'
                elif content_type == 'image/gif':
                    ext = '.gif'
                elif content_type == 'image/svg+xml':
                    ext = '.svg'
                elif content_type == 'image/webp':
                    ext = '.webp'
                else:
                    ext = '.png'  # Default to png
                    
                basename = f"image_{url_hash}{ext}"
            except:
                # If head request fails, use generic extension
                basename = f"image_{url_hash}.png"
        
        return basename
    
    def download_image(self, img_url, output_path):
        """
        Download an image from a URL and save it to the specified path.
        
        Args:
            img_url (str): URL of the image to download
            output_path (str): Path where the image should be saved
        
        Returns:
            bool: True if download was successful, False otherwise
        """
        try:
            # Create a session with appropriate headers
            session = requests.Session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
            }
            
            # Make the request
            response = session.get(img_url, headers=headers, stream=True, timeout=10)
            response.raise_for_status()
            
            # Check if the response is an image
            content_type = response.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                print(f"Warning: URL {img_url} does not point to an image (Content-Type: {content_type})")
            
            # Save the image
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return True
        
        except Exception as e:
            print(f"Error downloading image from {img_url}: {e}")
            return False
    
    def process_image(self, img_url, md_file=None):
        """
        Process an image URL: determine filename, download if needed, and return the path to use in markdown.
        
        Args:
            img_url (str): Image URL
            md_file (str, optional): Path to the markdown file referencing this image
        
        Returns:
            str: Relative path to use in markdown
        """
        if not self.download_images:
            return img_url
            
        # Generate a consistent filename for the image
        img_filename = self.get_image_filename(img_url)
        img_output_path = os.path.join(self.assets_dir, img_filename)
        
        # Calculate relative path from the actual markdown file to the assets directory
        if md_file:
            md_dir = os.path.dirname(md_file)
            rel_path = os.path.relpath(self.assets_dir, md_dir)
        else:
            rel_path = 'assets'
        
        new_img_path = os.path.join(rel_path, img_filename).replace('\\', '/')
        
        # Check if the image already exists
        if not os.path.exists(img_output_path):
            # Submit the download task to the executor
            future = self.executor.submit(self.download_image, img_url, img_output_path)
            self.download_futures.append((future, img_url, img_output_path))
        
        return new_img_path
        
    def scrape_page(self, url, output_path=None):
        """
        Scrape content from a Google Site page and convert it to markdown.
        
        Args:
            url (str): URL of the page to scrape
            output_path (str, optional): Path where the markdown file will be saved
            
        Returns:
            str: Markdown content of the page
        """
        if url in self.visited_urls:
            return None
        
        self.visited_urls.add(url)
        
        # Setup retry parameters
        max_retries = 5
        retry_delay = 5  # seconds
        
        for retry_count in range(max_retries):
            try:
                # Add a small delay to avoid hitting rate limits
                time.sleep(1)
                
                # Attempt to connect with increased timeout
                response = self.session.get(url, headers=self.headers, timeout=30)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extract the title
                title_elem = soup.find('title')
                title = title_elem.text if title_elem else "Untitled Page"
                
                # Extract the main content
                content_div = soup.find('div', {'id': 'content'}) or soup.find('div', {'class': 'sites-content'})
                if not content_div:
                    content_div = soup.find('div', {'role': 'main'})
                
                if not content_div:
                    return f"# {title}\n\nNo content could be extracted from this page."
                
                # Convert HTML to markdown
                markdown_content = f"# {title}\n\n"
                
                # Process paragraphs and other elements
                for element in content_div.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'a', 'img', 'table', 'iframe', 'embed', 'object', 'div']):
                    if element.name == 'p':
                        markdown_content += f"{element.get_text()}\n\n"
                    elif element.name.startswith('h'):
                        level = int(element.name[1])
                        markdown_content += f"{'#' * level} {element.get_text()}\n\n"
                    elif element.name == 'a':
                        href = element.get('href', '')
                        markdown_content += f"[{element.get_text()}]({href})\n\n"
                    elif element.name == 'img':
                        src = element.get('src', '')
                        alt = element.get('alt', '')
                        
                        # Process the image if downloading
                        if self.download_images and src.startswith('http'):
                            src = self.process_image(src, output_path)
                            
                        markdown_content += f"![{alt}]({src})\n\n"
                    elif element.name == 'ul':
                        for li in element.find_all('li'):
                            markdown_content += f"* {li.get_text()}\n"
                        markdown_content += "\n"
                    elif element.name == 'ol':
                        for i, li in enumerate(element.find_all('li')):
                            markdown_content += f"{i+1}. {li.get_text()}\n"
                        markdown_content += "\n"
                    elif element.name == 'iframe':
                        src = element.get('src', '')
                        title = element.get('title', 'Embedded Content')
                        width = element.get('width', '100%')
                        height = element.get('height', '400')
                        
                        # Extract information based on iframe source
                        if 'youtube.com' in src or 'youtu.be' in src:
                            # YouTube embed
                            video_id = self.extract_youtube_id(src)
                            if video_id:
                                markdown_content += f"### Embedded YouTube Video\n\n"
                                markdown_content += f"YouTube Video: [{title}](https://www.youtube.com/watch?v={video_id})\n\n"
                                markdown_content += f"<iframe width=\"{width}\" height=\"{height}\" src=\"https://www.youtube.com/embed/{video_id}\" frameborder=\"0\" allowfullscreen></iframe>\n\n"
                        elif 'docs.google.com/document' in src:
                            # Google Docs embed
                            markdown_content += f"### Embedded Google Document\n\n"
                            markdown_content += f"Google Document: [{title}]({src})\n\n"
                            markdown_content += f"<iframe width=\"{width}\" height=\"{height}\" src=\"{src}\" frameborder=\"0\"></iframe>\n\n"
                        elif 'docs.google.com/spreadsheets' in src:
                            # Google Sheets embed
                            markdown_content += f"### Embedded Google Spreadsheet\n\n"
                            markdown_content += f"Google Spreadsheet: [{title}]({src})\n\n"
                            markdown_content += f"<iframe width=\"{width}\" height=\"{height}\" src=\"{src}\" frameborder=\"0\"></iframe>\n\n"
                        elif 'docs.google.com/presentation' in src:
                            # Google Slides embed
                            markdown_content += f"### Embedded Google Slides\n\n"
                            markdown_content += f"Google Slides: [{title}]({src})\n\n"
                            markdown_content += f"<iframe width=\"{width}\" height=\"{height}\" src=\"{src}\" frameborder=\"0\"></iframe>\n\n"
                        elif 'drive.google.com' in src:
                            # Google Drive embed
                            markdown_content += f"### Embedded Google Drive File\n\n"
                            markdown_content += f"Google Drive File: [{title}]({src})\n\n"
                            markdown_content += f"<iframe width=\"{width}\" height=\"{height}\" src=\"{src}\" frameborder=\"0\"></iframe>\n\n"
                        elif 'calendar.google.com' in src:
                            # Google Calendar embed
                            markdown_content += f"### Embedded Google Calendar\n\n"
                            markdown_content += f"Google Calendar: [{title}]({src})\n\n"
                            markdown_content += f"<iframe width=\"{width}\" height=\"{height}\" src=\"{src}\" frameborder=\"0\"></iframe>\n\n"
                        elif 'forms.google.com' in src:
                            # Google Forms embed
                            markdown_content += f"### Embedded Google Form\n\n"
                            markdown_content += f"Google Form: [{title}]({src})\n\n"
                            markdown_content += f"<iframe width=\"{width}\" height=\"{height}\" src=\"{src}\" frameborder=\"0\"></iframe>\n\n"
                        else:
                            # Generic iframe
                            markdown_content += f"### Embedded Content\n\n"
                            markdown_content += f"Embedded content: [{title}]({src})\n\n"
                            markdown_content += f"<iframe width=\"{width}\" height=\"{height}\" src=\"{src}\" frameborder=\"0\"></iframe>\n\n"
                    
                    elif element.name == 'embed' or element.name == 'object':
                        src = element.get('src', '') or element.get('data', '')
                        type_attr = element.get('type', 'application/unknown')
                        width = element.get('width', '100%')
                        height = element.get('height', '400')
                        
                        if 'pdf' in type_attr.lower() or src.lower().endswith('.pdf'):
                            # PDF embed
                            markdown_content += f"### Embedded PDF\n\n"
                            markdown_content += f"PDF Document: [{os.path.basename(src)}]({src})\n\n"
                            markdown_content += f"<embed src=\"{src}\" type=\"application/pdf\" width=\"{width}\" height=\"{height}\">\n\n"
                        else:
                            # Generic embed
                            markdown_content += f"### Embedded Content\n\n"
                            markdown_content += f"Embedded content: [{type_attr}]({src})\n\n"
                            markdown_content += f"<embed src=\"{src}\" type=\"{type_attr}\" width=\"{width}\" height=\"{height}\">\n\n"
                    
                    elif element.name == 'div':
                        # Check if this is a special Google Sites embedded content div
                        if element.get('data-embed-type') or element.get('data-attr-src'):
                            embed_type = element.get('data-embed-type', 'unknown')
                            embed_src = element.get('data-attr-src', '')
                            
                            if embed_src:
                                markdown_content += f"### Embedded {embed_type.capitalize()} Content\n\n"
                                markdown_content += f"Embedded content: [{embed_type}]({embed_src})\n\n"
                                
                                # Special handling for different embed types
                                if 'image' in embed_type.lower():
                                    alt = element.get('data-attr-alt', '')
                                    src = embed_src
                                    
                                    # Process the image if downloading
                                    if self.download_images and src.startswith('http'):
                                        src = self.process_image(src, output_path)
                                        
                                    markdown_content += f"![{alt}]({src})\n\n"
                
                return markdown_content
                
            except requests.exceptions.RequestException as e:
                # If this is the last retry, raise the error
                if retry_count == max_retries - 1:
                    print(f"Error scraping {url} after {max_retries} attempts: {e}")
                    # Save an error page with the URL so we can retry later
                    return f"# Error\n\nFailed to scrape content from {url}. Error: {e}\n\nOriginal URL: {url}"
                
                # Log the error and retry
                print(f"Error on attempt {retry_count + 1}/{max_retries} scraping {url}: {e}")
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                
            except Exception as e:
                # For non-request exceptions, don't retry
                print(f"Unexpected error scraping {url}: {e}")
                return f"# Error\n\nFailed to scrape content from {url}. Error: {e}\n\nOriginal URL: {url}"
    
    def extract_youtube_id(self, url):
        """
        Extract YouTube video ID from various YouTube URL formats.
        
        Args:
            url (str): YouTube URL
            
        Returns:
            str: YouTube video ID or None if not found
        """
        youtube_regex = (
            r'(https?:\/\/)?(www\.)?'
            r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
            r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        
        match = re.match(youtube_regex, url)
        if match:
            return match.group(6)
        
        # Try to extract from query parameters
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        
        if 'v' in query_params:
            return query_params['v'][0]
        
        return None
    
    def save_markdown_file(self, page, content):
        """
        Save the markdown content to a file in the appropriate location.
        
        Args:
            page (dict): Page information dictionary
            content (str): Markdown content to save
        """
        # Build the file path based on path components
        file_path = self.output_dir
        for component in page['path_components'][:-1]:  # Exclude the last component (page name)
            clean_component = self.clean_filename(component)
            file_path = os.path.join(file_path, clean_component)
        
        # The last component is the page name
        page_name = page['path_components'][-1] if page['path_components'] else page['clean_title']
        clean_page_name = self.clean_filename(page_name)
        
        # Create the file
        file_path = os.path.join(file_path, f"{clean_page_name}.md")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return file_path
    
    def create_new_summary(self, pages):
        """
        Create a new SUMMARY.md file with local links instead of Google Site links.
        
        Args:
            pages (list): List of page dictionaries
        """
        print("Creating new SUMMARY.md file...")
        
        summary_content = "# Summary\n\n"
        
        for page in pages:
            # Calculate indentation based on level
            indent = "  " * page['level']
            
            # Build the relative path to the markdown file
            path_parts = [self.clean_filename(p) for p in page['path_components']]
            if path_parts:
                relative_path = "/".join(path_parts[:-1] + [f"{self.clean_filename(path_parts[-1])}.md"])
            else:
                relative_path = f"{page['clean_title']}.md"
            
            # Add the entry to the summary
            summary_content += f"{indent}* [{page['title']}]({relative_path})\n"
        
        # Save the new SUMMARY.md
        with open(os.path.join(self.output_dir, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
            f.write(summary_content)
    
    def run(self):
        """
        Run the complete scraping process.
        """
        # Parse the SUMMARY.md file
        pages = self.parse_summary()
        
        # Create the directory structure
        self.create_directory_structure(pages)
        
        error_pages = []
        with tqdm(total=len(pages), desc="Scraping pages") as pbar:
            for page in pages:
                try:
                    # Build the file path based on path components
                    file_path = self.output_dir
                    for component in page['path_components'][:-1]:  # Exclude the last component (page name)
                        clean_component = self.clean_filename(component)
                        file_path = os.path.join(file_path, clean_component)
                    
                    # The last component is the page name
                    page_name = page['path_components'][-1] if page['path_components'] else page['clean_title']
                    clean_page_name = self.clean_filename(page_name)
                    
                    # Create the file path
                    md_file_path = os.path.join(file_path, f"{clean_page_name}.md")
                    
                    # Create directory if it doesn't exist
                    os.makedirs(os.path.dirname(md_file_path), exist_ok=True)
                    
                    # Scrape the page content with the file path for correct image handling
                    content = self.scrape_page(page['url'], md_file_path)
                    
                    if content and "# Error" in content:
                        error_pages.append((page['title'], page['url'], md_file_path))
                    
                    # Save the file
                    if content:
                        with open(md_file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"Saved: {md_file_path}")
                    
                except Exception as e:
                    print(f"Error processing page {page['url']}: {e}")
                    error_pages.append((page['title'], page['url'], md_file_path if 'md_file_path' in locals() else 'unknown_path'))
                
                finally:
                    pbar.update(1)
        
        # Report on any errors
        if error_pages:
            print("\n=============================================")
            print(f"Encountered errors with {len(error_pages)} pages:")
            for title, url, path in error_pages:
                print(f"  - {title}: {url}")
            print("You may want to re-run the scraper for these pages later.")
            print("=============================================\n")
            
            # Save error_pages to a file for later reference
            error_file = os.path.join(self.output_dir, "error_pages.txt")
            with open(error_file, 'w', encoding='utf-8') as f:
                f.write("# Pages with errors during scraping\n\n")
                for title, url, path in error_pages:
                    f.write(f"- [{title}]({url}) -> {path}\n")
            print(f"Error pages list saved to: {error_file}")
        
        # Create a new SUMMARY.md file with local links
        self.create_new_summary(pages)
        
        # Wait for all image downloads to complete if downloading enabled
        if self.download_images and hasattr(self, 'download_futures'):
            print(f"Waiting for {len(self.download_futures)} image downloads to complete...")
            for future, img_url, img_output_path in self.download_futures:
                try:
                    result = future.result()
                    status = "Success" if result else "Failed"
                    print(f"{status}: {os.path.basename(img_output_path)} from {img_url}")
                except Exception as e:
                    print(f"Failed: {os.path.basename(img_output_path)} from {img_url}. Error: {e}")
            
            # Shutdown the executor
            self.executor.shutdown()
        
        print(f"Done! GitBook structure created in {self.output_dir}")


def main():
    """
    Main function to run the scraper.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape Google Sites to GitBook format')
    parser.add_argument('--summary', default='SUMMARY.md', help='Path to SUMMARY.md file')
    parser.add_argument('--output', default='gitbook', help='Output directory for GitBook files')
    parser.add_argument('--download-images', action='store_true', help='Download images during scraping')
    parser.add_argument('--max-workers', type=int, default=10, help='Maximum number of concurrent image downloads')
    
    args = parser.parse_args()
    
    scraper = GoogleSiteScraper(args.summary, args.output, args.download_images, args.max_workers)
    scraper.run()


if __name__ == '__main__':
    main()
