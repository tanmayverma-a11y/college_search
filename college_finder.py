import streamlit as st
import pandas as pd

# Upload CSV file
st.title("College Finder")


df = pd.read_csv(r"c:\Users\tanma\Downloads\data-1755675404346 (1).csv")



    # Select column to search
column = st.selectbox("Select column to search", df.columns)

    # Search query
query = st.text_input(f"Search by {column}")

if query:
    results = df[df[column].astype(str).str.contains(query, case=False, na=False)]
    st.write(f"Found {len(results)} matches")
    st.dataframe(results)


    # Preview table
st.subheader("Complete List of Colleges")
st.dataframe(df)
