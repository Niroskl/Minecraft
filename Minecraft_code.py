import streamlit as st

st.title("🦄 גרור ושחרר תמונה של חד־קרן תינוק")

# CSS להסתיר את כפתור הבחירה
hide_file_uploader_style = """
<style>
div[data-baseweb="file-uploader"] > div:nth-child(2) {
    display: none;
}
</style>
"""
st.markdown(hide_file_uploader_style, unsafe_allow_html=True)

# file uploader שמקבל רק גרירה
uploaded_image = st.file_uploader("", type=["png", "jpg", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, width=320)
    st.success("🦄 התמונה נטענה בהצלחה!")
else:
    st.info("⬆️ גרור ושחרר תמונה בלבד")
