import pygame
import sys

pygame.init()

# ----------- הגדרות מסך ----------
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🍳 משחק בישול אינטראקטיבי 2D")

# ----------- צבעים ----------
WHITE = (255, 255, 255)
TURQUOISE = (64, 224, 208)
BLACK = (0,0,0)

# ----------- טקסטים ----------
font = pygame.font.SysFont(None, 40)
def draw_text(text, x, y, color=BLACK):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# ----------- מרכיבים על המסך ----------
ingredients = [
    {"name": "ביצה", "rect": pygame.Rect(50, 50, 100, 50)},
    {"name": "קמח", "rect": pygame.Rect(50, 120, 100, 50)},
    {"name": "חלב", "rect": pygame.Rect(50, 190, 100, 50)},
]

bowl = pygame.Rect(600, 400, 150, 100)
bowl_contents = []

dragging = None

# ----------- לולאת המשחק ----------
running = True
while running:
    screen.fill(TURQUOISE)

    # ציור הקערה
    pygame.draw.ellipse(screen, WHITE, bowl)
    draw_text("קערה", bowl.x+30, bowl.y+35)

    # ציור המרכיבים
    for ing in ingredients:
        pygame.draw.rect(screen, WHITE, ing["rect"])
        draw_text(ing["name"], ing["rect"].x+10, ing["rect"].y+10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # התחלת גרירה
        if event.type == pygame.MOUSEBUTTONDOWN:
            for ing in ingredients:
                if ing["rect"].collidepoint(event.pos):
                    dragging = ing
                    mouse_x, mouse_y = event.pos
                    offset_x = ing["rect"].x - mouse_x
                    offset_y = ing["rect"].y - mouse_y

        # גרירה בפועל
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                dragging["rect"].x = mouse_x + offset_x
                dragging["rect"].y = mouse_y + offset_y

        # שחרור גרירה
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                if bowl.colliderect(dragging["rect"]):
                    bowl_contents.append(dragging["name"])
                    # החזרת המרכיב למקומו המקורי
                    dragging["rect"].x, dragging["rect"].y = 50, 50 + ingredients.index(dragging)*70
                dragging = None

    # הצגת תוכן הקערה
    draw_text("תוכן הקערה: " + ", ".join(bowl_contents), 300, 500)

    pygame.display.flip()

pygame.quit()
sys.exit()
