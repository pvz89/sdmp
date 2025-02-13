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

# ========== Frontend Design ==========
st.set_page_config(page_title="SoundCloud Downloader", layout="wide")

# Header Navigation
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("[About Us](#about-us)")
with col2:
    st.markdown("[Blog](#blog)")
with col3:
    st.markdown("[Contact](#contact)")
with col4:
    st.markdown("[Language](#language)")

st.markdown("---")

# Main Title
st.markdown("<h1 style='text-align: center; color: #ff5500;'>Soundcloud Downloader To Mp3 Tool</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; margin-top: -20px;'>Download Soundcloud Songs And Music To MP3 On PC And Mobile Quickly</h3>", unsafe_allow_html=True)

# Main Converter Section
with st.container():
    st.subheader("🔗 SoundCloud Track Link")
    url = st.text_input(" ", placeholder="Paste track URL here", label_visibility="collapsed")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🚀 Download MP3 Track", use_container_width=True):
            if url:
                try:
                    with st.spinner('Downloading... This may take a moment'):
                        mp3_path = download_audio(url)
                        
                        with open(mp3_path, "rb") as f:
                            btn = st.download_button(
                                label="💾 Save MP3 File",
                                data=f,
                                file_name=os.path.basename(mp3_path),
                                mime="audio/mpeg",
                                use_container_width=True
                            )
                        
                        os.remove(mp3_path)
                except Exception as e:
                    st.error(f"Error downloading track: {str(e)}")
            else:
                st.warning("Please enter a SoundCloud track URL")

# How To Use Section
st.markdown("---")
st.header("🎯 How to Use Soundcloud Downloader to Convert Soundcloud to MP3?")
steps = """
1. **Copy Soundcloud track link** - Find your desired track on SoundCloud and copy its URL
2. **Paste Soundcloud track link** - Insert the link in the input field above
3. **Save Soundcloud MP3 track** - Click the download button and enjoy offline!
"""
st.markdown(steps)

# Platform Guides
col1, col2 = st.columns(2)
with col1:
    st.subheader("🖥️ PC Instructions")
    st.markdown("""
    - Open SoundCloud in your browser
    - Right-click on track → 'Copy link address'
    - Paste here and click download
    """)

with col2:
    st.subheader("📱 Mobile Instructions")
    st.markdown("""
    - Open SoundCloud app
    - Share → Copy link
    - Paste here and download
    - Save to your device storage
    """)

# FAQ Section
st.markdown("---")
st.header("❓ Soundcloud To Mp3 Downloader FAQ")
with st.expander("What new updates will Soundcloud Downloader inserts this?"):
    st.write("We regularly update our converter to maintain compatibility and add new features")

with st.expander("Is this service free?"):
    st.write("Yes! Our SoundCloud downloader is completely free to use")

with st.expander("Supported formats?"):
    st.write("We currently support MP3 format with 192kbps quality")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <p style='font-size: 0.8em;'>
    **Disclaimer:** This tool is for educational purposes only. 
    Please ensure you have the right to download and use any content.<br>
    © 2023 SoundCloud Downloader Tool. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)

# Hidden Section Anchors
st.markdown("<div id='about-us'></div>", unsafe_allow_html=True)
st.markdown("<div id='blog'></div>", unsafe_allow_html=True)
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.markdown("<div id='language'></div>", unsafe_allow_html=True)
