# MP3 Merge with Crossfade and Fade-Out

This Python script allows you to select multiple MP3 files from your local machine, merge them with smooth crossfade transitions, and apply a final fade-out at the end of the result.

## Features

- Select multiple `.mp3` files using a file dialog
- Merge them with adjustable crossfade transitions (default: 2 seconds)
- Add a final fade-out (default: 5 seconds)
- Save the resulting file anywhere you like

## Requirements

- Python 3.x
- [FFmpeg](https://ffmpeg.org/) installed and added to system PATH
- Python libraries:
  ```bash
  pip install pydub
