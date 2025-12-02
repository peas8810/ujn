from pathlib import Path
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="UJN – Ecossistema de Publicação Científica",
    layout="wide",
    page_icon="📘"
)

# CSS global: fonte Arial, fundo branco, layout mais limpo
st.markdown("""
<style>
/* Fonte geral da página */
html, body, [class*="stApp"] {
    font-family: Arial, sans-serif !important;
    background-color: #ffffff !important;
}

/* Container principal mais "limpo" */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1.5rem !important;
    max-width: 1200px !important;
}

/* Remove fundo cinza de alguns elementos */
section[data-testid="stSidebar"] {
    background-color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# Lê o HTML da landing page
html_path = Path("index.html")
html_content = html_path.read_text(encoding="utf-8")

# Injeta o HTML direto na página (SEM iframe, SEM scroll separado)
st.markdown(html_content, unsafe_allow_html=True)
