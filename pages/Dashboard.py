import streamlit as st
import webbrowser as wb

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.title("DASHBOARD")


if st.button("Heart"):
    wb.open("http://localhost:8501/Heart")


if st.button("kidney"):
    wb.open("http://localhost:8501/kidney")
