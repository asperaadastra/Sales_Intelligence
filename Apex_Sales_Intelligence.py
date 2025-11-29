import streamlit as st
from PIL import Image
from pathlib import Path

# --------------------- GLOBAL CONFIG --------------------- #

st.set_page_config(
    page_title="Apex Sales Intelligence",
    page_icon="Image1.jpg",
    layout="wide",
)

# --------------------- CSS --------------------- #

def load_css_file(file_path: str = "styles/default.css"):
    css_path = Path(file_path)
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found at: {css_path}")

load_css_file()

# --------------------- SIDEBAR BRANDING --------------------- #

with st.sidebar:
    st.image("Image1.jpg", use_container_width=True)
    st.markdown(
        """
        <div class="sidebar-brand-title">Apex Sales Intelligence</div>
        <div class="sidebar-brand-subtitle">Peak Performance Analytics</div>
        <hr class="sidebar-separator" />
        """,
        unsafe_allow_html=True,
    )

# --------------------- HEADER APEX --------------------- #

logo = Image.open("Image1.jpg")

header_col1, header_col2 = st.columns([1, 4])

with header_col1:
    st.image(logo, width=70)

with header_col2:
    st.markdown(
        """
        ### Apex Sales Intelligence  
        Peak Performance Dashboard
        """
    )

st.write("")

# --------------------- LOGIN --------------------- #

st.title("🛒 Grocery Sales Dashboard - Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Connexion button
login_btn = st.button("Login", key="login_btn", use_container_width=False)

