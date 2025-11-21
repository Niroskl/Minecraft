import streamlit as st

st.set_page_config(page_title="Minecraft Canva Style", layout="wide")

# CSS לעיצוב שקופיות
st.markdown("""
<style>
body {
    background-color: #40E0D0; /* טורקיז */
    font-family: 'Courier New', monospace;
    color: white;
}
.slide {
    background-color: #006666;
    border-radius: 25px;
    padding: 50px;
    text-align: center;
    margin: 20px auto;
    max-width: 800px;
    box-shadow: 10px 10px 30px rgba(0,0,0,0.3);
}
.slide h1 {
    font-size: 48px;
    margin-bottom: 20px;
}
.slide p {
    font-size: 28px;
}
.slide img {
    max-width: 60%;
    margin-top: 20px;
    border-radius: 15px;
    box-shadow: 5px 5px 20px rgba(0,0,0,0.5);
}
button {
    background-color: #004d4d;
    color: white;
    padding: 15px 25px;
    font-size: 18px;
    border-radius: 10px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 מצגת Minecraft בסגנון Canva")

# רשימת שקופיות עם טקסט ותמונה
slides = [
    {"title": "ברוכים הבאים ל-Minecraft!", "text": "משחק Sandbox פופולרי בעולם.", "img": None},
    {"title": "מצבי משחק", "text": "Survival ו-Creative – לגלות ולבנות חופשי.", "img": None},
    {"title": "עולם פתוח", "text": "חקור כפרים, יערות, מערות וחיות.", "img": None},
    {"title": "מולטיפלייר", "text": "שחק עם חברים ברשת או יצור מודים.", "img": None},
    {"title": "סיום", "text": "Minecraft הוא משחק מהנה לכל הגילים!", "img": None}
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

# הצגת השקופית הנוכחית
slide = slides[st.session_state.slide_index]
st.markdown(f"<div class='slide'><h1>{slide['title']}</h1><p>{slide['text']}</p></div>", unsafe_allow_html=True)
if slide["img"]:
    st.image(slide["img"])
