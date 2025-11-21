import streamlit as st
import unicodedata

st.set_page_config(page_title="שילוב כל האמוג'ים", layout="wide")
st.title("🌈 כל האמוג’ים – בחר ושילב!")

# ----------- יצירת רשימת כל האמוג'ים (~3,304+) -------------
def generate_all_emojis():
    ranges = [
        (0x1F300, 0x1F5FF),  # סמלים מודרניים
        (0x1F600, 0x1F64F),  # סמיילים והבעות
        (0x1F680, 0x1F6FF),  # תחבורה ומקומות
        (0x2600, 0x26FF),    # סמלים כלליים
        (0x2700, 0x27BF),    # סמלים נוספים
        (0x1F1E6, 0x1F1FF),  # דגלים
        (0x1F900, 0x1F9FF),  # אנשים, גוף, חיות מודרניות
    ]
    emojis = []
    for start, end in ranges:
        for code in range(start, end + 1):
            try:
                char = chr(code)
                unicodedata.name(char)  # בדיקה אם חוקי
                emojis.append(char)
            except:
                continue
    # הסרת כפולים ומיון
    emojis = list(set(emojis))
    emojis.sort()
    return emojis

if "all_emojis" not in st.session_state:
    st.session_state.all_emojis = generate_all_emojis()

all_emojis = st.session_state.all_emojis
st.success(f"נטענו {len(all_emojis)} אמוג'ים מכל הסוגים! 🎉")

# ----------- בחירת מספר אמוג'ים -------------
st.subheader("בחר עד 5 אמוג'ים לשילוב")
num = st.slider("כמה אמוג'ים?", 1, 5, 2)

selected = []
for i in range(num):
    s = st.selectbox(f"אמוג'י {i+1}", all_emojis, index=i)
    selected.append(s)

# ----------- הצגת השילוב -------------
st.subheader("השילוב שלך")
combined = "".join(selected)

st.markdown(f"**אופקי:** {combined}")
st.markdown(f"**אנכי:** {combined.replace('', '\n')[1:-1]}")
st.markdown(f"<div style='font-size:80px'>{combined}</div>", unsafe_allow_html=True)
