import streamlit as st
import pandas as pd

def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

st.title("🔧 Column Mapping")

if "raw_df" not in st.session_state:
    st.warning("Upload a CSV first.")
    st.stop()

df = st.session_state["raw_df"]

columns = df.columns.tolist()

st.write("Match your CSV columns to app fields:")

date_col = st.selectbox("Date column:", columns)
item_col = st.selectbox("Item name column:", columns)
qty_col = st.selectbox("Quantity column:", columns)
price_col = st.selectbox("Unit price column:", columns)
category_col = st.selectbox("Category column:", columns)
stock_col = st.selectbox("Stock column (optional):", ["None"] + columns)

if st.button("Save Mapping"):
    st.session_state["mapping"] = {
        "date": date_col,
        "item": item_col,
        "qty": qty_col,
        "price": price_col,
        "cat": category_col,
        "stock": None if stock_col == "None" else stock_col
    }
    st.success("Mapping saved!")
