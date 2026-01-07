import streamlit as st
import base64
from pathlib import Path


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
          [data-testid="stHeader"] {{
            background: rgba(255,255,255,0);
          }}
          #MainMenu {{visibility: hidden;}}
          footer {{visibility: hidden;}}

          /* “Card” semplice per testo */
          .card {{
            max-width: 980px;
            margin: 0 auto;
            padding: 36px 40px;
            background: rgba(255,255,255,0.94);
            border: 1px solid rgba(210,210,210,0.85);
            border-radius: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
          }}
        </style>
        """,
        unsafe_allow_html=True
    )


st.set_page_config(page_title="Progetto Formativo – Nuove Competenze 2025", layout="wide")
set_background("sfondo.png")


# ----------------------------
# LOGO IN ALTO (centrato + ridimensionato SICURO)
# ----------------------------
top_logo = read_bytes("LogoEuroirte.png")
if top_logo:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image(top_logo, width=420)  # <-- cambia qui se lo vuoi più piccolo (es. 320)
else:
    st.warning("File mancante: LogoEuroirte.png")

st.write("")  # piccolo spazio


# ----------------------------
# TESTO (sempre visibile, no HTML)
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.title('PROGETTO FORMATIVO “NUOVE COMPETENZE 2025”')

st.markdown(
    """
**ID-FNC3 – S-08472**  
**AVVISO MLPS DEL 5/12/2024**  
**FONDONUOVE COMPETENZE 3 – COMPETENZE PER L’INNOVAZIONE**
"""
)

st.markdown(
    """
Il progetto formativo è realizzato nell’ambito del **Fondo Nuove Competenze – Competenze per le Innovazioni**,
operazione di importanza strategica del **Programma Nazionale Giovani, Donne e Lavoro 2021–2027**,
cofinanziato dall’Unione Europea – Fondo Sociale Europeo Plus (FSE+).
"""
)

st.markdown("**Periodo di realizzazione previsto** – DICEMBRE 2025 – FEBBRAIO 2026")
st.markdown("**Ambiti formativi** (es. competenze digitali, sicurezza, innovazione )")

st.markdown("</div>", unsafe_allow_html=True)


st.write("")  # spazio


# ----------------------------
# LOGHI A FINE PAGINA (centrati + ridimensionati SICURO)
# ----------------------------
footer_logos = read_bytes("loghi.png")
if footer_logos:
    c1, c2, c3 = st.columns([1, 3, 1])
    with c2:
        st.image(footer_logos, width=560)  # <-- cambia qui (es. 520 / 480) per più piccolo
else:
    st.warning("File mancante: loghi.png")
