import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from chatbot_utils import render_chatbot_for_df

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

# Revenue calculus
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

# Sales by category
st.subheader("🗂 Sales by Category")
cat_sales = df.groupby(mapping["cat"])["Revenue"].sum()
st.bar_chart(cat_sales)

# ---------- 🔽 CHATBOT ZONE BASED ON THE VISIBLE DATA 🔽 ----------

# DataFrame for the chatbot
chat_columns = [
    mapping["item"],
    mapping["cat"],
    mapping["date"],
    mapping["qty"],
    mapping["price"],
]

if mapping["stock"]:
    chat_columns.append(mapping["stock"])

chat_df = df[chat_columns].copy()
chat_df["Revenue"] = df["Revenue"]

# Opening state of the chatbot
if "show_chatbot_dashboard" not in st.session_state:
    st.session_state["show_chatbot_dashboard"] = False

# Button
st.markdown('<div class="chat-fab-wrapper">', unsafe_allow_html=True)
if st.button("🤖", key="chat_fab_dashboard"):
    st.session_state["show_chatbot_dashboard"] = not st.session_state["show_chatbot_dashboard"]
st.markdown("</div>", unsafe_allow_html=True)

# Chat pannel
if st.session_state["show_chatbot_dashboard"]:
    st.markdown('<div class="chat-panel">', unsafe_allow_html=True)
    st.caption("Assistant IA basé sur les données du dashboard.")
    render_chatbot_for_df(chat_df, state_key="sales_dashboard")
    st.markdown("</div>", unsafe_allow_html=True)
