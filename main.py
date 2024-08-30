import tkinter as tk
import os
from tkinter import filedialog
from audio_extractor import AudioExtractor
from speech_to_text import SpeechToText
from add_subtitles import AddSubtitles


def browse_file(file_type_desc, file_extensions):
    """
    Opens a file dialog to select a file and returns the file path.

    Args:
    - file_type_desc (str): Description of the file type (e.g., "Video files").
    - file_extensions (list): List of file extensions to filter (e.g., ["*.mp4", "*.avi"]).

    Returns:
    - str: The path to the selected file.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        filetypes=[(file_type_desc, file_extensions)],
        title="Select a Video File"
    )
    return file_path


# def save_file(file_type_desc, file_extensions):
#     """"
#     Opens a file save dialog to specify where to save a file and returns the file path.
#
#     Args:
#     - file_type_desc (str): Description of the file type (e.g., "MP4 files").
#     - file_extensions (list): List of file extensions to filter (e.g., ["*.mp4"]).
#
#     Returns:
#     - str: The path to save the file.
#     """
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window
#     file_path = filedialog.asksaveasfilename(
#         default_extension=file_extensions[0],
#         filetypes=[(file_type_desc, file_extensions)],
#         title="Save Video File As"
#     )
#     return file_path


def main():
    # User inputs
    print("Select the video file...")
    video_file = browse_file("Video files", ["*.mp4", "*.avi", "*.mov", "*.mkv"])
    if not video_file:
        print("No video file selected.")
        return

    output_video_file = os.path.basename(video_file)
    output_audio_path = os.path.splitext(output_video_file)[0] + ".mp3"
    subtitle_file = os.path.splitext(output_video_file)[0] + ".srt"

    # Check if the video file exists
    if not os.path.isfile(video_file):
        print(f"Video file {video_file} not found.")
        return

    # Extract audio from video
    print("Extracting audio from the video...")
    audio_extractor = AudioExtractor(video_file)
    audio_file = audio_extractor.extract_audio(output_audio_path)

    # Convert audio to text and generate subtitles
    print("Converting audio to text and generating subtitles...")
    stt = SpeechToText(model_name='base')  # Use the appropriate Whisper model
    subtitle_file = stt.convert_audio_to_text(audio_file, subtitle_file)

    # Add subtitles to video
    print("Adding subtitles to the video...")
    adder = AddSubtitles(video_file, subtitle_file)
    adder.add_subtitles(output_video_file)

    print(f"Processing complete! The video with subtitles is saved as {output_video_file}")


if __name__ == "__main__":
    main()
