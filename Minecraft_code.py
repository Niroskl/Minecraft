import streamlit as st

st.set_page_config(page_title="🎬 הופעה חמודה", layout="centered")
st.title("🎬 ברוכים הבאים!")

# הוספת CSS לרקע Roblox
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.imgur.com/3zVb9rI.png');  /* ניתן להחליף כל URL של תמונת Roblox */
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# בקשת שם המשתמש
name = st.text_input("מה שמך?")

# הצגת ברכה וסרטון
if name:
    st.subheader(f"ברוך הבא להופעה שלנו, {name}! מקווים שתהנה!")

    # סרטון עם autoplay (ללא סאונד כדי להפעיל אוטומטית בדפדפן)
    video_path = "SuperX.mp4"
    video_html = f"""
    <video width="640" autoplay muted controls>
        <source src="{video_path}" type="video/mp4">
        הדפדפן שלך אינו תומך בוידאו.
    </video>
    """
    st.markdown(video_html, unsafe_allow_html=True)
