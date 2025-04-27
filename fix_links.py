import os
from pathlib import Path
import re

def fix_links(directory):
    """
    Fix links in markdown files to use relative paths instead of absolute URLs.
    """
    directory = Path(directory)
    
    # Find all markdown files
    for md_file in directory.rglob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix links that start with /stanford.edu/testduplicationsscp/
        modified_content = re.sub(
            r'\[([^\]]+)\]\(/stanford\.edu/testduplicationsscp/([^\)]+)\)',
            lambda m: f'[{m.group(1)}](/{m.group(2)})',
            content
        )
        
        # Write back if content was modified
        if modified_content != content:
            print(f"Fixing links in {md_file}")
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)

if __name__ == '__main__':
    gitbook_dir = '/Users/akhilmarri/Google-Site-Scraper/gitbook_output/testduplicationsscp'
    fix_links(gitbook_dir)
