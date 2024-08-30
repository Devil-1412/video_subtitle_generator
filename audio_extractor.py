import ffmpeg
import os


class AudioExtractor:
    def __init__(self, input_video):
        self.input_video = input_video

        # Check if input video file exists
        if not os.path.isfile(input_video):
            raise FileNotFoundError(f"Video file {input_video} not found")

    def extract_audio(self, output_audio_path):
        """
        Extracts audio from the video and saves it as an audio file.

        Args:
        - output_audio (str): The output file path for the extracted audio.

        Returns:
        -
        """
        output_audio = output_audio_path
        try:
            # Use ffmpeg to extract the audio
            ffmpeg.input(self.input_video).output(output_audio, **{'q:a': 0, 'map': 'a'}).run()
            print(f"Audio extracted successfully to {output_audio}")
            return output_audio
        except ffmpeg.Error as e:
            print(f"Error extracting audio: {e}")
            raise


