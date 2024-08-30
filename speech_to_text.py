import whisper
import os


class SpeechToText:
    def __init__(self, model_name='base', language='en'):
        """
        Initialize the Whisper model.

        Args:
        - model_name (str): The name of the Whisper model to load. Options include 'tiny', 'base', 'small', 'medium', 'large'.
        """
        self.language = language
        print(f"Loading Whisper model: {model_name}...")
        self.model = whisper.load_model(model_name)
        print("Model loaded successfully!")

    def convert_audio_to_text(self, audio_file, subtitle_file_path):
        """
        Converts audio to text using the Whisper model and generates subtitles.

        Args:
        - audio_file (str): The path to the audio file to transcribe.

        Returns:
        - transcription (str): The transcribed text from the audio.
        - subtitle_file (str): Path to the generated subtitle file.
        """
        # Check if audio file exists
        if not os.path.isfile(audio_file):
            raise FileNotFoundError(f"Audio file {audio_file} not found")

        print(f"Transcribing audio from {audio_file}...")
        result = self.model.transcribe(audio_file, language=self.language, word_timestamps=True)
        segments = result['segments']

        # Generate SRT subtitles
        subtitle_file = subtitle_file_path
        self.generate_srt_subtitles(segments, subtitle_file)

        print("Transcription complete!")
        return subtitle_file

    def generate_srt_subtitles(self, segments, output_srt):
        """
        Converts transcription segments into SRT subtitle format.

        Args:
        - segments (list): List of segments with start, end, and text.
        - output_srt (str): Path to the output SRT file.
        """
        with open(output_srt, 'w', encoding='utf-8') as f:
            for idx, segment in enumerate(segments):
                # Extract start and end times
                start_time = segment['start']  # in seconds
                end_time = segment['end']  # in seconds
                text = segment['text']

                # Convert seconds to HH:MM:SS,MS format
                start_time_formatted = self.format_time_srt(start_time)
                end_time_formatted = self.format_time_srt(end_time)

                # Write to the SRT file
                f.write(f"{idx + 1}\n")
                f.write(f"{start_time_formatted} --> {end_time_formatted}\n")
                f.write(f"{text}\n\n")

    def format_time_srt(self, seconds):
        """
        Formats time from seconds to SRT time format.

        Args:
        - seconds (float): Time in seconds.

        Returns:
        - str: Time in HH:MM:SS,MS format.
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        milliseconds = int((seconds - int(seconds)) * 1000)
        return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


