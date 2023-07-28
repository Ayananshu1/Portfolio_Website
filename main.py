import streamlit as st
st.set_page_config(layout="wide")
col1 , col2 = st.columns(2)
with col1:
    st.image("IMG_20230130_180617.jpg")
with col2:
    st.title("Ayananshu Mahapatra")
    content = '''Hey all, this is Ayananshu Mahapatra.This is a portfolio website of my own where I will showcase my projects.
    I am a new bie into the software industry and am interested in learning and building projects in python.
    '''
    st.info(content)

st.text("Below are some of the projects I have built in python.You can have a look at these if you wish to.")


