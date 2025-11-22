import streamlit as st

st.set_page_config(page_title="מכין פיצה", page_icon="🍕")

st.title("🍕 מכין פיצה — גרסה מורחבת!")
st.write("בחר את כל התוספות שאתה רוצה על הפיצה שלך:")

# תוספות אפשריות
toppings = [
    "גבינה נוספת",
    "זיתים שחורים",
    "זיתים ירוקים",
    "פטריות",
    "בצל",
    "עגבניות",
    "פלפל חריף",
    "פלפל מתוק",
    "אננס",
    "נקניק",
    "טונה",
    "תירס",
    "בולגרית",
    "פפרוני",
    "בייקון בקר",
    "בזיליקום",
    "חצילים",
    "פטריות שמפיניון",
    "עגבניות מיובשות",
    "שמן זית",
    "רוטב שום",
    "רוטב פסטו"
]

# בחירת תוספות
selected_toppings = st.multiselect("בחר תוספות:", toppings)

# כפתור להכנת הפיצה
if st.button("אפה את הפיצה!"):
    if selected_toppings:
        st.success(f"🍕 פיצה מוכנה! עם: {', '.join(selected_toppings)} 🔥")
    else:
        st.warning("לא בחרת תוספות... מכין פיצה בסיסית 🍕")

# תמונה
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg",
    width=300
)
