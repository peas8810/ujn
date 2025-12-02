from pathlib import Path
import streamlit as st

# Configurações básicas da página
st.set_page_config(
    page_title="UJN – Ecossistema de Publicação Científica",
    layout="wide",
    page_icon="📘"
)

# CSS global: fonte Arial, página limpa, sem cara de app pesado
st.markdown("""
<style>
html, body, [class*="stApp"] {
    font-family: Arial, sans-serif !important;
    background-color: #ffffff !important;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1.5rem !important;
    max-width: 1200px !important;
}

/* Remove fundo do sidebar (caso apareça) */
section[data-testid="stSidebar"] {
    background-color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# Lê o HTML que está no mesmo diretório do app.py
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text(encoding="utf-8")

# Injeta o HTML direto na página (sem iframe, sem scroll separado)
st.markdown(html_content, unsafe_allow_html=True)
