# YT-Download

A powerful, easy-to-use command-line tool for downloading YouTube videos and playlists with quality options.

## Features

- Download single videos or entire playlists
- Select video quality (from 144p to 4K)
- Extract audio only (MP3)
- List available formats
- Choose specific format IDs
- Customize output directory
- Simple command-line interface

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install yt-download
```

### Option 2: Install from GitHub

```bash
pip install git+https://github.com/yourusername/yt-download.git
```

### Option 3: Manual Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yt-download.git
   cd yt-download
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install the package:
   ```bash
   pip install -e .
   ```

### Option 4: Standalone Executable (Windows)

1. Download the latest `yt-download.exe` from the [Releases](https://github.com/yourusername/yt-download/releases) page
2. Add the executable location to your PATH or use it directly

## Usage

### Basic Usage

Download a video at best quality:

```bash
yt-download https://www.youtube.com/watch?v=VIDEO_ID
```

### Quality Options

Download a video at a specific quality:

```bash
yt-download https://www.youtube.com/watch?v=VIDEO_ID -q 1080p
```

Available quality options:

- `best` (default)
- `4k` or `2160p`
- `1440p`
- `1080p`
- `720p`
- `480p`
- `360p`
- `240p`
- `144p`

### Format Selection

List all available formats for a video:

```bash
yt-download https://www.youtube.com/watch?v=VIDEO_ID -F
```

Download a specific format by its ID:

```bash
yt-download https://www.youtube.com/watch?v=VIDEO_ID -f 22
```

### Playlist Downloads

Download an entire YouTube playlist:

```bash
yt-download https://www.youtube.com/playlist?list=PLAYLIST_ID
```

### Audio Only

Extract audio and save as MP3:

```bash
yt-download https://www.youtube.com/watch?v=VIDEO_ID -a
```

### Output Directory

Specify where to save the downloaded files:

```bash
yt-download https://www.youtube.com/watch?v=VIDEO_ID -o /path/to/downloads
```

### Combining Options

You can combine multiple options:

```bash
yt-download https://www.youtube.com/playlist?list=PLAYLIST_ID -q 720p -o /path/to/downloads
```

## Command Line Options

| Option | Long Option      | Description                           |
| ------ | ---------------- | ------------------------------------- |
| `-q`   | `--quality`      | Set video quality (e.g., 1080p, 720p) |
| `-f`   | `--format`       | Select specific format ID             |
| `-F`   | `--list-formats` | List all available formats and exit   |
| `-a`   | `--audio-only`   | Download audio only (MP3)             |
| `-o`   | `--output`       | Specify output directory              |
| `-h`   | `--help`         | Show help message                     |

## Examples

### Example 1: Download a YouTube Short

```bash
yt-download https://www.youtube.com/shorts/jf3GOkuM-Xo
```

### Example 2: Download a High-Quality Music Video

```bash
yt-download https://www.youtube.com/watch?v=dQw4w9WgXcQ -q 1080p
```

### Example 3: Extract Audio from a Lecture

```bash
yt-download https://www.youtube.com/watch?v=VIDEO_ID -a -o ~/Lectures
```

### Example 4: Download an Educational Playlist

```bash
yt-download https://www.youtube.com/playlist?list=PLAYLIST_ID -q 720p -o ~/Courses
```

## Requirements

- Python 3.6 or higher
- yt-dlp

## Disclaimer

This tool is for personal use only. Respect copyright and YouTube's Terms of Service. Do not download or distribute copyrighted content without permission.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for providing the downloading functionality
- All contributors and users of this tool
