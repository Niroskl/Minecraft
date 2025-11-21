import streamlit as st

st.set_page_config(page_title="Minecraft Presentation", layout="centered")
st.title("🎮 מצגת Minecraft בסגנון Streamlit")

slides = [
    "ברוכים הבאים למצגת על Minecraft!",
    "Minecraft הוא משחק Sandbox פופולרי.",
    "ניתן לשחק במצב Survival או Creative.",
    "יש חיות, מפלצות, כפרים, ומאגרי משאבים.",
    "Minecraft הוא אחד המשחקים הנמכרים ביותר בעולם.",
    "סיום: תודה על הצפייה במצגת Minecraft!"
]

# ניווט בין שקופיות
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
st.markdown(f"<h2 style='color:#006666'>{slides[st.session_state.slide_index]}</h2>", unsafe_allow_html=True)
