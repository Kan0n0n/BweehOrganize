import os
import shutil
import datetime
import sys
import argparse

class BweehOrganize:
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.file_types = {
            "Images":    ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', '.webp', '.ico', '.raw', '.heic'],
            "Documents": ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages', '.tex', '.wpd'],
            "Spreadsheets": ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
            "Presentations": ['.ppt', '.pptx', '.odp', '.key'],
            "Videos":    ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.m4v', '.3gp', '.mpg', '.mpeg'],
            "Audio":     ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus'],
            "Archives":  ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
            "Code":      ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.php', '.rb', '.go', '.rs', '.swift'],
            "Executables": ['.exe', '.msi', '.dmg', '.deb', '.rpm', '.app'],
            "Fonts":     ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
        }

    def organize_by_type_and_date(self):
        if not os.path.isdir(self.source_dir):
            print(f"Source directory '{self.source_dir}' does not exist.")
            sys.exit(1)

        if not os.path.isdir(self.target_dir):
            print(f"Target directory '{self.target_dir}' does not exist. Creating it.")
            os.makedirs(self.target_dir, exist_ok=True)

        files_moved = 0
        for filename in os.listdir(self.source_dir):
            file_path = os.path.join(self.source_dir, filename)
            
            # Skip system files like desktop.ini
            if filename.lower() in ['desktop.ini', 'thumbs.db', '.ds_store']:
                print(f"Skipping system file: {filename}")
                continue
            
            # Skip if file is a folder
            if os.path.isdir(file_path):
                print(f"Skipping directory: {filename}")
                continue
            
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                ext = ext.lower()
                is_other = True

                # find matching category
                for category, extensions in self.file_types.items():
                    if ext in extensions:
                        # Create category subfolder if it doesn't exist
                        dest = os.path.join(self.target_dir, category)
                        os.makedirs(dest, exist_ok=True)
                        
                        # date subfolder
                        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                        sub = mtime.strftime("%Y-%m")
                        dest = os.path.join(self.target_dir, category, sub)
                        os.makedirs(dest, exist_ok=True)
                        shutil.move(file_path, os.path.join(dest, filename))
                        print(f"Moved {filename} → {dest}")
                        files_moved += 1
                        is_other = False
                        break
                    
                if is_other:
                    # If no category matches, move to "Others/Month-Year"
                    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    sub = mtime.strftime("%Y-%m")
                    dest = os.path.join(self.target_dir, "Others", sub)
                    os.makedirs(dest, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest, filename))
                    print(f"Moved {filename} → {dest}")
                    files_moved += 1

        print(f"Done. Bweeh {files_moved} files.")
        return files_moved

def main():
    p = argparse.ArgumentParser(description="Organize files by type and date")
    p.add_argument("-s", "--source", required=True, help="Source directory")
    p.add_argument("-t", "--target", required=True, help="Target directory")
    args = p.parse_args()

    organizer = BweehOrganize(args.source, args.target)
    organizer.organize_by_type_and_date()

if __name__ == "__main__":
    main()
