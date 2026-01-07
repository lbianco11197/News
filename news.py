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
    """
    Se esiste sfondo.png lo usa come background full-screen.
    Altrimenti usa un background chiaro (gradiente).
    """
    data = _read_bytes(image_path)

    if data:
        encoded = base64.b64encode(data).decode("utf-8")
        bg_css = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{encoded}") center/cover no-repeat fixed;
        }}
        </style>
        """
    else:
        # fallback: gradiente chiaro
        bg_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background: radial-gradient(circle at 20% 10%, rgba(225,235,255,0.9), rgba(244,246,248,1) 35%, rgba(244,246,248,1));
        }
        </style>
        """

    st.markdown(bg_css, unsafe_allow_html=True)


def inject_css():
    css = """
    <style>
      /* Header trasparente */
      [data-testid="stHeader"] {
        background: rgba(255,255,255,0) !important;
      }

      /* Contenitore centrale */
      .jj-card {
        max-width: 980px;
        margin: 64px auto 28px auto;
        padding: 44px 44px 36px 44px;
        background: rgba(255,255,255,0.90);
        border: 1px solid rgba(210,210,210,0.8);
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
      }

      .jj-title {
        font-size: 28px;
        font-weight: 800;
        text-align: center;
        margin: 0 0 18px 0;
        color: #0b1320;
      }

      .jj-subtitle {
        font-size: 16px;
        text-align: center;
        margin: 0 0 26px 0;
        color: #1f2d3d;
        line-height: 1.45;
      }

      .jj-text {
        font-size: 16px;
        color: #1f2d3d;
        line-height: 1.65;
        margin: 0 0 16px 0;
        text-align: left;
      }

      .jj-strong {
        font-weight: 700;
      }

      /* Footer loghi */
      .jj-footer {
        max-width: 980px;
        margin: 0 auto 26px auto;
        padding: 16px 12px;
        background: rgba(255,255,255,0.90);
        border: 1px solid rgba(210,210,210,0.8);
        border-radius: 14px;
        text-align: center;
      }

      /* Nascondi footer Streamlit */
      footer {visibility: hidden;}
      #MainMenu {visibility: hidden;}
    </style>

    .jj-footer {
    max-width: 980px;
    margin: 0 auto 26px auto;
    padding: 18px 12px;
    background: rgba(255,255,255,0.90);
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
    """
    st.markdown(css, unsafe_allow_html=True)


# ----------------------------
# App
# ----------------------------
st.set_page_config(
    page_title="Progetto Formativo – Nuove Competenze 2025",
    layout="wide"
)

set_page_background("sfondo.png")  # opzionale: se non c'è, usa fallback chiaro
inject_css()

# Contenuto (card centrale)
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
        <span class="jj-strong">Periodo di realizzazione previsto</span> – DICEMBRE 2025 – FEBBRAIO 2026
      </p>

      <p class="jj-text">
        <span class="jj-strong">Ambiti formativi</span> (es. competenze digitali, sicurezza, innovazione)
      </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Loghi a fine pagina
logo_bytes = _read_bytes("loghi.png")

if logo_bytes:
    st.markdown(
        '<div class="jj-footer">'
        '<img src="data:image/png;base64,' +
        base64.b64encode(logo_bytes).decode() +
        '" class="jj-logos"></div>',
        unsafe_allow_html=True
    )
else:
    st.warning("Immagine loghi non trovata: salva 'loghi.png' nella stessa cartella del file .py")

