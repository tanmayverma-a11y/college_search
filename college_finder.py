import streamlit as st
import pandas as pd

st.title("College Finder")

df = pd.read_csv("data.csv")

# --- Select column to search ---
# Force "College Name" to be the default if it exists, otherwise fallback to first column
default_index = df.columns.get_loc("College Name") if "College Name" in df.columns else 0
column = st.selectbox("Select column to search", df.columns, index=default_index)

# --- Search query ---
query = st.text_input(f"Search by {column}")

if query:
    results = df[df[column].astype(str).str.contains(query, case=False, na=False)]
    st.write(f"Found {len(results)} matches")
    st.dataframe(results)

# --- Preview table ---
st.subheader("Complete List of Colleges")
st.dataframe(df)
