import streamlit as st

st.set_page_config(page_title="משחק בישול אינטראקטיבי", layout="wide")
st.title("🍳 משחק בישול אינטראקטיבי – גרסה משודרגת")

# ----------- רשימת מתכונים ----------
recipes = {
    "חביתה": ["ביצה", "חלב", "מלח"],
    "סלט ירקות": ["עגבנייה", "מלפפון", "גזר", "שמן זית"],
    "פנקייק": ["ביצה", "חלב", "קמח", "סוכר"],
}

# ----------- רשימת מרכיבים כללית ----------
all_ingredients = ["ביצה", "חלב", "קמח", "גזר", "תפוח", "עגבנייה", "מלפפון", "שמן זית", "סוכר"]

# ----------- סטטוס המשחק ----------
if "bowl" not in st.session_state:
    st.session_state.bowl = []
if "score" not in st.session_state:
    st.session_state.score = 0

# ----------- בחירת מתכון ----------
selected_recipe = st.selectbox("בחר מתכון לנסות לבשל:", list(recipes.keys()))
st.subheader(f"מתכון נבחר: {selected_recipe}")

# ----------- בחירת מרכיבים ----------
st.subheader("הוסף מרכיבים לקערה:")
cols = st.columns(len(all_ingredients))
for i, ing in enumerate(all_ingredients):
    with cols[i]:
        if st.button(f"➕ {ing}"):
            st.session_state.bowl.append(ing)

st.subheader("מה יש בקערה עכשיו?")
st.write(" | ".join(st.session_state.bowl) if st.session_state.bowl else "הקערה ריקה 🥣")

# ----------- פעולות בישול ----------
st.subheader("פעולות בישול:")
col1, col2 = st.columns(2)
with col1:
    if st.button("ערבב"):
        if st.session_state.bowl:
            st.success("🔄 ערבבת את המרכיבים!")
        else:
            st.warning("הקערה ריקה! הוסף מרכיבים קודם.")
with col2:
    if st.button("בשל / טגן / אפה"):
        if not st.session_state.bowl:
            st.warning("אין מרכיבים בקערה!")
        else:
            correct_ingredients = set(recipes[selected_recipe])
            added_ingredients = set(st.session_state.bowl)
            if correct_ingredients == added_ingredients:
                st.success(f"🎉 הצלחת לבשל {selected_recipe}! כל הכבוד!")
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
    st.success("הקערה ריקה עכשיו!")
