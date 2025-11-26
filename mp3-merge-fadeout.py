import os
from tkinter import Tk, filedialog
from pydub import AudioSegment

# Required libraries:
# pip install pydub
# Ensure ffmpeg is installed and added to your system PATH.


def select_files():
    """Show a file dialog to select multiple MP3 files."""
    root = Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Select MP3 files",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    return list(file_paths)


def merge_with_transitions_and_fadeout(file_paths, output_path, transition_duration=2000, fadeout_duration=5000):
    """Merge MP3 files with crossfade transitions and a final fade-out.

    Args:
        file_paths (list): List of MP3 file paths.
        output_path (str): Path to save the merged MP3 file.
        transition_duration (int): Duration of crossfade in milliseconds.
        fadeout_duration (int): Duration of fade-out at the end in milliseconds.
    """
    if not file_paths:
        print("No files selected.")
        return

    print("Loading and processing files...")
    combined = AudioSegment.empty()

    for i, file_path in enumerate(file_paths):
        audio = AudioSegment.from_mp3(file_path)
        if i > 0:
            combined = combined.append(audio, crossfade=transition_duration)
        else:
            combined += audio

    print("Applying final fade-out...")
    combined = combined.fade_out(fadeout_duration)

    print("Exporting merged file...")
    combined.export(output_path, format="mp3")
    print(f"File saved at: {output_path}")


if __name__ == "__main__":
    print("Select the MP3 files to merge.")
    files = select_files()
    if files:
        output_file = filedialog.asksaveasfilename(
            title="Save merged MP3 file",
            defaultextension=".mp3",
            filetypes=[("MP3 Files", "*.mp3")]
        )
        if output_file:
            merge_with_transitions_and_fadeout(files, output_file)
        else:
            print("No output path selected.")
    else:
        print("No files selected.")
