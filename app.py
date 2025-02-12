# Main Converter Section
with st.container():  # Line 53
    # Properly indented content inside the 'with' block
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
    # Line 57 would be here
    st.markdown("---")  # This should be properly aligned under the container
