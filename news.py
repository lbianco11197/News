import streamlit as st
import base64
from pathlib import Path


# ----------------------------
# Utils
# ----------------------------
def read_bytes(filename: str) -> bytes | None:
    p = Path(__file__).parent / filename
    return p.read_bytes() if p.exists() else None


def set_background(image_path: str = "sfondo.png"):
    data = read_bytes(image_path)
    if not data:
        return
    b64 = base64.b64encode(data).decode("utf-8")
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{b64}") center/cover no-repeat fixed;
        }}
        [data-testid="stHeader"] {{ background: rgba(255,255,255,0); }}
        #MainMenu {{ visibility: hidden; }}
        footer {{ visibility: hidden; }}

        /* Contenitore centrale */
        .center-box {{
            max-width: 1100px;
            margin: 0 auto;
            text-align: center;
        }}

        /* Testi grandi */
        .big-text {{
            font-size: 20px;
            line-height: 1.7;
        }}

        .very-big {{
            font-size: 22px;
            font-weight: 700;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# ----------------------------
# App
# ----------------------------
st.set_page_config(
    page_title="Progetto Formativo – Nuove Competenze 2025",
    layout="wide"
)

set_background("sfondo.png")

# ----------------------------
# LOGO IN ALTO (centrato)
# ----------------------------
logo_top = read_bytes("LogoEuroirte.png")
if logo_top:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image(logo_top, width=380)

st.write("")

# ----------------------------
# CONTENUTO CENTRALE
# ----------------------------
st.markdown('<div class="center-box">', unsafe_allow_html=True)

st.markdown(
    "<h1>PROGETTO FORMATIVO “NUOVE COMPETENZE 2025”</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="very-big">
ID-FNC3 – S-08472<br>
AVVISO MLPS DEL 5/12/2024<br>
FONDONUOVE COMPETENZE 3 – COMPETENZE PER L’INNOVAZIONE
</div>
""",
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
<div class="big-text">
Il progetto formativo è realizzato nell’ambito del <b>Fondo Nuove Competenze – Competenze per le Innovazioni</b>,
operazione di importanza strategica del
<b>Programma Nazionale Giovani, Donne e Lavoro 2021–2027</b>,
cofinanziato dall’Unione Europea – Fondo Sociale Europeo Plus (FSE+).
</div>
""",
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    """
<div class="big-text">
<b>Periodo di realizzazione previsto</b> – DICEMBRE 2025 – FEBBRAIO 2026
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="big-text">
<b>Ambiti formativi</b> (es. competenze digitali, sicurezza, innovazione)
</div>
""",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ----------------------------
# LOGHI FINALI (centrati)
# ----------------------------
logos = read_bytes("loghi.png")
if logos:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image(logos, width=600)
