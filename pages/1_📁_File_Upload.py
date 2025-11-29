import streamlit as st
import pandas as pd
from PIL import Image

def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

# Display Makro Supermarket Image
try:
    # Try to load the image
    image = Image.open('Makro_Supermarket_in_Uzbekistan.jpg')
    st.image(image, caption='Makro Supermarket in Uzbekistan - Our Inspiration 🌟', use_column_width=True)
except:
    # If image fails to load, show a placeholder
    st.markdown("""
    <div style="background: #e67e22; color: white; padding: 60px; text-align: center; border-radius: 15px;">
        <h1>🏪 Makro Supermarket</h1>
        <p style="font-size: 20px;">Salamy-Teeki - Central Asian Groceries</p>
        <p>📍 Image: Makro Supermarket in Uzbekistan</p>
    </div>
    """, unsafe_allow_html=True)

# Original upload functionality
st.title("📁 Upload Sales Data")

uploaded = st.file_uploader("Upload your CSV file", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.session_state["raw_df"] = df
    st.success("File uploaded!")

    st.dataframe(df.head())