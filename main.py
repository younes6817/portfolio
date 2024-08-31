import pandas
import streamlit as st
# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("younes/my.jpg", width=300)

with col2:
    st.title("sed Younes")
    content = """
        Hi I am sed younes mousavi
        i was interested in programming which I am getting into
        I am also interested in editing clips and photos
        And I hope to get a job that I like.
        
    """
    st.info(content)

content2 = """
The things I made and know are below
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("story.csv", sep=";")
with col3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("younes/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("younes/"+row["image"])
        st.write(f"[Source Code]({row['url']}]")
