import streamlit as st

st.set_page_config(page_title="🦄 טיפול בחד־קרן תינוק", page_icon="🦄", layout="centered")

# --- מצב המשחק --- #
if "happiness" not in st.session_state:
    st.session_state.happiness = 50
if "energy" not in st.session_state:
    st.session_state.energy = 50
if "cleanliness" not in st.session_state:
    st.session_state.cleanliness = 50

st.title("🦄 טיפול בחד־קרן תינוק")
st.write("בחר תמונה של חד־קרן תינוק מהמחשב שלך!")

# -------- תמונה -------- #
uploaded_image = st.file_uploader("העלה תמונה (PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, width=320)
else:
    st.info("⬆️ העלה תמונה כדי שהחד־קרן יופיע במשחק!")

st.subheader("מצב התינוק:")

# --- פסי התקדמות --- #
st.progress(st.session_state.happiness / 100, text="שמחה")
st.progress(st.session_state.energy / 100, text="אנרגיה")
st.progress(st.session_state.cleanliness / 100, text="ניקיון")

st.divider()

# --- כפתורי פעולות --- #
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🍏 להאכיל"):
        st.session_state.happiness += 10
        st.session_state.energy += 15
        st.session_state.cleanliness -= 5

with col2:
    if st.button("🧼 מקלחת"):
        st.session_state.cleanliness += 20
        st.session_state.happiness -= 5

with col3:
    if st.button("🎈 לשחק"):
        st.session_state.happiness += 15
        st.session_state.energy -= 10

if st.button("😴 לישון"):
    st.session_state.energy += 25
    st.session_state.happiness += 5

# --- תיקון גבולות --- #
st.session_state.happiness = min(max(st.session_state.happiness, 0), 100)
st.session_state.energy = min(max(st.session_state.energy, 0), 100)
st.session_state.cleanliness = min(max(st.session_state.cleanliness, 0), 100)

st.divider()

# --- התראות --- #
if st.session_state.happiness == 100:
    st.success("🎉 חד־הקרן מאושר מאוד!")
elif st.session_state.happiness < 20:
    st.error("☹️ חד־הקרן עצוב… תעזור לו!")

if st.session_state.energy < 20:
    st.warning("😴 חד־הקרן עייף… כדאי לישון!")

if st.session_state.cleanliness < 20:
    st.warning("🧽 חד־הקרן מלוכלך!")
