import pygame
import sys

# --------- הגדרות בסיסיות ----------
pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MiniCraft 2D - מזויף 😄")

# צבעים
SKY_BLUE = (135, 206, 235)
BROWN = (139, 69, 19)
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

# --------- הגדרות שחקן ----------
player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 50
player_speed = 5

# --------- בלוקים לסביבה ----------
block_size = 40
blocks = []  # רשימת בלוקים (x, y)
# דוגמה – קרקע ראשונית
for i in range(0, WIDTH, block_size):
    blocks.append((i, HEIGHT - block_size))

# --------- פונקציות עזר ----------
def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, player_size, player_size))

def draw_blocks():
    for bx, by in blocks:
        pygame.draw.rect(screen, BROWN, (bx, by, block_size, block_size))

# --------- לולאת המשחק ----------
running = True
while running:
    clock.tick(FPS)
    screen.fill(SKY_BLUE)  # רקע שמיים

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # יצירת בלוק חדש על ידי לחיצה על העכבר
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            # מיקום הבלוק לגריד
            bx = (mx // block_size) * block_size
            by = (my // block_size) * block_size
            blocks.append((bx, by))

    # --------- קלט מהמקלדת ----------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # --------- ציור ----------
    draw_blocks()
    draw_player(player_x, player_y)

    pygame.display.flip()
