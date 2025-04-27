import os
import shutil
from pathlib import Path

def restructure_gitbook(directory):
    """
    Restructure a directory to match GitBook's directory structure.
    If a page has the same name as a folder, move its contents to README.md inside the folder.
    """
    directory = Path(directory)
    
    # Get all .md files and directories
    md_files = {f.stem: f for f in directory.rglob('*.md')}
    dirs = {d.name: d for d in directory.rglob('*') if d.is_dir()}
    
    # Find cases where we have both a .md file and a directory with the same name
    for name in set(md_files.keys()) & set(dirs.keys()):
        md_file = md_files[name]
        dir_path = dirs[name]
        
        # Skip if the md_file is already inside its namesake directory
        if md_file.parent == dir_path:
            continue
            
        readme_path = dir_path / 'README.md'
        
        # Copy content to README.md in the directory
        print(f"Moving content from {md_file} to {readme_path}")
        shutil.copy2(md_file, readme_path)
        
        # Delete the original .md file
        print(f"Deleting {md_file}")
        md_file.unlink()

if __name__ == '__main__':
    gitbook_dir = '/Users/akhilmarri/Google-Site-Scraper/gitbook_output/testduplicationsscp'
    restructure_gitbook(gitbook_dir)
