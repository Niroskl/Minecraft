import streamlit as st
import random

st.set_page_config(page_title="🦄 תינוק חד קרן", layout="wide")
st.title("🦄 משחק אינטראקטיבי – לטפל בתינוק חד קרן")

# ----------- רקע צבעוני ----------
st.markdown(
    """
    <style>
    body {
        background-color: #a0e7e5;
    }
    </style>
    """, unsafe_allow_html=True
)

# ----------- סטטוס ----------
if "happiness" not in st.session_state:
    st.session_state.happiness = 0

# ----------- תמונה של תינוק חד קרן ----------
unicorn_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Unicorn_fantasy.png/320px-Unicorn_fantasy.png"
st.image(unicorn_image_url, width=300)

# ----------- פעולות אינטראקטיביות ----------
st.subheader("מה תרצה לעשות עם התינוק חד קרן?")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("להאכיל 🍎"):
        st.session_state.happiness += random.randint(1, 3)
        st.success(f"התינוק חד קרן אוכל בשמחה! 🦄❤️ נקודות: {st.session_state.happiness}")

with col2:
    if st.button("לשחק 🎾"):
        st.session_state.happiness += random.randint(2, 4)
        st.info(f"התינוק חד קרן צוחק מהמשחק! 🦄✨ נקודות: {st.session_state.happiness}")

with col3:
    if st.button("ללטף 🤗"):
        st.session_state.happiness += random.randint(1, 2)
        st.warning(f"התינוק חד קרן נהנה מהחיבוק! 🦄💖 נקודות: {st.session_state.happiness}")

# ----------- מצב שמחה ----------
st.subheader(f"שמחת התינוק חד קרן: {st.session_state.happiness} ⭐")
if st.session_state.happiness >= 10:
    st.balloons()
    st.success("🎉 התינוק חד קרן מאושר מאוד! אתה אלוף בטיפול! 🦄🌈")

# ----------- כפתור לאיפוס ----------
if st.button("♻️ לאתחל משחק"):
    st.session_state.happiness = 0
    st.success("המשחק התחיל מחדש! 🦄")
