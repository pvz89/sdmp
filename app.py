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

# Legal Pages Content
st.markdown("---")
st.markdown("<div id='dmca'></div>", unsafe_allow_html=True)
st.header("📜 DMCA Compliance")
st.markdown("""
**Digital Millennium Copyright Act (DMCA) Notice**

We respect intellectual property rights and comply with the DMCA. 
If you believe your copyrighted work is being infringed:

1. Submit a written notice containing:
   - Identification of the copyrighted work
   - URL of allegedly infringing content
   - Your contact information
   - Statement of good faith belief
   - Verification under penalty of perjury

2. Send to our designated agent:
   Email: dmca@example.com  
   Address: 123 Copyright Lane, Digital City

We will respond to valid notices within 5 business days.
""")

st.markdown("---")
st.markdown("<div id='disclaimer'></div>", unsafe_allow_html=True)
st.header("⚠️ Legal Disclaimer")
st.markdown("""
**Important Notice:**

1. This tool is provided for **educational purposes only**
2. Users are solely responsible for verifying copyright status
3. We do not host or store any copyrighted content
4. Downloading unauthorized content may violate copyright laws
5. We reserve the right to refuse service to any user

By using this service, you agree to these terms and assume all liability.
""")

st.markdown("---")
st.markdown("<div id='t&amp;c'></div>", unsafe_allow_html=True)
st.header("📑 Terms & Conditions")
st.markdown("""
**Service Agreement:**

1. Users must be 13+ years old
2. Maximum 10 downloads per day
3. No commercial use allowed
4. We reserve right to modify terms without notice
5. Service provided "as-is" without warranties

Violation of terms may result in IP ban and legal action.
""")

st.markdown("---")
st.markdown("<div id='privacy-policy'></div>", unsafe_allow_html=True)
st.header("🔒 Privacy Policy")
st.markdown("""
**Data Handling:**

1. We do not collect personal information
2. Downloaded files are immediately deleted
3. We use cookies for basic analytics
4. Third-party links have separate policies
5. Data retention: No user data stored

We never share or sell any user information.
""")

# About & Contact Sections
st.markdown("---")
st.markdown("<div id='about-us'></div>", unsafe_allow_html=True)
st.header("👥 About Us")
st.markdown("""
**Our Mission:**

- Provide accessible audio tools
- Promote ethical content use
- Support independent creators
- Innovate in digital media conversion

Founded in 2023 by audio technology enthusiasts.
""")

st.markdown("---")
st.markdown("<div id='contact'></div>", unsafe_allow_html=True)
st.header("📩 Contact Us")
st.markdown("""
**Get in Touch:**

- Support: support@example.com
- Partnerships: partners@example.com
- Office: 456 Tech Street, Digital City
- Hours: Mon-Fri 9AM-5PM (GMT)

We respond within 24 hours.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; margin-bottom: 20px;'>
    <a href="#dmca" style="color: #ff5500; text-decoration: none; margin: 0 10px;">DMCA</a> •
    <a href="#disclaimer" style="color: #ff5500; text-decoration: none; margin: 0 10px;">Disclaimer</a> •
    <a href="#t&amp;c" style="color: #ff5500; text-decoration: none; margin: 0 10px;">T&C</a> •
    <a href="#about-us" style="color: #ff5500; text-decoration: none; margin: 0 10px;">About Us</a> •
    <a href="#contact" style="color: #ff5500; text-decoration: none; margin: 0 10px;">Contact Us</a> •
    <a href="#privacy-policy" style="color: #ff5500; text-decoration: none; margin: 0 10px;">Privacy Policy</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center;'>
    <p style='font-size: 0.8em;'>
    **Disclaimer:** This tool is for educational purposes only. 
    Please ensure you have the right to download and use any content.<br>
    © 2023 SoundCloud Downloader Tool. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)
