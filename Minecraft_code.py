import streamlit as st

st.set_page_config(page_title="MiniCraft 2D Streamlit", layout="wide")
st.title("🟫 MiniCraft 2D - מזויף")

# ----------- הגדרות סביבה ----------
GRID_WIDTH = 10
GRID_HEIGHT = 10
CELL_SIZE = 50  # פיקסלים, רק לציור

# שמירת מצב המשחק
if "player_pos" not in st.session_state:
    st.session_state.player_pos = [0, GRID_HEIGHT-1]  # התחלה בתחתית השמאלית
if "blocks" not in st.session_state:
    st.session_state.blocks = []

player_x, player_y = st.session_state.player_pos

# ----------- פונקציות עזר ----------
def draw_grid():
    for y in range(GRID_HEIGHT):
        cols = []
        for x in range(GRID_WIDTH):
            if [x, y] == st.session_state.player_pos:
                cols.append("🧍")  # השחקן
            elif [x, y] in st.session_state.blocks:
                cols.append("🟫")  # בלוק
            else:
                cols.append("🟦")  # שמיים/רקע
        st.write("".join(cols))

# ----------- כפתורי ניווט ----------
st.subheader("זוז עם הכפתורים או הוסף בלוק")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️"):
        if st.session_state.player_pos[0] > 0:
            st.session_state.player_pos[0] -= 1
with col2:
    if st.button("⬆️"):
        if st.session_state.player_pos[1] > 0:
            st.session_state.player_pos[1] -= 1
with col3:
    if st.button("➡️"):
        if st.session_state.player_pos[0] < GRID_WIDTH-1:
            st.session_state.player_pos[0] += 1
if st.button("⬇️"):
    if st.session_state.player_pos[1] < GRID_HEIGHT-1:
        st.session_state.player_pos[1] += 1

# כפתור להוספת בלוק במקום השחקן
if st.button("🟫 הוסף בלוק כאן"):
    if st.session_state.player_pos not in st.session_state.blocks:
        st.session_state.blocks.append(st.session_state.player_pos.copy())

# ----------- ציור הרשת ----------
draw_grid()
