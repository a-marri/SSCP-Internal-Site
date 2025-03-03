#!/usr/bin/env python3
"""
Utility functions for the Google Site Scraper

This script provides additional utilities for working with the scraped GitBook content.
"""

import os
import re
import argparse
import requests
import hashlib
from pathlib import Path
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor


def download_image(img_url, output_path):
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


def get_image_filename(img_url):
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


def fix_image_links(gitbook_dir, download=True, max_workers=10):
    """
    Fix image links in markdown files to use relative paths and optionally download the images.
    
    Args:
        gitbook_dir (str): Path to the GitBook directory
        download (bool): Whether to download the images
        max_workers (int): Maximum number of concurrent download workers
    """
    print(f"Fixing image links in {gitbook_dir}...")
    
    # Get all markdown files
    md_files = list(Path(gitbook_dir).glob('**/*.md'))
    print(f"Found {len(md_files)} markdown files")
    
    # Create an assets directory if it doesn't exist
    assets_dir = os.path.join(gitbook_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)
    
    # If downloading, create an executor for parallel downloads
    if download:
        executor = ThreadPoolExecutor(max_workers=max_workers)
        download_futures = []
    
    # Keep track of all images to download
    all_images = []
    
    # First pass: collect all image URLs and update markdown files
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all image links
        img_pattern = r'!\[(.*?)\]\((https?://.*?)\)'
        matches = re.findall(img_pattern, content)
        
        if matches:
            print(f"Found {len(matches)} image links in {md_file}")
            
            # Replace each image link
            for alt_text, img_url in matches:
                # Generate a consistent filename for the image
                img_filename = get_image_filename(img_url)
                
                # Create the relative path from markdown file to assets directory
                rel_path = os.path.relpath(assets_dir, os.path.dirname(md_file))
                new_img_path = os.path.join(rel_path, img_filename).replace('\\', '/')
                
                # Replace the link in the content
                content = content.replace(
                    f"![{alt_text}]({img_url})",
                    f"![{alt_text}]({new_img_path})"
                )
                
                # Add to list of images to download
                if download:
                    img_output_path = os.path.join(assets_dir, img_filename)
                    all_images.append((img_url, img_output_path))
            
            # Write the updated content back to the file
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    # Second pass: download all unique images
    if download and all_images:
        # Remove duplicates (same URL with different output paths)
        unique_images = {}
        for url, path in all_images:
            unique_images[url] = path
        
        print(f"Downloading {len(unique_images)} unique images...")
        
        # Submit download tasks to the executor
        for img_url, img_output_path in unique_images.items():
            # Skip if the image already exists
            if os.path.exists(img_output_path):
                print(f"Skipping existing image: {os.path.basename(img_output_path)}")
                continue
                
            # Submit the download task
            future = executor.submit(download_image, img_url, img_output_path)
            download_futures.append((future, img_url, img_output_path))
        
        # Wait for all downloads to complete
        for future, img_url, img_output_path in download_futures:
            result = future.result()
            status = "Success" if result else "Failed"
            print(f"{status}: {os.path.basename(img_output_path)} from {img_url}")
        
        # Shutdown the executor
        executor.shutdown()
        
        print(f"Image downloads completed.")


def fix_internal_links(gitbook_dir):
    """
    Fix internal links in markdown files to use relative paths.
    
    Args:
        gitbook_dir (str): Path to the GitBook directory
    """
    print(f"Fixing internal links in {gitbook_dir}...")
    
    # Get all markdown files
    md_files = list(Path(gitbook_dir).glob('**/*.md'))
    print(f"Found {len(md_files)} markdown files")
    
    # Create a mapping of Google Site URLs to local file paths
    url_to_path = {}
    
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for the original URL in the content (usually at the top)
        url_pattern = r'# .*?\n\n.*?(https://sites\.google\.com/.*?)\n'
        match = re.search(url_pattern, content)
        
        if match:
            original_url = match.group(1)
            rel_path = str(md_file.relative_to(gitbook_dir))
            url_to_path[original_url] = rel_path
    
    # Now fix the links in each file
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all markdown links
        link_pattern = r'\[(.*?)\]\((https://sites\.google\.com/.*?)\)'
        matches = re.findall(link_pattern, content)
        
        if matches:
            print(f"Found {len(matches)} internal links in {md_file}")
            
            # Replace each link
            for link_text, url in matches:
                if url in url_to_path:
                    # Get the relative path from the current file to the target file
                    from_dir = os.path.dirname(md_file)
                    to_file = os.path.join(gitbook_dir, url_to_path[url])
                    rel_path = os.path.relpath(to_file, from_dir)
                    
                    # Replace the link in the content
                    content = content.replace(
                        f"[{link_text}]({url})",
                        f"[{link_text}]({rel_path})"
                    )
            
            # Write the updated content back to the file
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)


def create_book_json(gitbook_dir, title="GitBook Documentation", author="Author"):
    """
    Create a book.json file in the GitBook directory.
    
    Args:
        gitbook_dir (str): Path to the GitBook directory
        title (str): Title of the GitBook
        author (str): Author of the GitBook
    """
    print(f"Creating book.json in {gitbook_dir}...")
    
    book_json = {
        "title": title,
        "description": "Documentation generated from Google Sites",
        "author": author,
        "language": "en",
        "structure": {
            "readme": "README.md",
            "summary": "SUMMARY.md"
        },
        "plugins": [
            "highlight",
            "search",
            "theme-default",
            "expandable-chapters",
            "back-to-top-button"
        ],
        "pluginsConfig": {
            "theme-default": {
                "showLevel": True
            }
        }
    }
    
    import json
    with open(os.path.join(gitbook_dir, 'book.json'), 'w', encoding='utf-8') as f:
        json.dump(book_json, f, indent=2)


def main():
    """
    Main function to run the utilities.
    """
    parser = argparse.ArgumentParser(description='Utilities for Google Sites to GitBook conversion')
    parser.add_argument('--gitbook', required=True, help='Path to the GitBook directory')
    parser.add_argument('--fix-images', action='store_true', help='Fix image links')
    parser.add_argument('--download-images', action='store_true', help='Download images to assets folder')
    parser.add_argument('--max-workers', type=int, default=10, help='Maximum number of concurrent image downloads')
    parser.add_argument('--fix-links', action='store_true', help='Fix internal links')
    parser.add_argument('--create-book-json', action='store_true', help='Create book.json file')
    parser.add_argument('--title', default='GitBook Documentation', help='Title for the GitBook')
    parser.add_argument('--author', default='Author', help='Author of the GitBook')
    
    args = parser.parse_args()
    
    if args.fix_images:
        fix_image_links(args.gitbook, download=args.download_images, max_workers=args.max_workers)
    
    if args.fix_links:
        fix_internal_links(args.gitbook)
    
    if args.create_book_json:
        create_book_json(args.gitbook, args.title, args.author)


if __name__ == '__main__':
    main()
