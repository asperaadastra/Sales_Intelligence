import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_css_file(file_path="styles/default.css"):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file()

st.title("📊 Sales Dashboard")

if "mapping" not in st.session_state:
    st.warning("Complete column mapping first.")
    st.stop()

mapping = st.session_state["mapping"]
df = st.session_state["raw_df"].copy()

st.markdown('<div class="dashboard-page-pattern">', unsafe_allow_html=True)

df["Revenue"] = df[mapping["qty"]] * df[mapping["price"]]

# Metrics
total_rev = df["Revenue"].sum()
top_item = df.groupby(mapping["item"])["Revenue"].sum().idxmax()

col1, col2 = st.columns(2)
col1.metric("Total Revenue", f"${total_rev:,.2f}")
col2.metric("Best Seller", top_item)

# Top 10
st.subheader("🏅 Top 10 Best-Selling Items")
top10 = df.groupby(mapping["item"])["Revenue"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top10)

# Low Stock
if mapping["stock"]:
    st.subheader("⚠️ Low Stock Items (< 10 units)")
    low = df[df[mapping["stock"]] < 10][[mapping["item"], mapping["stock"]]]
    st.dataframe(low)

# Sales over time
st.subheader("📈 Sales Over Time")
df[mapping["date"]] = pd.to_datetime(df[mapping["date"]])
daily_sales = df.groupby(df[mapping["date"]].dt.date)["Revenue"].sum()
st.line_chart(daily_sales)

# sales by category
st.subheader("🗂 Sales by Category")
cat_sales = df.groupby(mapping["cat"])["Revenue"].sum()
st.bar_chart(cat_sales)
