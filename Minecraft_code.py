import streamlit as st

st.set_page_config(page_title="🎬 הופעה חמודה", layout="centered")
st.title("🎬 ברוכים הבאים!")

# בקשת שם המשתמש
name = st.text_input("מה שמך?")

# הצגת ברכה וסרטון
if name:
    st.subheader(f"ברוך הבא להופעה שלנו, {name}! מקווים שתהנה!")
    
    # פתיחת הסרטון מתוך התיקייה ביחס לקוד
    video_file = open("SuperX.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
