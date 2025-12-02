import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="UJN – Ecossistema de Publicação Científica",
    layout="wide",
    page_icon="📘"
)

# Caminho da pasta onde está o app.py
APP_DIR = Path(__file__).parent

# Caminho completo para o index.html na MESMA pasta do app.py
html_file = APP_DIR / "index.html"

# Lê o conteúdo do HTML
html_content = html_file.read_text(encoding="utf-8")

# Mostra o HTML no Streamlit
st.components.v1.html(html_content, height=3000, scrolling=True)
