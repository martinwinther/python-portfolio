import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Martin Winther")
    bio = """
    Hi, I'm Martin. A software engineer based in Aarhus, Denmark. I'm passionate about building cool stuff.
    I'm currently working on a project to build a web-based dashboard to monitor the performance of my company's
    production systems. I'm also interested in learning new technologies and exploring new ways to build software.
    Feel free to reach out to me if you have any questions or want to collaborate.
    
    """
    st.info(bio)

content = """
Below you can find a list of my projects that I have built in Python
"""
st.write(content)

col3, col_empty, col4 = st.columns([1.5, 0.5, 1.5])

data = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
