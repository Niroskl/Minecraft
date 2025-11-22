import streamlit as st

st.set_page_config(page_title="מכין פיצה", page_icon="🍕")

st.title("🍕 מכין פיצה")
st.write("בחר את התוספות שאתה רוצה על הפיצה שלך:")

# תוספות אפשריות
toppings = [
    "גבינה נוספת",
    "זיתים",
    "פטריות",
    "בצל",
    "עגבניות",
    "פלפל חריף",
    "אננס",
    "נקניק"
]

# בחירת תוספות
selected_toppings = st.multiselect("תוספות:", toppings)

# כפתור להכנת הפיצה
if st.button("אפה את הפיצה!"):
    if selected_toppings:
        st.success(f"פיצה עם: {', '.join(selected_toppings)} מוכנה בתנור! 🍕🔥")
    else:
        st.warning("לא בחרת תוספות! זאת תהיה פיצה פשוטה 🍕")

# תצוגה ויזואלית
st.image("https://upload.wikimedia.org/wikipedia/commons/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg", width=300)
