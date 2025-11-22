import streamlit as st

# ---------- הגדרות עמוד ----------
st.set_page_config(page_title="🦄 משחק חד־קרן חמוד", page_icon="🦄", layout="centered")
st.title("🦄 טאמגוצ’י חד־קרן חמוד")
st.write("טפל בחד־קרן שלך: האכל, שחק ותן לו לישון!")

# ---------- מצב ראשוני ----------
if "happiness" not in st.session_state:
    st.session_state.happiness = 50
if "energy" not in st.session_state:
    st.session_state.energy = 50
if "cleanliness" not in st.session_state:
    st.session_state.cleanliness = 50

# ---------- העלאת תמונה ----------
uploaded_image = st.file_uploader("גרור ושחרר כאן תמונה של חד־קרן (PNG/JPG)", type=["png", "jpg", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, width=250)
else:
    st.info("⬆️ גרור ושחרר תמונה כדי שהחד־קרן יופיע במשחק")

# ---------- פונקציה לתיקון ערכים ----------
def clamp(value):
    return min(max(value, 0), 100)

# ---------- פסי התקדמות ----------
st.subheader("📊 מצב חד־הקרן:")
st.write("**שמחה:**")
st.progress(clamp(st.session_state.happiness)/100)
st.write("**אנרגיה:**")
st.progress(clamp(st.session_state.energy)/100)
st.write("**ניקיון:**")
st.progress(clamp(st.session_state.cleanliness)/100)

st.divider()

# ---------- כפתורי פעולה ----------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🍎 האכל"):
        st.session_state.happiness += 10
        st.session_state.energy += 15
        st.session_state.cleanliness -= 5
        st.success("התינוק אוכל בשמחה!")

with col2:
    if st.button("🛁 מקלחת"):
        st.session_state.cleanliness += 20
        st.session_state.happiness -= 5
        st.info("התינוק מתקלח!")

with col3:
    if st.button("🎈 לשחק"):
        st.session_state.happiness += 15
        st.session_state.energy -= 10
        st.success("התינוק משחק וצוחק!")

if st.button("😴 לישון"):
    st.session_state.energy += 25
    st.session_state.happiness += 5
    st.info("התינוק נרדם...")

# ---------- תיקון גבולות ----------
st.session_state.happiness = clamp(st.session_state.happiness)
st.session_state.energy = clamp(st.session_state.energy)
st.session_state.cleanliness = clamp(st.session_state.cleanliness)

st.divider()

# ---------- התראות ----------
if st.session_state.happiness >= 100:
    st.success("🎉 חד־הקרן מאושר מאוד!")
elif st.session_state.happiness < 20:
    st.warning("☹️ חד־הקרן עצוב… תעזור לו!")

if st.session_state.energy < 20:
    st.warning("😴 חד־הקרן עייף… כדאי לישון!")

if st.session_state.cleanliness < 20:
    st.warning("🧽 חד־הקרן מלוכלך!")

# ---------- התחלה מחדש ----------
if st.button("♻️ התחלת משחק חדש"):
    st.session_state.happiness = 50
    st.session_state.energy = 50
    st.session_state.cleanliness = 50
    st.success("🎉 המשחק התחיל מחדש!")
