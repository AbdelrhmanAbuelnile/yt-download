#!/usr/bin/env python3
# Save this file as yt-download.py

import sys
import os
import argparse
import yt_dlp

def download_progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%')
        speed = d.get('_speed_str', '?')
        eta = d.get('_eta_str', '?')
        filename = os.path.basename(d.get('filename', 'Unknown'))
        print(f"\rDownloading {filename}... {percent} at {speed}, ETA: {eta}", end='')
    elif d['status'] == 'finished':
        print("\nDownload finished. Processing file...")

def get_format_string(quality):
    """Convert quality setting to yt-dlp format string"""
    if quality == 'best':
        return 'best'
    elif quality == '4k' or quality == '2160p':
        return 'bestvideo[height<=2160]+bestaudio/best'
    elif quality == '1440p':
        return 'bestvideo[height<=1440]+bestaudio/best'
    elif quality == '1080p':
        return 'bestvideo[height<=1080]+bestaudio/best'
    elif quality == '720p':
        return 'bestvideo[height<=720]+bestaudio/best'
    elif quality == '480p':
        return 'bestvideo[height<=480]+bestaudio/best'
    elif quality == '360p':
        return 'bestvideo[height<=360]+bestaudio/best'
    elif quality == '240p':
        return 'bestvideo[height<=240]+bestaudio/best'
    elif quality == '144p':
        return 'bestvideo[height<=144]+bestaudio/best'
    else:
        return 'best'

def list_formats(url):
    """List all available formats for the video(s)"""
    print(f"Fetching available formats for: {url}")
    ydl_opts = {
        'listformats': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_video(url, output_path=None, quality='best', format_id=None, list_only=False, audio_only=False):
    """Download YouTube video or playlist using yt-dlp"""
    try:
        # If user just wants to list formats, do that and return
        if list_only:
            list_formats(url)
            return True
            
        # Set default output path if not specified
        if not output_path:
            output_path = os.getcwd()
        
        # Make sure output directory exists
        os.makedirs(output_path, exist_ok=True)
        
        # Determine if URL is a playlist
        is_playlist = 'playlist' in url or 'list=' in url
        
        # Configure output template based on whether it's a playlist
        if is_playlist:
            output_template = os.path.join(output_path, '%(playlist_title)s/%(playlist_index)s-%(title)s.%(ext)s')
        else:
            output_template = os.path.join(output_path, '%(title)s.%(ext)s')
        
        # Configure format based on parameters
        if audio_only:
            format_string = 'bestaudio/best'
            postprocessors = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        elif format_id:
            format_string = format_id
            postprocessors = []
        else:
            format_string = get_format_string(quality)
            postprocessors = []
        
        # Configuration for yt-dlp
        ydl_opts = {
            'format': format_string,
            'outtmpl': output_template,
            'progress_hooks': [download_progress_hook],
            'ignoreerrors': True,
            'no_warnings': False,
            'quiet': False,
            'verbose': False,
            'postprocessors': postprocessors,
            # For playlists
            'extract_flat': 'in_playlist',
            'noplaylist': False if is_playlist else True,
        }
        
        print(f"Downloading from: {url}")
        print(f"Output directory: {output_path}")
        print(f"Quality: {quality if not format_id else f'Format ID: {format_id}'}")
        print(f"Type: {'Audio only (MP3)' if audio_only else 'Video with audio'}")
        if is_playlist:
            print("Detected playlist URL. Will download all videos in the playlist.")
        
        # Download the video or playlist
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.download([url])
            
        print("\nDownload completed successfully!")
        return True
                
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Check your internet connection")
        print("2. Verify the YouTube URL is correct and accessible")
        print("3. Some YouTube videos might be restricted or region-locked")
        print("4. Try listing available formats with --list-formats")
        return False

def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos or playlists from the command line")
    parser.add_argument("url", help="YouTube video or playlist URL")
    parser.add_argument("-o", "--output", help="Output directory (optional)")
    parser.add_argument("-q", "--quality", choices=['best', '4k', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p'], 
                        default='best', help="Video quality (default: best)")
    parser.add_argument("-f", "--format", dest="format_id", help="Specific format ID (overrides quality setting)")
    parser.add_argument("-F", "--list-formats", action="store_true", help="List all available formats and exit")
    parser.add_argument("-a", "--audio-only", action="store_true", help="Download audio only (MP3)")
    
    args = parser.parse_args()
    
    download_video(args.url, args.output, args.quality, args.format_id, args.list_formats, args.audio_only)

if __name__ == "__main__":
    main()