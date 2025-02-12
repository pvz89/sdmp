import streamlit as st
import yt_dlp
import os
from pathlib import Path

# Create downloads directory if not exists
Path("downloads").mkdir(exist_ok=True)

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        mp3_filename = os.path.splitext(filename)[0] + '.mp3'
        return mp3_filename

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- [About Us](#about-us)
- [Blog](#blog)
- [Contact](#contact)
- [Language](#language)
""")

# Main content
st.title("SoundCloud Downloader To MP3 Tool")
st.write("Convert and download SoundCloud tracks to MP3 format")

url = st.text_input("SoundCloud Track Link", placeholder="Paste track URL here")

if st.button("Download MP3 Track"):
    if url:
        try:
            with st.spinner('Downloading... This may take a moment'):
                mp3_path = download_audio(url)
                
                with open(mp3_path, "rb") as f:
                    btn = st.download_button(
                        label="Download MP3 File",
                        data=f,
                        file_name=os.path.basename(mp3_path),
                        mime="audio/mpeg"
                    )
                
                # Clean up file after download
                os.remove(mp3_path)
        except Exception as e:
            st.error(f"Error downloading track: {str(e)}")
    else:
        st.warning("Please enter a SoundCloud track URL")

# Footer
st.markdown("---")
st.markdown("""
**Disclaimer:** This tool is for educational purposes only. 
Please ensure you have the right to download and use any content.
""")
