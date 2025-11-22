import streamlit as st

st.set_page_config(page_title="🎬 הופעה חמודה", layout="centered")
st.title("🎬 ברוכים הבאים!")

name = st.text_input("מה שמך?")

if name:
    st.subheader(f"ברוך הבא להופעה שלנו, {name}! מקווים שתהנה!")
    
    video_path = "SuperX.mp4"  # הסרטון בתיקייה של הקוד

    video_html = f"""
    <video width="640" autoplay controls>
        <source src="{video_path}" type="video/mp4">
        הדפדפן שלך אינו תומך בוידאו.
    </video>
    """

    st.markdown(video_html, unsafe_allow_html=True)
