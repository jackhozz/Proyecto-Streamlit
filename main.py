import streamlit as st

import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Mi Hamburguesita", page_icon="❤️")

st.markdown(
    """
    <style>
    .big-font {
        font-size: 40px !important;
        text-align: center;
        color: #FF69B4; /* Rosa fuerte */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("") # Espacio para centrar mejor
st.write("")
st.write("")

# URL de una animación de corazón de LottieFiles
lottie_heart = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_t0g5y.json")

if lottie_heart:
    st_lottie(lottie_heart, speed=1, width=300, height=300, key="heart_animation")
else:
    st.write("No se pudo cargar la animación del corazón. ¡Pero el sentimiento es el mismo! ❤️")

st.markdown('<p class="big-font"># Te extraño mucho mi hamburguesita</p>', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("---")
st.markdown("¡Espero que te guste mucho!")
