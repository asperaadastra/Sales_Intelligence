import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

st.title("🤖 Sales Prediction")

if "mapping" not in st.session_state:
    st.warning("Complete column mapping first.")
    st.stop()

mapping = st.session_state["mapping"]
df = st.session_state["raw_df"].copy()

df["Revenue"] = df[mapping["qty"]] * df[mapping["price"]]

# Prepare features
df["Day"] = pd.to_datetime(df[mapping["date"]]).dt.dayofweek
df["Month"] = pd.to_datetime(df[mapping["date"]]).dt.month

X = df[["Day", "Month"]]
y = df["Revenue"]

model = RandomForestRegressor().fit(X, y)

day = st.slider("Day of Week (0–6)", 0, 6)
month = st.slider("Month (1–12)", 1, 12)

pred = model.predict([[day, month]])[0]

st.write(f"### Predicted Sales for Day {day}, Month {month}: **${pred:,.2f}**")
