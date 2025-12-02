from pathlib import Path
import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="UJN – Ecossistema de Publicação Científica",
    layout="wide",
    page_icon="📘"
)

# CSS global para deixar a página limpa + Arial
st.markdown("""
<style>
html, body, [class*="stApp"] {
    font-family: Arial, sans-serif !important;
    background-color: #ffffff !important;
    overflow-x: hidden !important;  /* evita scroll horizontal */
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
    max-width: 1000px !important;
    margin: 0 auto !important;
}

/* remove aquele efeito de container de app */
main {
    background-color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# Carrega o HTML diretamente
html_file = Path(__file__).parent / "index.html"
html_content = html_file.read_text(encoding="utf-8")

# Exibe o HTML direto, SEM iframe → SEM scroll lock
st.markdown(html_content, unsafe_allow_html=True)
