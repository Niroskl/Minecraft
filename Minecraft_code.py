import streamlit as st
import emoji

st.set_page_config(page_title="כל האמוג'ים הקיימים", layout="wide")
st.title("🌈 כל האמוג׳ים הקיימים – בחר ושילב!")

# ----------- טוען את כל האמוג'ים הידועים -------------
all_emojis = list(emoji.EMOJI_DATA.keys())
all_emojis.sort()

st.success(f"נטענו {len(all_emojis)} אמוג'ים מכל הסוגים! 🎉")

# ----------- בחירת אמוג'ים -------------
st.subheader("בחר עד 5 אמוג'ים לשילוב")
num = st.slider("כמה לבחור?", 1, 5, 2)

selected = []
for i in range(num):
    s = st.selectbox(f"אמוג'י {i+1}", all_emojis, index=i)
    selected.append(s)

# ----------- הצגת השילוב -------------
st.subheader("השילוב שלך")
combined = "".join(selected)
st.markdown(f"**בגודל רגיל:** {combined}")
st.markdown(f"<div style='font-size:80px'>{combined}</div>", unsafe_allow_html=True)
