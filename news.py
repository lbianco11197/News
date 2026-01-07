import streamlit as st
import pandas as pd
import base64 
from pathlib import Path
import requests

# ----------------------------
# Helpers
# ----------------------------
def _read_bytes(path: str) -> bytes | None:
    p = Path(path)
    if not p.exists():
        alt = Path(__file__).parent / path
        if alt.exists():
            p = alt
        else:
            return None
    return p.read_bytes()


def set_page_background(image_path: str = "sfondo.png"):
    data = _read_bytes(image_path)
    if not data:
        return

    encoded = base64.b64encode(data).decode("utf-8")
    css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: url("data:image/png;base64,{encoded}") center/cover no-repeat fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def inject_css():
    css = """
    <style>
    /* Header trasparente */
    [data-testid="stHeader"] {
        background: rgba(255,255,255,0);
    }

    /* Logo iniziale */
    .jj-top-logo {
        display: block;
        max-width: 320px;
        width: 100%;
        height: auto;
        margin: 24px auto 16px auto;
    }

    /* Card centrale */
    .jj-card {
        max-width: 980px;
        margin: 20px auto 30px auto;
        padding: 44px;
        background: rgba(255,255,255,0.94);
        border: 1px solid rgba(210,210,210,0.8);
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    }

    .jj-title {
        font-size: 26px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 18px;
        color: #0b1320;
    }

    .jj-subtitle {
        font-size: 15px;
        text-align: center;
        line-height: 1.5;
        margin-bottom: 28px;
        color: #1f2d3d;
    }

    .jj-text {
        font-size: 16px;
        line-height: 1.65;
        margin-bottom: 16px;
        color: #1f2d3d;
    }

    .jj-strong {
        font-weight: 700;
    }

    /* Footer loghi */
    .jj-footer {
        max-width: 980px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 26px;
        padding: 18px 12px;
        background: rgba(255,255,255,0.94);
        border: 1px solid rgba(210,210,210,0.8);
        border-radius: 14px;
        display: flex;
        justify-content: center;
    }

    .jj-logos {
        max-width: 520px;
        width: 100%;
        height: auto;
    }

    /* Nascondi elementi Streamlit */
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# ----------------------------
# App
# ----------------------------
st.set_page_config(
    page_title="Progetto Formativo – Nuove Competenze 2025",
    layout="wide"
)

set_page_background("sfondo.png")
inject_css()


# ----------------------------
# Logo Euroirte centrato (RIDIMENSIONATO)
# ----------------------------
logo_top = _read_bytes("LogoEuroirte.png")
if logo_top:
    st.markdown(
        '<img src="data:image/png;base64,' +
        base64.b64encode(logo_top).decode() +
        '" class="jj-top-logo">',
        unsafe_allow_html=True
    )


# ----------------------------
# Contenuto centrale (HTML CORRETTO)
# ----------------------------
st.markdown(
    """
    <div class="jj-card">
        <div class="jj-title">PROGETTO FORMATIVO “NUOVE COMPETENZE 2025”</div>

        <div class="jj-subtitle">
            ID-FNC3 – S-08472<br>
            AVVISO MLPS DEL 5/12/2024<br>
            FONDONUOVE COMPETENZE 3 – COMPETENZE PER L’INNOVAZIONE
        </div>

        <p class="jj-text">
            Il progetto formativo è realizzato nell’ambito del
            <span class="jj-strong">Fondo Nuove Competenze – Competenze per le Innovazioni</span>,
            operazione di importanza strategica del
            <span class="jj-strong">Programma Nazionale Giovani, Donne e Lavoro 2021–2027</span>,
            cofinanziato dall’Unione Europea – Fondo Sociale Europeo Plus (FSE+).
        </p>

        <p class="jj-text">
            <span class="jj-strong">Periodo di realizzazione previsto</span>
            – DICEMBRE 2025 – FEBBRAIO 2026
        </p>

        <p class="jj-text">
            <span class="jj-strong">Ambiti formativi</span>
            (es. competenze digitali, sicurezza, innovazione)
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ----------------------------
# Loghi finali centrati
# ----------------------------
logo_footer = _read_bytes("loghi.png")
if logo_footer:
    st.markdown(
        '<div class="jj-footer">'
        '<img src="data:image/png;base64,' +
        base64.b64encode(logo_footer).decode() +
        '" class="jj-logos"></div>',
        unsafe_allow_html=True
    )
else:
    st.warning("Immagine 'loghi.png' non trovata")
