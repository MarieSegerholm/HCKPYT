
import streamlit as st
import base64
from pathlib import Path
import pygame

# Initiera pygame för ljud
pygame.init()
pygame.mixer.init()

# Hästdata
horses = {
    "Maja": "maja.png",
    "Bella": "bella.png",
    "Prins": "prins.png",
    "Shine": "Shine.png"
}

STALL_IMAGE = "stall.png"
BRUSH_IMAGE = "ryktborste.png"
WHINNY_SOUND = "horse whinny.mp3"

st.set_page_config(layout="wide")
st.title("🐴 Välj din häst för borstning")

selected_horse = st.selectbox("Välj häst:", list(horses.keys()))
brush_count = st.session_state.get("brush_count", 0)
groomed = st.session_state.get("groomed", False)

# Visa stallbild som bakgrund
def set_background(image_path):
    bin_str = base64.b64encode(Path(image_path).read_bytes()).decode()
    css = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)

set_background(STALL_IMAGE)

# Hästvisning
st.subheader(f"Du har valt {selected_horse}")
col1, col2 = st.columns([2, 1])
with col1:
    st.image(horses[selected_horse], width=500)
with col2:
    if not groomed:
        st.image(BRUSH_IMAGE, caption="Svep borsten 10 gånger")
        if st.button("Svep ryktborsten"):
            brush_count += 1
            st.session_state.brush_count = brush_count
            if brush_count >= 10:
                st.session_state.groomed = True
                st.session_state.stars = st.session_state.get("stars", 0) + 2
                pygame.mixer.music.load(WHINNY_SOUND)
                pygame.mixer.music.play()
                st.success(f"🎉 {selected_horse} är färdigryktad! Du fick ⭐⭐")
    else:
        st.info(f"{selected_horse} är redan ryktad")

st.write("Totala stjärnor: ⭐" + str(st.session_state.get("stars", 0)))
