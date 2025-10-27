#!/usr/bin/env python3

'''Organize files in a directory into subdirectories based on file extensions.

Usage:
    python organize.py <directory_path>

     This script will create subdirectories for each file extension found in the specified directory
     and move the files into their respective subdirectories.
     Example:
         python organize.py /path/to/directory
'''

import sys
from pathlib import Path;
import shutil
import argparse
import logging


EXT_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Code': ['.py', '.js', '.java', '.c', '.cpp'],
    'Other': []
}

logging.basicConfig(filename="logs/organizer.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def classify(ext:str):
    ext = ext.lower()
    for category, extensions in EXT_MAP.items():
        if ext in extensions:
            return category
    return 'Other'

def organize_folder(target_dir: Path, dry_run: bool=False):
    if not target_dir.is_dir():
        raise NotADirectoryError(str(target_dir) + " is not a valid directory.")
    
    for item in target_dir.iterdir():
        if item.is_dir():
            continue
        category = classify(item.suffix)
        dest_dir = target_dir / category
        dest_dir.mkdir(exist_ok=True)
        dest_file = dest_dir / item.name
        logging.info(f'{'DRY:' if dry_run else ''} Moving {item.name} to {dest_dir}/')
        if not dry_run:
            # If file exists, append a number to the filename
            if dest_file.exists():
                stem = item.stem
                i = 1
                while True:
                    new_name = f"{stem}_{i}{item.suffix}"
                    dest_file = dest_dir / new_name
                    if not dest_file.exists():
                        break
                    i += 1
            shutil.move(str(item), str(dest_file))

def main():
    parser = argparse.ArgumentParser(description='Organize files in a directory by their extensions.')
    parser.add_argument('directory', type=Path, help='Path to the target directory.')
    parser.add_argument('--dry-run', action='store_true', help='Simulate the organization without moving files.')
    args = parser.parse_args()
    try:
        logging.info("Performing dry run...")
        organize_folder(args.directory, dry_run=args.dry_run)
        confirm = input("\nDry run complete. Apply these changes? (y/n): ").strip().lower() 
        if confirm == 'y':
            logging.info("Organizing files...")
            organize_folder(args.directory, dry_run=False)
            logging.info("Organization complete.")
        else:
            logging.info("Operation cancelled by user.")
    except Exception as e:
        logging.error(f'Error: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()