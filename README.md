# Video Subtitle Generator

The Video Subtitle Generator is a web application that automates the process of adding subtitles to video files. Leveraging advanced speech-to-text technology, this tool extracts audio from video files, transcribes the audio into text, and embeds the generated subtitles into the video. Built with Python and utilizing the Whisper model, the application provides a seamless user experience through a web interface created with Streamlit.

## Key Features

- **Audio Extraction**: Extracts audio from various video formats without saving intermediate files.
- **Speech-to-Text Transcription**: Converts spoken content into text using the Whisper model, supporting multiple languages.
- **Subtitle Embedding**: Integrates subtitles directly into the video, ensuring synchronization with the audio.
- **Web Interface**: Easy-to-use interface for file uploads and processing, built with Streamlit.

## Installation

To set up and run the Video Subtitle Generator locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Devil-1412/video_subtitle_generator.git

2. **Navigate to the Project Directory**:

   ```bash
   cd video_subtitle_generator

3. **Set Up a Virtual Environment (optional but recommended)**:

   ```bash
   python -m venv .venv

4. **Activate the Virtual Environment**:

  - **Windows**:
     
     ```bash
     .venv\Scripts\activate

  - **macOS/Linux**:

    ```bash
    source .venv/bin/activate

5. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt


## Usage

1. **Run the Streamlit app**:

   ```bash
   streamlit run webApp.py

2. **Upload a Video**:

   - Open your browser and navigate to http://localhost:8501 (or the address shown in the terminal). 
   - Use the web interface to upload a video file.

3. **Process and Download**:

   - The app will process the video, generate subtitles, and provide an option to download the video with embedded subtitles.
