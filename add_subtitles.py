import subprocess
import os


class AddSubtitles:
    def __init__(self, video_file, subtitle_file):
        """
        Initialize the AddSubtitles class.

        Args:
        - video_file (str): The path to the video file.
        - subtitle_file (str): The path to the subtitle file (e.g., SRT).
        """
        self.video_file = video_file
        self.subtitle_file = subtitle_file

        # Check if video and subtitle files exist
        if not os.path.isfile(video_file):
            raise FileNotFoundError(f"Video file {video_file} not found")
        if not os.path.isfile(subtitle_file):
            raise FileNotFoundError(f"Subtitle file {subtitle_file} not found")

    def add_subtitles(self, output_file):
        """
        Adds subtitles to the video using FFmpeg.

        Args:
        - output_file (str): The path to the output video file with subtitles.
        """
        print(f"Adding subtitles from {self.subtitle_file} to {self.video_file}...")
        # Add your path to ffmpeg
        ffmpeg_path = r"C:\Users\hp\Downloads\ffmpeg-N-114855-g35ae44c615-win64-gpl\ffmpeg-N-114855-g35ae44c615-win64-gpl\bin\ffmpeg.exe"
        try:
            subprocess.run([
                ffmpeg_path,
                '-i', self.video_file,
                '-vf', f'subtitles={self.subtitle_file}',
                output_file
            ], check=True)
            print(f"Subtitles added successfully. Output file: {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error adding subtitles: {e}")
            raise
