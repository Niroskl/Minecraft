import streamlit as st

st.set_page_config(page_title="🎬 הופעה חמודה", layout="centered")
st.title("🎬 ברוכים הבאים!")

# בקשת שם המשתמש
name = st.text_input("מה שמך?")

# הצגת ברכה וסרטון
if name:
    st.subheader(f"ברוך הבא להופעה שלנו, {name}! מקווים שתהנה!")
    
    # פתיחת הסרטון לפי הנתיב המלא
    video_path = r"C:\Users\user\Downloads\SuperX.mp4"
    video_file = open(video_path, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
