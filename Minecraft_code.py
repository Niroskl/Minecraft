import streamlit as st
import random
import time

st.set_page_config(page_title="🦄 תינוק חד קרן", layout="wide")

# ----------- עיצוב רקע מהמם -----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #a0e7ff, #d6bfff, #ffe4fa);
}
</style>
""", unsafe_allow_html=True)

st.title("🦄👶 תינוק חד־קרן – משחק טיפול משודרג")
st.subheader("דאגו לתינוק החד־קרן שיהיה שמח, רגוע ומטופל! 🌈")

# ----------- מצב פנימי -----------

if "happiness" not in st.session_state:
    st.session_state.happiness = 5
if "energy" not in st.session_state:
    st.session_state.energy = 5
if "hunger" not in st.session_state:
    st.session_state.hunger = 5
if "mood" not in st.session_state:
    st.session_state.mood = "רגוע"

# ----------- תמונת תינוק חד קרן אמיתית -----------

unicorn_baby_image = "https://i.imgur.com/8oaS4tF.png"  # תינוק חד קרן אמיתי

st.image(unicorn_baby_image, width=300, caption="תינוק חד־קרן חמוד 🦄💖")

# ----------- פונקציה לעדכון מצב -----------

def update_status(action):
    if action == "feed":
        st.session_state.hunger += 2
        st.session_state.happiness += 1
        st.session_state.mood = "שבע ומרוצה 😋"
    elif action == "play":
        st.session_state.happiness += 3
        st.session_state.energy -= 1
        st.session_state.mood = "משועשע ושמח 😄"
    elif action == "sleep":
        st.session_state.energy += 3
        st.session_state.mood = "ישן מתוק 😴"
    elif action == "hug":
        st.session_state.happiness += 2
        st.session_state.mood = "מרגיש אהבה 🤗💖"

    # גבולות
    st.session_state.energy = min(max(st.session_state.energy, 0), 10)
    st.session_state.hunger = min(max(st.session_state.hunger, 0), 10)
    st.session_state.happiness = min(max(st.session_state.happiness, 0), 10)


# ----------- כפתורים -----------

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🍎 להאכיל"):
        update_status("feed")
        st.success("התינוק חד־קרן אוכל בהנאה!")

with col2:
    if st.button("🎾 לשחק"):
        update_status("play")
        st.info("התינוק מתגלגל מצחוק!")

with col3:
    if st.button("😴 להשכיב לישון"):
        update_status("sleep")
        st.warning("זזז… התינוק נרדם.")

with col4:
    if st.button("🤗 חיבוק"):
        update_status("hug")
        st.balloons()
        st.success("איזה חיבוק! התינוק מאושר!")

# ----------- תצוגת מצב -----------

st.markdown("### מצב התינוק:")

st.progress(st.session_state.happiness/10)
st.write(f"**שמחה:** {st.session_state.happiness}/10")

st.progress(st.session_state.energy/10)
st.write(f"**אנרגיה:** {st.session_state.energy}/10")

st.progress(st.session_state.hunger/10)
st.write(f"**שובע:** {st.session_state.hunger}/10")

st.info(f"**מצב רוח נוכחי:** {st.session_state.mood}")

# ----------- ניצחון -----------

if st.session_state.happiness == 10 and st.session_state.energy >= 8 and st.session_state.hunger >= 8:
    st.success("🌈🦄 התינוק חד־קרן הגיע לאושר מושלם!!!")
    st.balloons()

# ----------- איפוס -----------

if st.button("♻️ התחלת משחק חדש"):
    st.session_state.happiness = 5
    st.session_state.energy = 5
    st.session_state.hunger = 5
    st.session_state.mood = "רגוע"
    st.success("🎉 המשחק התחיל מחדש!")
