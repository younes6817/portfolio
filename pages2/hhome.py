import streamlit as st
import pandas


st.title("The Best Company")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
col1, col2, col3= st.columns(3)
df = pandas.read_csv("004 data.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row["first name"]} {row['last name']}")
        st.write(row["role"])
        st.image("image004/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row["first name"]} {row['last name']}")
        st.write(row["role"])
        st.image("image004/"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row["first name"]} {row['last name']}")
        st.write(row["role"])
        st.image("image004/"+row["image"])

