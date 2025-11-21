import streamlit as st
import unicodedata

st.set_page_config(page_title="שילוב אמוג'ים", layout="wide")
st.title("😀 שילוב שני אמוג'ים מכל האמוג'ים הקיימים")

# ----------- טוען את כל האמוג'ים -------------
def load_all_emojis():
    emojis = []
    # טווחי יוניקוד לאמוג'ים
    ranges = [
        (0x1F300, 0x1FAFF),  # סמלים ואמוג'ים
        (0x2600, 0x26FF),    # סמלים
        (0x2700, 0x27BF),    # סמלים נוספים
        (0x1F1E6, 0x1F1FF),  # דגלים
    ]
    for start, end in ranges:
        for code in range(start, end + 1):
            try:
                char = chr(code)
                unicodedata.name(char)  # בדיקה אם חוקי
                emojis.append(char)
            except:
                continue
    # הסרת כפולים
    emojis = list(set(emojis))
    emojis.sort()
    return emojis

if "all_emojis" not in st.session_state:
    st.session_state.all_emojis = load_all_emojis()

all_emojis = st.session_state.all_emojis
st.success(f"נטענו {len(all_emojis)} אמוג'ים!")

# ----------- בחירת שני אמוג'ים -------------
st.subheader("בחר שני אמוג'ים לשילוב")
emoji1 = st.selectbox("אמוג'י ראשון", all_emojis, index=0)
emoji2 = st.selectbox("אמוג'י שני", all_emojis, index=1)

# ----------- הצגת השילוב -------------
st.subheader("השילוב שלך")
st.markdown(f"**אופקי:** {emoji1}{emoji2}")
st.markdown(f"**אנכי:** {emoji1}\n{emoji2}")
st.markdown(f"<div style='font-size:80px'>{emoji1}{emoji2}</div>", unsafe_allow_html=True)
