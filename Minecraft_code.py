import streamlit as st
import random

st.set_page_config(page_title="🍳 סופר משחק בישול 500 מתכונים", layout="wide")
st.title("🍳 סופר משחק בישול – 500 מתכונים")

# ----------- יצירת 500 מתכונים לדוגמה ----------
ingredients_pool = [f"מרכיב {i}" for i in range(1, 401)]  # 400 מרכיבים
recipes = {}
for i in range(1, 501):
    recipes[f"מתכון {i}"] = random.sample(ingredients_pool, k=random.randint(3,7))

# ----------- סטטוס המשחק ----------
if "bowl" not in st.session_state:
    st.session_state.bowl = []
if "score" not in st.session_state:
    st.session_state.score = 0

# ----------- בחירת מתכון ----------
selected_recipe = st.selectbox("בחר מתכון לנסות לבשל:", list(recipes.keys()))
st.subheader(f"מתכון נבחר: {selected_recipe}")

# ----------- הצגת המרכיבים עם כפתורים (רק חלק מהם כדי לא לעמוס) ----------
st.subheader("הוסף מרכיבים לקערה:")
display_ingredients = random.sample(ingredients_pool, 50)  # מציג רק 50 מרכיבים בכל פעם
cols = st.columns(5)
for i, ing in enumerate(display_ingredients):
    col = cols[i % 5]
    if col.button(f"➕ {ing}"):
        st.session_state.bowl.append(ing)

# ----------- הצגת תוכן הקערה ----------
st.subheader("מה יש בקערה עכשיו?")
st.write(" | ".join(st.session_state.bowl) if st.session_state.bowl else "הקערה ריקה 🥣")

# ----------- פעולות בישול ----------
st.subheader("פעולות בישול:")
col1, col2 = st.columns(2)
with col1:
    if st.button("ערבב 🔄"):
        if st.session_state.bowl:
            st.success("🔄 ערבבת את המרכיבים!")
        else:
            st.warning("הקערה ריקה! הוסף מרכיבים קודם.")
with col2:
    if st.button("בשל 🍳"):
        if not st.session_state.bowl:
            st.warning("אין מרכיבים בקערה!")
        else:
            correct_ingredients = set(recipes[selected_recipe])
            added_ingredients = set(st.session_state.bowl)
            if correct_ingredients == added_ingredients:
                st.success(f"🎉 הצלחת לבשל {selected_recipe}! 🏆")
                st.session_state.score += 1
            else:
                st.error(f"❌ המרכיבים אינם נכונים. המתכון הנכון: {', '.join(correct_ingredients)}")
            st.session_state.bowl.clear()

# ----------- ניקוד ותמיכה באמוג'ים ----------
st.subheader(f"ניקוד: {st.session_state.score} ⭐")
st.info("נסה לשלב את המרכיבים הנכונים לפי המתכון ובשל! 🌟")

# ----------- כפתור לאיפוס הקערה ----------
if st.button("♻️ אפס קערה"):
    st.session_state.bowl.clear()
    st.success("הקערה ריקה עכשיו! 🥣")
