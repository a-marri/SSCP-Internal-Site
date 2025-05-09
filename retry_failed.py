#!/usr/bin/env python3
"""
Retry Failed Pages Script

This script reads the error_pages.txt file generated by the scraper and attempts to
scrape the failed pages again. This is useful when some pages fail due to temporary
network issues or rate limiting.
"""

import os
import re
import argparse
from scraper import GoogleSiteScraper

def parse_error_file(error_file):
    """
    Parse the error_pages.txt file to extract page titles, URLs, and output paths.
    
    Args:
        error_file (str): Path to the error_pages.txt file
        
    Returns:
        list: List of tuples with (title, url, output_path)
    """
    if not os.path.exists(error_file):
        print(f"Error file not found: {error_file}")
        return []
    
    failed_pages = []
    with open(error_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('-'):
                # Extract information using regex
                match = re.search(r'\[(.*?)\]\((.*?)\) -> (.*?)$', line.strip())
                if match:
                    title, url, output_path = match.groups()
                    failed_pages.append((title, url, output_path))
    
    return failed_pages

def retry_failed_pages(error_file, download_images=False, max_workers=10):
    """
    Retry scraping the failed pages.
    
    Args:
        error_file (str): Path to the error_pages.txt file
        download_images (bool): Whether to download images
        max_workers (int): Maximum number of concurrent workers for image download
    """
    failed_pages = parse_error_file(error_file)
    
    if not failed_pages:
        print("No failed pages found to retry.")
        return
    
    print(f"Found {len(failed_pages)} failed pages to retry.")
    
    # Determine the output directory from the first output path
    output_dir = os.path.dirname(os.path.dirname(failed_pages[0][2]))
    
    # Create a temporary scraper instance
    scraper = GoogleSiteScraper(
        summary_file=None,  # Not using a summary file for retry
        output_dir=output_dir,
        download_images=download_images,
        max_workers=max_workers
    )
    
    # Run the scraper on each failed page
    success_count = 0
    still_failed = []
    
    for title, url, output_path in failed_pages:
        print(f"Retrying: {title} ({url})")
        try:
            content = scraper.scrape_page(url, output_path)
            
            if content and "# Error" not in content:
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Save content to markdown file
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Success: {output_path}")
                success_count += 1
            else:
                print(f"Failed again: {title}")
                still_failed.append((title, url, output_path))
        except Exception as e:
            print(f"Error retrying {url}: {e}")
            still_failed.append((title, url, output_path))
    
    # Wait for any pending image downloads to complete
    if download_images and hasattr(scraper, 'download_futures'):
        print(f"Waiting for {len(scraper.download_futures)} image downloads to complete...")
        for future, img_url, img_output_path in scraper.download_futures:
            try:
                result = future.result()
                status = "Success" if result else "Failed"
                print(f"{status}: {os.path.basename(img_output_path)} from {img_url}")
            except Exception as e:
                print(f"Failed: {os.path.basename(img_output_path)} from {img_url}. Error: {e}")
        
        # Shutdown the executor
        scraper.executor.shutdown()
    
    # Report results
    print("\n=== Retry Results ===")
    print(f"Successfully retried: {success_count}/{len(failed_pages)} pages")
    
    if still_failed:
        print(f"Still failed: {len(still_failed)} pages")
        
        # Save still failed pages to a new file
        new_error_file = os.path.join(output_dir, "still_failed_pages.txt")
        with open(new_error_file, 'w', encoding='utf-8') as f:
            f.write("# Pages still failing after retry\n\n")
            for title, url, path in still_failed:
                f.write(f"- [{title}]({url}) -> {path}\n")
        print(f"Still failing pages list saved to: {new_error_file}")

def main():
    parser = argparse.ArgumentParser(description='Retry failed pages from Google Site scraping')
    parser.add_argument('--error-file', default='error_pages.txt', help='Path to the error_pages.txt file')
    parser.add_argument('--download-images', action='store_true', help='Download images for retried pages')
    parser.add_argument('--max-workers', type=int, default=10, help='Maximum number of concurrent image download workers')
    
    args = parser.parse_args()
    
    retry_failed_pages(args.error_file, args.download_images, args.max_workers)

if __name__ == '__main__':
    main()
