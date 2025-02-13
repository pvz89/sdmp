import streamlit as st
import yt_dlp
import os
from pathlib import Path
import imageio_ffmpeg

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
        'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe(),
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        mp3_filename = os.path.splitext(filename)[0] + '.mp3'
        return mp3_filename

# ========== Legal Pages Content ==========
def show_legal_pages():
    st.markdown("---")
    # DMCA Page
    with st.expander("DMCA Copyright Policy", expanded=False):
        st.markdown("""
        **soundcloudtomp3.pro DMCA Takedown Policy**
        [Content remains same as before]
        """)
    # Other pages remain same...

def main_footer():
    st.markdown("---")
    # Footer content remains same...

# ========== Main App UI ==========
def main():
    st.set_page_config(page_title="SoundCloud Downloader", layout="wide")
    
    # Header Navigation
    col1, col2, col3, col4 = st.columns(4)
    # ... [Header content remains same] ...
    
    # Main Converter Section
    with st.container():
        # ... [Main content remains same] ...
    
    # How To Use Section
    st.markdown("---")
    # ... [Rest of main content] ...
    
    # Show legal pages and footer
    show_legal_pages()
    main_footer()

if __name__ == "__main__":
    main()
