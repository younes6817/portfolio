import streamlit as st
# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=300)

with col2:
    st.title("Mostafa")
    content = """
        Hi, I am mostafa ghafari . Iam a Python programmer 
        teacher, and funder of FarviGram.
        I graduated in 2022 from Software engineer,
        I have worked with AI, FPGA, C++, C# and...
        
        
    """
    st.info(content)
