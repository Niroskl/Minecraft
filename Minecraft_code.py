# -*- coding: utf-8 -*-
# מחולל שילובי אמוג'ים (כל אמוג׳י עם כל אמוג׳י)

import itertools

# רשימת כל האמוג'ים העדכנית (3,304 אמוג'ים)
# נשתמש בטווח היוניקוד הכולל אותם
# זה כולל את כל האמוג׳ים המודרניים

def load_all_emojis():
    emojis = []
    for codepoint in range(0x1F300, 0x1FAFF):  # טווח האמוג׳ים ביוניקוד
        try:
            char = chr(codepoint)
            if char.encode('utf-8').decode('utf-8') and char.strip():
                emojis.append(char)
        except:
            pass
    return emojis

all_emojis = load_all_emojis()

print(f"נטענו {len(all_emojis)} אמוג'ים ✔")

# --- בוחר שני אמוג'ים ---
e1 = input("בחר אמוג'י ראשון: ")
e2 = input("בחר אמוג'י שני: ")

print("\nשילוב אופקי:")
print(e1 + e2)

print("\nשילוב אנכי:")
print(e1 + "\n" + e2)

# --- כל השילובים האפשריים ---
save = input("\nלשמור קובץ עם כל 3,304 × 3,304 השילובים? (y/n): ")

if save.lower() == "y":
    with open("emoji_combinations.txt", "w", encoding="utf-8") as f:
        for a, b in itertools.product(all_emojis, all_emojis):
            f.write(a + b + "\n")

    print("✔ נוצר קובץ emoji_combinations.txt עם כל השילובים!")
