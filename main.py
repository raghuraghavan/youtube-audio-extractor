#!/usr/bin/env python3
"""
YouTube Audio Extractor Script
------------------------------
This script downloads the audio from a YouTube video URL and saves it as an MP3 file.
Uses yt-dlp which is more reliable and frequently updated compared to pytube.
Requires ffmpeg to be installed for audio conversion.
"""

import os
import argparse
import subprocess
import sys


def download_audio(url, output_path=None, filename=None, ffmpeg_path=None):
    """
    Download audio from a YouTube video using yt-dlp.
    
    Args:
        url (str): YouTube video URL
        output_path (str, optional): Directory to save the audio file
        filename (str, optional): Custom filename (without extension)
        ffmpeg_path (str, optional): Path to ffmpeg executable
        
    Returns:
        str: Path to the downloaded audio file
    """
    try:
        # Set default output path if not provided
        if not output_path:
            output_path = os.getcwd()
        
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Prepare the yt-dlp command
        cmd = ["yt-dlp", "--extract-audio", "--audio-format", "mp3"]
        
        # Add ffmpeg location if provided
        if ffmpeg_path:
            cmd.extend(["--ffmpeg-location", ffmpeg_path])
        
        # Add output path
        cmd.extend(["-o", os.path.join(output_path, "%(title)s.%(ext)s")])
        
        # Add custom filename if provided
        if filename:
            cmd = ["yt-dlp", "--extract-audio", "--audio-format", "mp3"]
            
            # Re-add ffmpeg path if it was specified
            if ffmpeg_path:
                cmd.extend(["--ffmpeg-location", ffmpeg_path])
                
            cmd.extend(["-o", os.path.join(output_path, f"{filename}.%(ext)s")])
        
        # Add the URL
        cmd.append(url)
        
        # Print the command being executed
        print(f"Executing: {' '.join(cmd)}")
        
        # Run the command
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return None
        
        print(f"Output: {result.stdout}")
        print("Download complete!")
        
        # Extract the filename from the output
        for line in result.stdout.split('\n'):
            if "[ExtractAudio] Destination:" in line:
                return line.split("[ExtractAudio] Destination:")[1].strip()
        
        return "Audio downloaded successfully, but couldn't determine the exact file path."
        
    except FileNotFoundError:
        print("Error: yt-dlp is not installed. Please install it using:")
        print("pip install yt-dlp")
        print("Or visit: https://github.com/yt-dlp/yt-dlp#installation")
    except Exception as e:
        print(f"An error occurred: {e}")


def check_ffmpeg():
    """Check if ffmpeg is installed and available in PATH"""
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        return True
    except FileNotFoundError:
        return False

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Download audio from YouTube videos")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", help="Output directory path", default=None)
    parser.add_argument("-f", "--filename", help="Output filename (without extension)", default=None)
    parser.add_argument("--ffmpeg-path", help="Path to ffmpeg executable (if not in PATH)", default=None)
    
    args = parser.parse_args()
    
    # Check if yt-dlp is installed
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True)
    except FileNotFoundError:
        print("Error: yt-dlp is not installed. Please install it using:")
        print("pip install yt-dlp")
        print("Or visit: https://github.com/yt-dlp/yt-dlp#installation")
        sys.exit(1)
    
    # Check if ffmpeg is installed
    if not check_ffmpeg() and not args.ffmpeg_path:
        print("Error: ffmpeg is not installed or not in PATH.")
        print("Please install ffmpeg:")
        if sys.platform == 'win32':
            print("- Windows: Download from https://ffmpeg.org/download.html")
            print("  After installation, add to PATH or use --ffmpeg-path argument")
        elif sys.platform == 'darwin':
            print("- macOS: Use 'brew install ffmpeg'")
        else:
            print("- Linux: Use 'apt install ffmpeg' or equivalent for your distribution")
        print("\nAlternatively, specify path with --ffmpeg-path /path/to/ffmpeg")
        sys.exit(1)
    
    # Download the audio
    download_audio(args.url, args.output, args.filename, args.ffmpeg_path)


if __name__ == "__main__":
    main()