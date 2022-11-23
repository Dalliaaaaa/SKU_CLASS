import time
import random

class Box():
    def __init__(self, attack, hp, band):
        self.attack = attack
        self.hp = hp
        self.band = band

    def box_1(self):
        print("\n앞에 보물상자가 있습니다!")
        weapon = random.choice(["검(Normal)", "활(Unique)", "창(Legend)"])
        print(f"\n당신은 {weapon}을 얻었습니다!")
        time.sleep(2)
        if weapon == "검(Normal)":
            self.attack += 5
            print("\n당신은 5의 공격력을 얻었습니다")
        elif weapon == "활(Unique)":
            self.attack += 10
            print("\n당신은 10의 공격력을 얻었습니다")
        elif weapon == "창(Legend)":
            self.attack += 20
            print("\n당신은 20의 공격력을 얻었습니다")

    def box_2(self):
        print("\n앞에 보물상자가 있습니다!")
        weapon = random.choice(["장갑(Normal)", "투구(Unique)", "방탄복(Legend)"])
        print(f"\n당신은 {weapon}을 얻었습니다!")
        time.sleep(2)
        if weapon == "장갑(Normal)":
            self.hp += 10
            print("\n당신은 10의 방어력(체력)을 얻었습니다")
        elif weapon == "투구(Unique)":
            self.hp += 20
            print("\n당신은 20의 방어력(체력)을 얻었습니다")
        elif weapon == "방탄복(Legend)":
            self.hp += 30
            print("\n당신은 30의 방어력(체력)을 얻었습니다")

    def box_3(self):
        print("\n앞에 보물상자가 있습니다!")
        weapon = random.choice(["붕대2개(Normal)", "붕대4개(Unique)", "붕대6개(Legend)"])
        print(f"\n당신은 {weapon}를 얻었습니다!")
        time.sleep(2)
        if weapon == "붕대2개(Normal)":
            self.band += 2
        elif weapon == "붕대4개(Unique)":
            self.band += 4
        elif weapon == "붕대6개(Legend)":
            self.band += 6

    
