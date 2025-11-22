import streamlit as st
import random
import time

# ---------- הגדרות עמוד ----------
st.set_page_config(page_title="👻 משחק אימה אוטומטי", page_icon="👻", layout="centered")
st.title("👻 משחק אימה אוטומטי מאוד מפחיד")
st.write("הישאר חי, נסה לא להיבהל! 😱")

# ---------- מצב ראשוני ----------
if "fear" not in st.session_state:
    st.session_state.fear = 0
if "health" not in st.session_state:
    st.session_state.health = 100
if "game_running" not in st.session_state:
    st.session_state.game_running = True

placeholder = st.empty()

# ---------- פונקציה לתיקון ערכים ----------
def clamp(value, min_value=0, max_value=100):
    return min(max(value, min_value), max_value)

# ---------- פונקציה לאירוע מפחיד ----------
def scary_event():
    event_type = random.choice(["רוח רפאים", "קול פתאומי", "צל מסתורי", "מפלצת פתאומית"])
    fear_increase = random.randint(5, 20)
    st.session_state.fear += fear_increase
    st.session_state.fear = clamp(st.session_state.fear)
    return f"💀 {event_type}! הפחד שלך עולה ב-{fear_increase}!"

# ---------- פונקציה לאירוע אוכל ----------
def food_event():
    health_gain = random.randint(5, 15)
    st.session_state.health += health_gain
    st.session_state.health = clamp(st.session_state.health)
    return f"🍎 מצאת אוכל! הבריאות שלך עולה ב-{health_gain}!"

# ---------- לולאה אוטומטית ----------
for i in range(50):  # 50 עדכונים, אפשר לשנות למספר גדול יותר
    if not st.session_state.game_running:
        break

    message = "כל בסדר כרגע..."

    # אירוע מפחיד 40% סיכוי
    if random.random() < 0.4:
        message = scary_event()
        st.session_state.health -= random.randint(0, 15)
        st.session_state.health = clamp(st.session_state.health)

    # אירוע אוכל 20% סיכוי
    elif random.random() < 0.2:
        message = food_event()

    # עדכון המסך
    with placeholder.container():
        st.subheader("📊 מצבך:")
        st.write(f"**פחד:** {st.session_state.fear}")
        st.progress(clamp(st.session_state.fear)/100)
        st.write(f"**בריאות:** {st.session_state.health}")
        st.progress(clamp(st.session_state.health)/100)
        st.write(f"{message}")

    # בדיקת מצב סיום
    if st.session_state.health <= 0:
        st.error("💀 אתה מת! המשחק נגמר…")
        st.session_state.game_running = False
        break
    if st.session_state.fear >= 100:
        st.error("😱 הפחד השתלט עליך! אתה בורח מהחדר… המשחק נגמר")
        st.session_state.game_running = False
        break

    time.sleep(1)

# ---------- התחלה מחדש ----------
if st.button("♻️ התחלת משחק חדש"):
    st.session_state.fear = 0
    st.session_state.health = 100
    st.session_state.game_running = True
    st.experimental_rerun()
