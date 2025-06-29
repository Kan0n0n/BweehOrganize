# Bweeh Organize 📁

A Python script that automatically organizes files by type and date, helping you keep your directories clean and structured.

## Features

- **File Type Classification**: Automatically categorizes files into predefined types (Images, Documents, Videos, etc.)
- **Date-based Organization**: Creates subfolders based on file modification date (YYYY-MM format)
- **Smart Handling**: Skips system files and directories automatically
- **Comprehensive File Support**: Supports a wide range of file extensions across multiple categories

## Supported File Types

| Category | Extensions |
|----------|------------|
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.tif`, `.svg`, `.webp`, `.ico`, `.raw`, `.heic` |
| **Documents** | `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.odt`, `.pages`, `.tex`, `.wpd` |
| **Spreadsheets** | `.xls`, `.xlsx`, `.csv`, `.ods`, `.numbers` |
| **Presentations** | `.ppt`, `.pptx`, `.odp`, `.key` |
| **Videos** | `.mp4`, `.avi`, `.mov`, `.wmv`, `.flv`, `.mkv`, `.webm`, `.m4v`, `.3gp`, `.mpg`, `.mpeg` |
| **Audio** | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a`, `.opus` |
| **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz` |
| **Code** | `.py`, `.js`, `.html`, `.css`, `.cpp`, `.c`, `.java`, `.php`, `.rb`, `.go`, `.rs`, `.swift` |
| **Executables** | `.exe`, `.msi`, `.dmg`, `.deb`, `.rpm`, `.app` |
| **Fonts** | `.ttf`, `.otf`, `.woff`, `.woff2`, `.eot` |

Files that don't match any category are placed in the "Others" folder.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Kan0n0n/BweehOrganize.git
cd BweehOrganize
```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Command Line Interface

```bash
python organize.py -s /path/to/source/directory -t /path/to/target/directory
```

### Parameters

- `-s, --source`: Source directory containing files to organize (required)
- `-t, --target`: Target directory where organized files will be moved (required)

### Example

```bash
# Organize files from Downloads folder to an Organized folder
python organize.py -s "C:\Users\YourName\Downloads" -t "C:\Users\YourName\Organized"
```

## How It Works

1. **Scans** the source directory for files
2. **Skips** system files (`desktop.ini`, `thumbs.db`, `.ds_store`) 
3. **Categorizes** files based on their extensions
4. **Creates** organized folder structure: `Target/Category/YYYY-MM/`
5. **Moves** files to their appropriate destinations
6. **Reports** the number of files successfully organized

## Folder Structure Example

After running the script, your target directory will look like this:

```
Organized/
├── Images/
│   ├── 2024-01/
│   │   ├── photo1.jpg
│   │   └── screenshot.png
│   └── 2024-02/
│       └── vacation.heic
├── Documents/
│   └── 2024-01/
│       ├── report.pdf
│       └── notes.txt
├── Videos/
│   └── 2024-02/
│       └── movie.mp4
└── Others/
    └── 2024-01/
        └── unknown_file.xyz
```

## Safety Features

- **Non-destructive**: Files are moved, not copied (no duplication)
- **Directory creation**: Automatically creates target directories if they don't exist
- **Error handling**: Graceful handling of missing source directories
- **System file awareness**: Skips common system files automatically

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool!

## License

This project is open source. Feel free to use and modify as needed.

---

*"Bweeh" your files into perfect organization! 🎯*