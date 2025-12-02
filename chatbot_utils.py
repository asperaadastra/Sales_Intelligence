# chatbot_utils.py
import os
import pandas as pd
import streamlit as st
from openai import OpenAI



client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def _build_data_context(data: pd.DataFrame, max_rows: int = 80) -> str:
    if len(data) > max_rows:
        data = data.head(max_rows)
    return data.to_csv(index=False)


def _ask_sales_bot(question: str, data: pd.DataFrame) -> str:
    """
    Calls the OpenAI model with sales data context.
    The model is encouraged to analyze, aggregate and infer answers.
    """

    # Convert data to compact CSV
    data_text = _build_data_context(data)
    cols = ", ".join(list(data.columns))

    system_prompt = (
        "You are a data analysis assistant specialized in sales performance.\n"
        "You will receive a dataset extracted from a sales dashboard (CSV format).\n"
        f"The available columns are: {cols}.\n\n"
        "Your objectives:\n"
        "- Use the dataset to calculate insights such as revenue ranking, best-selling product,\n"
        "  category performance, stock shortage, sales trends, etc.\n"
        "- You MUST attempt to answer questions using the provided CSV dataset,\n"
        "  even if it requires grouping, summing, filtering, or comparing values.\n"
        "- Respond naturally and clearly in English, unless the user speaks another language.\n"
        "- You may perform calculations based on columns like Quantity, Price, Revenue or Date.\n"
        "- You are NOT allowed to invent or guess information not inferable from the dataset.\n"
        "- Only answer 'I don't know.' when the question clearly cannot be answered using the data\n"
        "  (e.g. marketing budget, CEO name, external strategy, information not inside the table).\n\n"
        "Here is the dataset (CSV format):\n"
        f"{data_text}"
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0.1,
    )

    return completion.choices[0].message.content



def render_chatbot_for_df(df: pd.DataFrame, state_key: str = "sales_dashboard_chat"):
    st.subheader("💬 AI Sales Assistant")

    history_key = f"{state_key}_history"
    if history_key not in st.session_state:
        st.session_state[history_key] = []

    for msg in st.session_state[history_key]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    question = st.chat_input("Ask a question on the sales...")
    if question:
        st.session_state[history_key].append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Data analyses..."):
                try:
                    answer = _ask_sales_bot(question, df)
                except Exception as e:
                    answer = f"Erreur lors de l'appel à l'API : {e}"
                st.markdown(answer)

        st.session_state[history_key].append({"role": "assistant", "content": answer})
