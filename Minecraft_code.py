import streamlit as st
import random
import time

# ---------- הגדרות עמוד ----------
st.set_page_config(page_title="👻 משחק אימה", page_icon="👻", layout="centered")
st.title("👻 משחק אימה מפחיד מאוד מאוד")
st.write("הישאר חי, נסה לא להיבהל! 😱")

# ---------- מצב ראשוני ----------
if "fear" not in st.session_state:
    st.session_state.fear = 0      # פחד
if "health" not in st.session_state:
    st.session_state.health = 100  # בריאות

# ---------- פונקציה לתיקון ערכים ----------
def clamp(value, min_value=0, max_value=100):
    return min(max(value, min_value), max_value)

# ---------- אירוע אקראי מפחיד ----------
def scary_event():
    event_type = random.choice(["רוח רפאים", "קול פתאומי", "צל מסתורי", "מפלצת פתאומית"])
    fear_increase = random.randint(10, 30)
    st.session_state.fear += fear_increase
    st.session_state.fear = clamp(st.session_state.fear)
    st.warning(f"💀 {event_type}! הפחד שלך עולה ב-{fear_increase}!")

# ---------- מדדים ----------
st.subheader("📊 מצבך:")
st.write("**פחד:**")
st.progress(clamp(st.session_state.fear)/100)
st.write("**בריאות:**")
st.progress(clamp(st.session_state.health)/100)

st.divider()

# ---------- כפתורי פעולה ----------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🕯 הדלק נר"):
        st.success("הנר מאיר את החדר, הפחד יורד מעט!")
        st.session_state.fear -= 10
        st.session_state.fear = clamp(st.session_state.fear)

with col2:
    if st.button("🏃‍♂️ לברוח"):
        st.info("אתה מנסה לברוח…")
        if random.random() < 0.5:
            st.success("ברחת בהצלחה! הפחד קטן מעט")
            st.session_state.fear -= 15
        else:
            st.error("לא הספקת לברוח! הבריאות יורדת")
            st.session_state.health -= 20
        st.session_state.fear = clamp(st.session_state.fear)
        st.session_state.health = clamp(st.session_state.health)

with col3:
    if st.button("🔎 לבדוק את החדר"):
        st.info("אתה בודק את החדר…")
        if random.random() < 0.6:
            st.success("החדר רגוע…")
        else:
            scary_event()

# ---------- אירוע אקראי קורה לעיתים ----------
if random.random() < 0.3:
    scary_event()

st.divider()

# ---------- התראות סיום ----------
if st.session_state.health <= 0:
    st.error("💀 אתה מת! המשחק נגמר…")
    if st.button("♻️ התחלה מחדש"):
        st.session_state.fear = 0
        st.session_state.health = 100

elif st.session_state.fear >= 100:
    st.error("😱 הפחד שלך השתלט עליך! אתה בורח מהחדר… המשחק נגמר")
    if st.button("♻️ התחלה מחדש"):
        st.session_state.fear = 0
        st.session_state.health = 100

# ---------- התחלה מחדש ----------
if st.button("♻️ התחלת משחק חדש"):
    st.session_state.fear = 0
    st.session_state.health = 100
    st.success("🎉 המשחק התחיל מחדש!")
