import streamlit as st
import unicodedata

st.set_page_config(page_title="כל האמוג'ים והסמלים", layout="wide")
st.title("🎨 בחר אמוג'י או סמל מכל היוניקוד")

# ----------- טוען את כל האמוג'ים והסמלים -------------
def load_all_emojis_and_symbols():
    emojis = []
    ranges = [
        (0x1F300, 0x1FAFF),  # אמוג'ים מודרניים
        (0x2600, 0x26FF),    # סמלים כלליים
        (0x2700, 0x27BF),    # סמלים נוספים
        (0x1F1E6, 0x1F1FF),  # דגלים
    ]
    for start, end in ranges:
        for code in range(start, end + 1):
            try:
                char = chr(code)
                # אם יש שם רשמי ביוניקוד, זה תקין
                unicodedata.name(char)
                emojis.append(char)
            except:
                continue
    emojis = list(set(emojis))
    emojis.sort()
    return emojis

if "all_symbols" not in st.session_state:
    st.session_state.all_symbols = load_all_emojis_and_symbols()

all_symbols = st.session_state.all_symbols
st.success(f"נטענו {len(all_symbols)} אמוג'ים וסמלים! 🎉")

# ----------- בחירת אמוג'ים/סמלים -------------
st.subheader("בחר עד 5 אמוג'ים/סמלים")
num = st.slider("כמה לבחור?", 1, 5, 2)

selected = []
for i in range(num):
    s = st.selectbox(f"סמל/אמוג'י {i+1}", all_symbols, index=i)
    selected.append(s)

# ----------- הצגת השילוב -------------
st.subheader("השילוב שלך")
combined = "".join(selected)
st.markdown(f"**בגודל רגיל:** {combined}")
st.markdown(f"<div style='font-size:80px'>{combined}</div>", unsafe_allow_html=True)
