import streamlit as st
import pandas as pd
import base64

def set_background_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        /* Make content containers semi-transparent */
        .stMarkdown, .stDataFrame, .css-1d391kg, .stPlotlyChart, 
        div[data-testid="stHorizontalBlock"] > div,
        [data-testid="metric-container"] {{
            background: rgba(255, 255, 255, 0.92) !important;
            backdrop-filter: blur(5px) !important;
        }}
        
        .stFileUploader > div {{
            background: rgba(248, 253, 255, 0.85) !important;
            backdrop-filter: blur(3px) !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="upload-page-pattern">', unsafe_allow_html=True)

# Set background for this page
set_background_image("ark_bukhara-e1690445501430.jpg")

# Load your main CSS
def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

# Your page content
st.title("📁 Upload Sales Data")
uploaded = st.file_uploader("Upload your CSV file", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.session_state["raw_df"] = df
    st.success("File uploaded!")
    st.dataframe(df.head())