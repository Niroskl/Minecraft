import streamlit as st

st.set_page_config(page_title="מטבח אינטראקטיבי", layout="wide")
st.title("🍳 בישול אינטראקטיבי במחשב")

# ----------- מרכיבים ----------
ingredients = ["ביצה", "חלב", "קמח", "גזר", "תפוח"]
if "bowl" not in st.session_state:
    st.session_state.bowl = []

st.subheader("בחר מרכיבים והוסף לקערה:")

cols = st.columns(len(ingredients))
for i, ing in enumerate(ingredients):
    with cols[i]:
        if st.button(f"➕ {ing}"):
            st.session_state.bowl.append(ing)

st.subheader("מה בקערה עכשיו?")
st.write(" | ".join(st.session_state.bowl) if st.session_state.bowl else "הקערה ריקה 🥣")

# ----------- פעולות ----------
st.subheader("בצע פעולה:")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("ערבב"):
        if st.session_state.bowl:
            st.success("🔄 ערבבת את המרכיבים!")
        else:
            st.warning("הקערה ריקה! הוסף מרכיבים קודם.")
with col2:
    if st.button("טגן"):
        if st.session_state.bowl:
            st.success("🍳 טיגנת את מה שיש בקערה!")
            st.session_state.bowl.clear()
        else:
            st.warning("אין מה לטגן!")
with col3:
    if st.button("אפה"):
        if st.session_state.bowl:
            st.success("🍰 אפית את מה שיש בקערה!")
            st.session_state.bowl.clear()
        else:
            st.warning("אין מה לאפות!")

st.info("הוסף מרכיבים, ערבב, וטגן או אפה. נסה ליצור משהו טעים! 😋")
