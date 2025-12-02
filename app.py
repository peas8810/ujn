import streamlit as st
import pathlib

# Configurações da página
st.set_page_config(
    page_title="UJN – Ecossistema de Publicação Científica",
    layout="wide",
    page_icon="📘"
)

# Caminho do arquivo HTML
html_path = pathlib.Path("index.html").read_text(encoding="utf-8")

# Exibir o HTML na página
st.components.v1.html(html_path, height=3000, scrolling=True)
