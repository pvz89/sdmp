# ... [Keep all previous imports and backend code] ...

# ========== Footer Pages Content ==========
def show_legal_pages():
    st.markdown("---")
    
    # DMCA Page
    with st.expander("DMCA Copyright Policy", expanded=False):
        st.markdown("""
        **soundcloudtomp3.pro DMCA Takedown Policy**

        We respect intellectual property rights and comply with the Digital Millennium Copyright Act (DMCA). 
        To file a copyright infringement notification:
        
        1. Provide your contact information
        2. Identify the copyrighted work
        3. Include the URL of allegedly infringing content
        4. State your good faith belief of unauthorized use
        5. Include a statement under penalty of perjury
        
        Send notices to: dmca@soundcloudtomp3.pro  
        Counter-notices must include similar information.
        """)
    
    # Privacy Policy
    with st.expander("Privacy Policy", expanded=False):
        st.markdown("""
        **soundcloudtomp3.pro Privacy Commitment**
        
        We collect minimal data necessary for service operation:
        
        - URLs submitted for conversion
        - Temporary system logs (deleted after 24 hours)
        - No personal information stored
        
        We use cookies only for essential functionality. We never sell data or share with third parties.
        """)
    
    # Terms & Conditions
    with st.expander("Terms & Conditions", expanded=False):
        st.markdown("""
        **soundcloudtomp3.pro Service Terms**
        
        By using our service, you agree:
        
        - You have rights to convert/download content
        - Maximum 10 conversions per day per user
        - No commercial use allowed
        - We may terminate abusive accounts
        - Service provided "as-is" without warranties
        
        Prohibited activities include reverse engineering, automated scraping, and redistribution of converted content.
        """)
    
    # About Us
    with st.expander("About Us", expanded=False):
        st.markdown("""
        **About soundcloudtomp3.pro**
        
        Established in 2023, we provide temporary audio conversion services for:
        
        - Personal backup purposes
        - Content creators with original works
        - Educational use cases
        
        Our mission is to enable fair use of audio content while respecting creators' rights.
        """)
    
    # Contact Us
    with st.expander("Contact Us", expanded=False):
        st.markdown("""
        **soundcloudtomp3.pro Support Channels**
        
        For general inquiries: support@soundcloudtomp3.pro  
        Technical issues: tech@soundcloudtomp3.pro  
        Legal matters: legal@soundcloudtomp3.pro  
        
        Office Address:  
        SoundCloudToMP3 Ltd.  
        Digital Media Hub,  
        Tech Valley, CA 94016  
        (Virtual office - no physical visits)
        """)

# ========== Updated Footer Section ==========
def main_footer():
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <div style='display: inline-block; margin: 0 10px;'>
            <a href='#dmca' style='text-decoration: none; color: #666;'>DMCA</a> | 
            <a href='#privacy' style='text-decoration: none; color: #666;'>Privacy Policy</a> | 
            <a href='#terms' style='text-decoration: none; color: #666;'>T&C</a> | 
            <a href='#about' style='text-decoration: none; color: #666;'>About Us</a> | 
            <a href='#contact' style='text-decoration: none; color: #666;'>Contact</a>
        </div>
        <p style='font-size: 0.8em; margin-top: 20px;'>
        © 2023 soundcloudtomp3.pro - All rights reserved<br>
        Disclaimer: Third-party service for temporary conversions. Not affiliated with SoundCloud.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hidden anchors for footer links
    st.markdown("<div id='dmca'></div>", unsafe_allow_html=True)
    st.markdown("<div id='privacy'></div>", unsafe_allow_html=True)
    st.markdown("<div id='terms'></div>", unsafe_allow_html=True)
    st.markdown("<div id='about'></div>", unsafe_allow_html=True)
    st.markdown("<div id='contact'></div>", unsafe_allow_html=True)

# ========== Main App Flow ==========
# ... [Keep previous header and main content] ...

# Show legal pages at bottom
show_legal_pages()

# Display footer
main_footer()
