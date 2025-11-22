import random
import time

class Player:
    def __init__(self):
        self.hp = 100
        self.attack_power = 15
        self.level = 1
        self.exp = 0

    def attack(self, enemy):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        print(f"אתה תוקף את האויב ועושה {damage} נזק!")
        enemy.hp -= damage
        if enemy.hp < 0:
            enemy.hp = 0

    def level_up(self):
        self.level += 1
        self.attack_power += 5
        self.hp += 20
        self.exp = 0
        print(f"\n🎉 מזל טוב! עלית לדרגה {self.level}!")
        print(f"כוח ההתקפה שלך עלה ל-{self.attack_power} ונקודות החיים שלך ל-{self.hp}!\n")

class Enemy:
    def __init__(self, level):
        self.level = level
        self.hp = 50 + level * 20
        self.attack_power = 10 + level * 5

    def attack(self, player):
        damage = random.randint(self.attack_power - 3, self.attack_power + 3)
        print(f"האויב תוקף ועושה לך {damage} נזק!")
        player.hp -= damage
        if player.hp < 0:
            player.hp = 0

def game():
    player = Player()
    print("ברוך הבא למשחק החזקקקק! 🦸‍♂️\n")
    while True:
        enemy = Enemy(player.level)
        print(f"פגשת אויב בדרגה {enemy.level} עם {enemy.hp} נקודות חיים.\n")
        while enemy.hp > 0 and player.hp > 0:
            action = input("בחר: (1) תוקף (2) מגן\n")
            if action == "1":
                player.attack(enemy)
            elif action == "2":
                print("אתה מגן על עצמך ומפחית נזק בפעם הבאה.")
                # הגנה מפחיתה נזק, נשמור את זה פשוט עכשיו
            else:
                print("בחר פעולה תקינה.")
                continue

            if enemy.hp > 0:
                enemy.attack(player)

            print(f"נקודות החיים שלך: {player.hp} | נקודות חיים של האויב: {enemy.hp}\n")
            time.sleep(1)

        if player.hp <= 0:
            print("אתה מת! המשחק נגמר.")
            break
        else:
            print("הרגת את האויב! אתה מקבל ניסיון.")
            player.exp += 50
            if player.exp >= 100:
                player.level_up()
            # מחזירים חיים חלקית אחרי קרב
            player.hp = min(player.hp + 30, 100 + (player.level - 1)*20)
            print(f"נקודות החיים שלך התחדשו ל-{player.hp}.\n")
            time.sleep(1)

if __name__ == "__main__":
    game()
