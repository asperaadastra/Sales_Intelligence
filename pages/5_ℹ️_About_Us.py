import streamlit as st

def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()



def load_about_page():

    st.title("📌 About Us")
    st.subheader("Apex Sales Intelligence")

    st.write("""
    At **Apex Sales Intelligence**, our mission is to empower grocery stores with smart
    data analytics, real-time insights, and accurate sales forecasting tools.
    
    We believe that modern retail should be **data-driven**, and our platform helps business
    owners make informed decisions effortlessly.
    """)

    st.markdown("---")

    # --- TEAM SECTION ---
    st.header("👥 Meet the Team")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.image("IMG_9515.JPG", caption="Mirzaakbar Siddikov")
        st.write("• ISE Student")

    with col2:
        st.image("photo_2025-11-24 11.53.50 PM.jpeg", caption="Ruziev Ratmir")
        st.write("•IBT Student")

    with col3:
        st.image("photo_2025-11-24 11.53.55 PM.jpeg", caption="Hamrokulov Niyozbek")
        st.write("•IBT Student")
    with col4:
        st.image("photo_2025-11-24 11.53.52 PM.jpeg", caption="Murodullaev Abubakr ")
        st.write("IBT Student")
    with col5:
        st.image("hoto_2025-11-25 12.12.26 AM.jpeg", caption="Podolak Florian")
        st.write("IBT Student")
    with col6:
        st.image("photo_2025-11-24 11.53.57 PM.jpeg", caption="Purev Nomin")
        st.write("•IBT Student")
    
    st.markdown("---")

    # --- CONTACT SECTION ---
    st.header("📞 Contact Us")

    st.write("""
    **Phone:** +82 10-1234-5678  
    **Email:** siddikovmirzoakbar@gmail.com  
    **Address:** 123 Smart Street, Seoul, South Korea
    """)

    st.markdown("### 🗺 Our Location")

    # Google Maps Embed
    google_map_iframe = """
    <iframe 
        width="100%" 
        height="350" 
        frameborder="0" 
        style="border:0"
        src="https://maps.google.com/maps?q=seoul%20south%20korea&t=&z=13&ie=UTF8&iwloc=&output=embed"
        allowfullscreen>
    </iframe>
    """

    st.markdown(google_map_iframe, unsafe_allow_html=True)

    st.markdown("---")

    st.success("Feel free to contact us anytime — we're here to help your business grow!")

# Run page (for Streamlit multipage apps)
load_about_page()
