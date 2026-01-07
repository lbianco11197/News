import streamlit as st
import base64
from pathlib import Path


def read_bytes(filename: str) -> bytes | None:
    p = Path(__file__).parent / filename
    return p.read_bytes() if p.exists() else None


def set_background_and_global_css(bg_name: str = "sfondo.png"):
    bg = read_bytes(bg_name)
    bg_css = ""
    if bg:
        b64 = base64.b64encode(bg).decode("utf-8")
        bg_css = f"""
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{b64}") center/cover no-repeat fixed;
        }}
        """

    st.markdown(
        f"""
        <style>
        {bg_css}

        [data-testid="stHeader"] {{ background: rgba(255,255,255,0); }}
        #MainMenu {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}

        /* Contenitore centrale */
        .block-container {{
            max-width: 980px !important;
            padding-top: 16px !important;
            padding-bottom: 30px !important;
        }}

        /* Centra TUTTO il contenuto */
        [data-testid="stAppViewContainer"] .block-container {{
            text-align: center;
        }}

        /* Titolo grande */
        h1 {{
            font-size: 44px !important;
            font-weight: 800 !important;
            line-height: 1.15 !important;
            margin-bottom: 14px !important;
        }}

        /* Testo più grande (tutti i markdown/paragrafi) */
        .stMarkdown, .stMarkdown p, .stMarkdown li {{
            font-size: 22px !important;
            line-height: 1.7 !important;
        }}

        /* Blocco "evidenziato" (ID/Avviso/Fondo) un filo più grande */
        .highlight-block {{
            font-size: 24px !important;
            font-weight: 700 !important;
            line-height: 1.6 !important;
            margin: 10px 0 16px 0;
        }}

        /* Logo top */
        .top-logo {{
            display: block;
            margin: 10px auto 14px auto;
            width: 360px;
            max-width: 85vw;
            height: auto;
        }}

        /* Loghi finali */
        .bottom-logos {{
            display: block;
            margin: 18px auto 0 auto;
            width: 560px;
            max-width: 90vw;
            height: auto;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


st.set_page_config(page_title="Progetto Formativo – Nuove Competenze 2025", layout="wide")
set_background_and_global_css("sfondo.png")


# --- Logo Euroirte (centrato, ridimensionato) ---
top_logo = read_bytes("LogoEuroirte.png")
if top_logo:
    st.markdown(
        f'<img class="top-logo" src="data:image/png;base64,{base64.b64encode(top_logo).decode()}">',
        unsafe_allow_html=True
    )
else:
    st.warning("Manca LogoEuroirte.png")


# --- Titolo ---
st.title('PROGETTO FORMATIVO “NUOVE COMPETENZE 2025”')


# --- Blocco evidenziato (NO HTML nel contenuto) ---
st.markdown(
    """
<div class="highlight-block">
ID-FNC3 – S-08472  
AVVISO MLPS DEL 5/12/2024  
FONDONUOVE COMPETENZE 3 – COMPETENZE PER L’INNOVAZIONE
</div>
""",
    unsafe_allow_html=True
)

# --- Testo descrittivo (solo Markdown) ---
st.markdown(
    "Il progetto formativo è realizzato nell’ambito del **Fondo Nuove Competenze – Competenze per le Innovazioni**, "
    "operazione di importanza strategica del **Programma Nazionale Giovani, Donne e Lavoro 2021–2027**, "
    "cofinanziato dall’Unione Europea – Fondo Sociale Europeo Plus (FSE+)."
)

st.markdown("**Periodo di realizzazione previsto** – DICEMBRE 2025 – FEBBRAIO 2026")
st.markdown("**Ambiti formativi** (es. competenze digitali, sicurezza, innovazione)")


# --- Loghi finali (centrati) ---
bottom = read_bytes("loghi.png")
if bottom:
    st.markdown(
        f'<img class="bottom-logos" src="data:image/png;base64,{base64.b64encode(bottom).decode()}">',
        unsafe_allow_html=True
    )
else:
    st.warning("Manca loghi.png")
