import streamlit as st
import base64
from pathlib import Path


def read_bytes(filename: str) -> bytes | None:
    p = Path(__file__).parent / filename
    return p.read_bytes() if p.exists() else None


def set_background_and_css(bg_name: str = "sfondo.png"):
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

        [data-testid="stHeader"] {{
            background: rgba(255,255,255,0);
        }}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}

        /* Contenitore centrale: centra TUTTO e limita la larghezza */
        .block-container {{
            max-width: 980px !important;
            padding-top: 18px !important;
            padding-bottom: 30px !important;
        }}

        /* Centra i blocchi principali */
        .center {{
            text-align: center;
        }}

        /* Titolo più grande e centrato */
        .title {{
            font-size: 42px;
            font-weight: 800;
            line-height: 1.15;
            margin: 12px 0 18px 0;
        }}

        /* Testo evidenziato (ID / Avviso / Fondo) più grande */
        .highlight {{
            font-size: 22px;
            font-weight: 700;
            line-height: 1.55;
            margin: 0 0 18px 0;
        }}

        /* Testo descrittivo più grande */
        .bodytext {{
            font-size: 20px;
            line-height: 1.75;
            margin: 0 0 14px 0;
        }}

        /* Logo top controllato */
        .top-logo {{
            display: block;
            margin: 10px auto 10px auto;
            width: 360px;           /* cambia qui se lo vuoi più piccolo */
            max-width: 85vw;
            height: auto;
        }}

        /* Loghi finali controllati */
        .bottom-logos {{
            display: block;
            margin: 18px auto 0 auto;
            width: 560px;          /* cambia qui se li vuoi più piccoli */
            max-width: 90vw;
            height: auto;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


st.set_page_config(page_title="Progetto Formativo – Nuove Competenze 2025", layout="wide")
set_background_and_css("sfondo.png")


# --- Logo Euroirte (centrato, dimensione controllata via CSS) ---
top_logo = read_bytes("LogoEuroirte.png")
if top_logo:
    st.markdown(
        '<div class="center">'
        f'<img class="top-logo" src="data:image/png;base64,{base64.b64encode(top_logo).decode()}">'
        '</div>',
        unsafe_allow_html=True
    )
else:
    st.warning("Manca LogoEuroirte.png")


# --- Contenuto centrato + font grandi ---
st.markdown(
    """
    <div class="center">
        <div class="title">PROGETTO FORMATIVO “NUOVE COMPETENZE 2025”</div>

        <div class="highlight">
            ID-FNC3 – S-08472<br>
            AVVISO MLPS DEL 5/12/2024<br>
            FONDONUOVE COMPETENZE 3 – COMPETENZE PER L’INNOVAZIONE
        </div>

        <div class="bodytext">
            Il progetto formativo è realizzato nell’ambito del
            <b>Fondo Nuove Competenze – Competenze per le Innovazioni</b>,
            operazione di importanza strategica del
            <b>Programma Nazionale Giovani, Donne e Lavoro 2021–2027</b>,
            cofinanziato dall’Unione Europea – Fondo Sociale Europeo Plus (FSE+).
        </div>

        <div class="bodytext">
            <b>Periodo di realizzazione previsto</b> – DICEMBRE 2025 – FEBBRAIO 2026
        </div>

        <div class="bodytext">
            <b>Ambiti formativi</b> (es. competenze digitali, sicurezza, innovazione)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --- Loghi finali centrati ---
bottom = read_bytes("loghi.png")
if bottom:
    st.markdown(
        '<div class="center">'
        f'<img class="bottom-logos" src="data:image/png;base64,{base64.b64encode(bottom).decode()}">'
        '</div>',
        unsafe_allow_html=True
    )
else:
    st.warning("Manca loghi.png")
