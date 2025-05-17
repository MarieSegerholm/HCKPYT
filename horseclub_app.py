import streamlit as st
import json
import os
import datetime

# Ladda/spara profil
def get_filename(name, pin):
    return f"profil_{name}_{pin}.json"

def load_profile(name, pin):
    file = get_filename(name, pin)
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {
        "stars": 0,
        "calendar": [],
        "horses": {"Bella": False, "Stjärna": False, "Maja": False},
        "last_played": None,
        "task_done": False,
        "fed": False
    }

def save_profile(name, pin, data):
    file = get_filename(name, pin)
    with open(file, "w") as f:
        json.dump(data, f)

st.set_page_config(page_title="HorseClub Kids – DELUXE", layout="centered")
st.title("🐴 HorseClub Kids – DELUXE")

name = st.text_input("Ditt namn:")
pin = st.text_input("PIN (4 siffror):", type="password", max_chars=4)

if name and pin:
    profile = load_profile(name, pin)
    today = str(datetime.date.today())

    if profile["last_played"] != today:
        profile["horses"] = {h: False for h in profile["horses"]}
        profile["task_done"] = False
        profile["fed"] = False
        profile["last_played"] = today

    st.subheader(f"Hej {name} 👋")
    st.markdown("## 📅 Dagens uppdrag: 🧼 Rykta + mata hästarna")

    if not profile["fed"]:
        st.image("bilder/ho.png", width=80)
        if st.button("🍎 Ge hö, morot & vatten"):
            profile["fed"] = True
            st.success("Hästarna har fått mat och vatten!")
    else:
        st.info("✅ Hästarna är redan matade idag")

    for horse in profile["horses"]:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(f"bilder/{horse.lower()}.png", width=100)
        with col2:
            st.subheader(horse)
            if not profile["horses"][horse]:
                if st.button(f"🧼 Rykta {horse}"):
                    profile["horses"][horse] = True
                    st.success(f"{horse} är nu ryktad!")
            else:
                st.info(f"{horse} är redan ryktad")

    if all(profile["horses"].values()) and profile["fed"] and not profile["task_done"]:
        profile["stars"] += 1
        profile["calendar"].append(today)
        profile["task_done"] = True
        st.balloons()
        st.success("🎉 Du klarade dagens uppdrag och fick en ⭐!")

    st.markdown(f"### ⭐ Totala stjärnor: {profile['stars']}")
    st.markdown("### 📅 Kalender:")
    for date in sorted(profile["calendar"]):
        st.write(f"✔️ {date}")

    if profile["stars"] >= 20:
        st.image("bilder/pokal.png", width=100)
        st.success("🏆 Du har fått en pokal!")
    elif profile["stars"] >= 10:
        st.image("bilder/medalj.png", width=100)
        st.success("🎖️ Du har fått en medalj!")
    elif profile["stars"] >= 5:
        st.image("bilder/rosett.png", width=100)
        st.success("🎁 Du har fått en rosett!")

    if profile["stars"] >= 10:
        st.markdown("### 🏇 Tävling")
        st.image("bilder/tavling.png", width=100)
        if st.button("🏁 Delta i tävling"):
            st.success("🎉 Du vann en extra ⭐ i tävlingen!")
            profile["stars"] += 1

    save_profile(name, pin, profile)

import streamlit as st
import json
import os
import datetime


# Initiera talsyntes
engine = pyttsx3.init()
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass

# Ladda/spara profil
def get_filename(name, pin):
    return f"profil_{name}_{pin}.json"

def load_profile(name, pin):
    file = get_filename(name, pin)
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return {
        "stars": 0,
        "calendar": [],
        "horses": {"Bella": False, "Stjärna": False, "Maja": False},
        "last_played": None,
        "task_done": False,
        "fed": False
    }

def save_profile(name, pin, data):
    file = get_filename(name, pin)
    with open(file, "w") as f:
        json.dump(data, f)

st.set_page_config(page_title="HorseClub Kids – DELUXE", layout="centered")
st.title("🐴 HorseClub Kids – DELUXE")

name = st.text_input("Ditt namn:")
pin = st.text_input("PIN (4 siffror):", type="password", max_chars=4)
voice_on = st.checkbox("🔊 Talsyntes aktiv", value=True)

if name and pin:
    profile = load_profile(name, pin)
    today = str(datetime.date.today())

    if profile["last_played"] != today:
        profile["horses"] = {h: False for h in profile["horses"]}
        profile["task_done"] = False
        profile["fed"] = False
        profile["last_played"] = today

    st.subheader(f"Hej {name} 👋")
    st.markdown("## 📅 Dagens uppdrag: 🧼 Rykta + mata hästarna")

    if not profile["fed"]:
        st.image("bilder/ho.png", width=80)
        if st.button("🍎 Ge hö, morot & vatten"):
            profile["fed"] = True
            st.success("Hästarna har fått mat och vatten!")
            if voice_on: speak("Hästarna är mätta och glada!")
    else:
        st.info("✅ Hästarna är redan matade idag")

    for horse in profile["horses"]:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(f"bilder/{horse.lower()}.png", width=100)
        with col2:
            st.subheader(horse)
            if not profile["horses"][horse]:
                if st.button(f"🧼 Rykta {horse}"):
                    profile["horses"][horse] = True
                    st.success(f"{horse} är nu ryktad!")
                    if voice_on: speak(f"Bra jobbat! Du ryktade {horse}.")
            else:
                st.info(f"{horse} är redan ryktad")

    if all(profile["horses"].values()) and profile["fed"] and not profile["task_done"]:
        profile["stars"] += 1
        profile["calendar"].append(today)
        profile["task_done"] = True
        st.balloons()
        st.success("🎉 Du klarade dagens uppdrag och fick en ⭐!")
        if voice_on: speak("Du klarade dagens uppdrag!")

    st.markdown(f"### ⭐ Totala stjärnor: {profile['stars']}")
    st.markdown("### 📅 Kalender:")
    for date in sorted(profile["calendar"]):
        st.write(f"✔️ {date}")

    if profile["stars"] >= 20:
        st.image("bilder/pokal.png", width=100)
        st.success("🏆 Du har fått en pokal!")
    elif profile["stars"] >= 10:
        st.image("bilder/medalj.png", width=100)
        st.success("🎖️ Du har fått en medalj!")
    elif profile["stars"] >= 5:
        st.image("bilder/rosett.png", width=100)
        st.success("🎁 Du har fått en rosett!")

    if profile["stars"] >= 10:
        st.markdown("### 🏇 Tävling")
        st.image("bilder/tavling.png", width=100)
        if st.button("🏁 Delta i tävling"):
            st.success("🎉 Du vann en extra ⭐ i tävlingen!")
            profile["stars"] += 1
            if voice_on: speak("Grattis! Du vann tävlingen.")

    save_profile(name, pin, profile)
