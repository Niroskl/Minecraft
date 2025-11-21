import streamlit as st

st.set_page_config(page_title="Minecraft Presentation", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #40E0D0;  /* רקע טורקיז */
        color: white;
        font-family: 'Courier New', monospace;
    }
    .slide-box {
        background-color: #006666;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 20px;
    }
    .slide-img {
        max-width: 80%;
        height: auto;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎮 מצגת Minecraft")

# רשימת שקופיות עם טקסט ותמונה (תמונות צריך להוריד או קישור URL)
slides = [
    {"text": "ברוכים הבאים למצגת על Minecraft!", "img": None},
    {"text": "Minecraft הוא משחק Sandbox פופולרי", "img": None},
    {"text": "ניתן לשחק במצב Survival או Creative", "img": None},
    {"text": "יש חיות, מפלצות, כפרים ומאגרי משאבים", "img": None},
    {"text": "Minecraft הוא אחד המשחקים הנמכרים ביותר בעולם", "img": None},
    {"text": "סיום: תודה על הצפייה במצגת Minecraft!", "img": None},
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

# הצגת השקופית
slide = slides[st.session_state.slide_index]
st.markdown(f"<div class='slide-box'><h2>{slide['text']}</h2></div>", unsafe_allow_html=True)

# אם יש תמונה לשקופית
if slide["img"]:
    st.image(slide["img"], use_column_width=True, caption="")
