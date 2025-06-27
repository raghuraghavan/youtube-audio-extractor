"""# README for YouTube Audio Extractor Script
## Overview
This script allows you to download the audio from a YouTube video and save it as an MP3 file. It uses `yt-dlp`, a powerful command-line tool for downloading videos from YouTube and other sites, and requires `ffmpeg` for audio conversion.
## Requirements
- Python 3.x
- `yt-dlp` library
- `ffmpeg` installed and available in PATH

## Installation
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install `yt-dlp` using pip:
   ```
   pip install yt-dlp
   ```
3. Install `ffmpeg`:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.
   - **macOS**: Use Homebrew:
     ```
     brew install ffmpeg
     ```
   - **Linux**: Use your package manager, e.g.:
     ```
     sudo apt install ffmpeg
     ```

## Usage
Run the script from the command line:
```
python main.py <YouTube-URL> [-o <output-dir>] [-f <filename>] [--ffmpeg-path <path-to-ffmpeg>]
```

## Example
```
python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ -o ~/Downloads -f my_audio
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.   
## Troubleshooting
If you encounter issues:
- Ensure `yt-dlp` is installed correctly by running `yt-dlp --version`.
- Ensure `ffmpeg` is installed and available in your PATH by running `ffmpeg -version`.
- If `ffmpeg` is not in your PATH, specify its location using the `--ffmpeg-path` argument.
## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.
## Contact
For any questions or feedback, please contact the author at [raghu.x.raghavan@kp.org](mailto:raghu.x.raghavan@kp.org).
