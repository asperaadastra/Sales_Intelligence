import streamlit as st
import pandas as pd
from PIL import Image

def load_css():
    st.markdown("""
    <style>
    /* ----------------------------- */
    /* GLOBAL LAYOUT & BACKGROUND    */
    /* ----------------------------- */
    body, .stApp {
        background: linear-gradient(135deg, #fef5e7 0%, #fdebd0 100%) !important;
        font-family: "Inter", "Arial", sans-serif !important;
        color: #5d4037 !important;
    }

    /* Main titles with Uzbek style */
    h1 {
        font-weight: 800 !important;
        color: #8b4513 !important;
        background: linear-gradient(135deg, #e67e22, #d35400) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        padding: 10px 0 !important;
        border-bottom: 3px solid #e67e22 !important;
        margin-bottom: 25px !important;
        text-align: center !important;
    }

    /* Containers & Cards */
    .stMarkdown, .stDataFrame, .css-1d391kg, div[data-testid="stHorizontalBlock"] > div {
        background: rgba(255, 255, 255, 0.95) !important;
        padding: 25px !important;
        border-radius: 12px !important;
        border: 2px solid #e67e22 !important;
        box-shadow: 0 4px 15px rgba(230, 126, 34, 0.2) !important;
        margin-bottom: 20px !important;
    }

    /* File uploader styling */
    .stFileUploader > div {
        background: linear-gradient(135deg, #fffaf0 0%, #fef5e7 100%) !important;
        border: 3px dashed #e67e22 !important;
        border-radius: 15px !important;
        padding: 40px !important;
        text-align: center !important;
    }

    .stFileUploader > div:hover {
        border: 3px dashed #d35400 !important;
        background: linear-gradient(135deg, #fef9f3 0%, #fdebd0 100%) !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #e67e22 0%, #d35400 100%) !important;
        color: #fef5e7 !important;
        border-radius: 10px !important;
        padding: 12px 30px !important;
        border: 2px solid #a04000 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #d35400 0%, #a04000 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(211, 84, 0, 0.4) !important;
    }

    /* Success messages */
    .stSuccess {
        background: linear-gradient(135deg, #27ae60, #229954) !important;
        color: white !important;
        border: 2px solid #1e8449 !important;
        border-radius: 10px !important;
        padding: 20px !important;
        text-align: center !important;
    }

    /* Image styling */
    .store-image {
        border: 4px solid #e67e22 !important;
        border-radius: 15px !important;
        box-shadow: 0 8px 25px rgba(230, 126, 34, 0.3) !important;
        margin: 20px 0 !important;
    }

    /* Header banner */
    .store-header {
        background: linear-gradient(135deg, #d35400 0%, #e67e22 100%) !important;
        color: white !important;
        padding: 20px !important;
        border-radius: 15px !important;
        text-align: center !important;
        margin-bottom: 30px !important;
        border: 3px solid #a04000 !important;
    }

    /* Welcome text */
    .welcome-text {
        background: linear-gradient(135deg, #fffaf0 0%, #fef5e7 100%) !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 2px solid #e67e22 !important;
        text-align: center !important;
        font-size: 18px !important;
        color: #5d4037 !important;
        margin-bottom: 25px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Store Header Banner
st.markdown("""
<div class="store-header">
    <h1>🌿 Makro Supermarket - Salamy-Teeki 🌿</h1>
    <h3>Central Asian Groceries in Korea</h3>
</div>
""", unsafe_allow_html=True)

# Welcome Message
st.markdown("""
<div class="welcome-text">
    🏺 Welcome to Makro Analytics Dashboard! 🏺<br>
    Upload your sales data to get insights about your Central Asian products
</div>
""", unsafe_allow_html=True)

# Display Makro Supermarket Image
try:
    # Try to load the image (you'll need to place the image in your project folder)
    image = Image.open('Makro_Supermarket_in_Uzbekistan.jpg')
    st.image(image, caption='Makro Supermarket in Uzbekistan - Our Inspiration 🌟', use_column_width=True, output_format='auto', clamp=True)
except:
    # If image fails to load, show a placeholder with Uzbek style
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e67e22, #d35400); color: white; padding: 60px; text-align: center; border-radius: 15px; border: 3px solid #a04000;">
        <h2>🏪 Makro Supermarket</h2>
        <p style="font-size: 20px;">Salamy-Teeki - Central Asian Groceries</p>
        <p>📍 Image: Makro Supermarket in Uzbekistan</p>
    </div>
    """, unsafe_allow_html=True)

# Original upload functionality
st.title("📁 Upload Sales Data")

uploaded = st.file_uploader("Upload your CSV file with sales data", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.session_state["raw_df"] = df
    st.success("✅ File uploaded successfully!")
    
    st.subheader("📊 Data Preview")
    st.dataframe(df.head())
    
    # Show some basic info with Uzbek styling
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Rows", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        st.metric("File Size", f"{uploaded.size / 1024:.1f} KB")