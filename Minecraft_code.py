import streamlit as st

st.set_page_config(page_title="Minecraft Canva Style", layout="wide")

# רשימת שקופיות עם טקסט ותמונה
slides = [
    {"title": "ברוכים הבאים ל-Minecraft!", "text": "משחק Sandbox פופולרי בעולם."},
    {"title": "מצבי משחק", "text": "Survival ו-Creative – לגלות ולבנות חופשי."},
    {"title": "עולם פתוח", "text": "חקור כפרים, יערות, מערות וחיות."},
    {"title": "מולטיפלייר", "text": "שחק עם חברים ברשת או יצור מודים."},
    {"title": "סיום", "text": "Minecraft הוא משחק מהנה לכל הגילים!"}
]

# ניהול שקופית נוכחית
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

col1, col2, col3 = st.columns([1,2,1])
with col1:
    if st.button("⬅️ קודמת"):
        if st.session_state.slide_index > 0:
            st.session_state.slide_index -= 1
with col3:
    if st.button("➡️ הבאה"):
        if st.session_state.slide_index < len(slides)-1:
            st.session_state.slide_index += 1

# הצגת השקופית הנוכחית עם רקע Minecraft
slide = slides[st.session_state.slide_index]

st.markdown(
    f"""
    <div style="
        background-image: url('minecraft_bg.png');
        background-size: cover;
        background-position: center;
        padding: 100px;
        border-radius: 25px;
        text-align: center;
        color: white;
        box-shadow: 10px 10px 30px rgba(0,0,0,0.3);
    ">
        <h1 style='font-size:60px'>{slide['title']}</h1>
        <p style='font-size:28px'>{slide['text']}</p>
    </div>
    """,
    unsafe_allow_html=True
)
