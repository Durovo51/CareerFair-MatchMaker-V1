import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Booth Matchmaker", page_icon="🎯", layout="wide")


# ---------- Header ----------
st.title("Booth Matchmaker")
st.write(
    "Get a ranked list of employer booths worth your time at the career fair, "
    "plus talking points tailored to your background."
)



# ---------- Placeholder matching logic ----------
