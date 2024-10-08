import streamlit as st
from audio_extractor import AudioExtractor
from speech_to_text import SpeechToText
# from add_subtitles import AddSubtitles
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads/')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'outputs/')

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# Set title for the website
st.title("Video Subtitle Generator")

# File upload
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file is not None:
    # Configure file paths
    subtitle_file = os.path.splitext(uploaded_file.name)[0] + ".srt"
    extracted_audio = os.path.splitext(uploaded_file.name)[0] + ".mp3"
    sub_file_path = os.path.join(OUTPUT_FOLDER, subtitle_file)
    audio_path = os.path.join(OUTPUT_FOLDER, extracted_audio)
    
    # Save the uploaded file
    video_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded video: {uploaded_file.name}")

    # Extract audio
    st.write("Extracting audio from the video...")
    audio_extractor = AudioExtractor(video_path)
    extracted_audio_path = audio_extractor.extract_audio(audio_path)

    # Convert audio to text and generate subtitles
    st.write("Converting audio to text and generating subtitles...")
    stt = SpeechToText(model_name='base')

    stt.convert_audio_to_text(extracted_audio_path, sub_file_path)
    # output_video_file = os.path.join(OUTPUT_FOLDER, 'video_with_subtitles.mp4')

    # # Add subtitles to video (use only when ffmpeg path is provided to AddSubtitles)
    # st.write("Adding subtitles to video...")
    # adder = AddSubtitles(video_path, subtitle_file)
    # adder.add_subtitles(output_video_file)

    # Provide a download link for the video with subtitles
    st.write("Processing complete! Download subtitles for your video:")
    with open(sub_file_path, "rb") as f:
        st.download_button(
            label="Download subtitles",
            data=f,
            file_name={subtitle_file},
            mime="subtitle/srt"
        )
