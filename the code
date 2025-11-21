import pygame
import sys

# ========================
# הגדרות בסיסיות
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minecraft Presentation")

# צבעים
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE = (64, 224, 208)

# פונטים בסגנון Minecraft
try:
    font = pygame.font.Font("Minecraft.ttf", 36)
except:
    font = pygame.font.SysFont("Arial", 36)

# ========================
# רשימת שקופיות ארוכה על Minecraft
slides = [
    "ברוכים הבאים למצגת על Minecraft!",
    "Minecraft הוא משחק וידאו פופולרי שיצא בשנת 2011.",
    "השחקנים חוקרים עולם פתוח ומבנים בסגנון Sandbox.",
    "ניתן לשחק במצב Survival או Creative.",
    "ב-Survival השחקנים צריכים לאסוף משאבים ולשרוד.",
    "ב-Creative יש לכל שחקן כל המשאבים והחופש לבנות.",
    "Minecraft מאפשר משחק יחיד או מול חברים ברשת.",
    "למשחק יש גרפיקה פיקסלית מזוהה עם בלוקים.",
    "יש חיות, מפלצות, כפרים, ומאגרי משאבים.",
    "המשחק תומך במודים שמוסיפים יכולות חדשות.",
    "Minecraft הוא אחד המשחקים הנמכרים ביותר בעולם.",
    "סיום: תודה על הצפייה במצגת Minecraft!"
]

current_slide = 0

# ========================
# לולאת מצגת
running = True
while running:
    screen.fill(TURQUOISE)  # רקע טורקיז
    
    # טקסט של השקופית
    text_lines = slides[current_slide].split("\n")
    for i, line in enumerate(text_lines):
        text = font.render(line, True, WHITE)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 + i*50))
        screen.blit(text, text_rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # חץ ימינה -> שקופית הבאה
                current_slide = (current_slide + 1) % len(slides)
            elif event.key == pygame.K_LEFT:  # חץ שמאלה -> שקופית קודמת
                current_slide = (current_slide - 1) % len(slides)

pygame.quit()
sys.exit()
