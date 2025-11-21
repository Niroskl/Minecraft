import streamlit as st
import random

st.set_page_config(page_title="משחק ללמוד עברית", layout="wide")
st.title("📝 משחק ללמוד עברית – כיתה ג'")

# ----------- רשימת מילים עם תמונה ----------
# במציאות אפשר לשים קבצי תמונה מקומיים או קישורים
words = [
    {"word": "תפוח", "image": "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg"},
    {"word": "כלב", "image": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"},
    {"word": "חתול", "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg"},
    {"word": "בית", "image": "https://upload.wikimedia.org/wikipedia/commons/a/a3/White_house.jpg"},
    {"word": "ספר", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Bookshelf.jpg"},
]

# ----------- בחירת מילה אקראית ----------
current = random.choice(words)

st.subheader("מה המילה שמתאימה לתמונה?")
st.image(current["image"], width=300)

# ----------- אפשרויות תשובה ----------
options = [current["word"]]
# מוסיפים שתי אפשרויות נוספות אקראיות
while len(options) < 3:
    w = random.choice(words)["word"]
    if w not in options:
        options.append(w)

random.shuffle(options)

# ----------- בחירה מהמשתמש ----------
choice = st.radio("בחר את התשובה הנכונה:", options)

if st.button("בדוק"):
    if choice == current["word"]:
        st.success("🎉 נכון! כל הכבוד!")
    else:
        st.error(f"❌ לא נכון. המילה הנכונה היא: {current['word']}")
