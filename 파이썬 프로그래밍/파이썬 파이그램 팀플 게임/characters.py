import time
import random

class Player:
    # 플레이어의 이름 및 체력, 공격력 초기화
    def __init__(self, name, attack, hp, band) :
        self.name = name
        self.hp = hp
        self.attack = attack
        self.band = band
        self.count3 = 0
        
    # 플레이어의 상태
    def status(self) :
            print(f""" 
            [스테이터스]
            이름 : {self.name}
            공격력 : {self.attack}
            체력 : {self.hp}
            붕대 : {self.band}개\n""")
            input("                    엔터하면 다음 방으로 넘어갑니다..")

    # 플레이어의 이동
    def moving_1():
        print("\n게임방으로 이동 중입니다...")
        t = 3
        while t >= 1:
            time.sleep(1)
            print(f"{t}..")
            t -= 1
        print()

    def moving_2():
        print("\n다음 게임방으로 이동 중입니다...")
        t = 3
        while t >= 1:
            time.sleep(1)
            print(f"{t}..")
            t -= 1
        print()
    
    # 플레이어의 데미지
    def dmg(self, a, b):
        damage = random.randrange(a, b)
        self.hp -= damage
        print(f"\n살인마에게 공격당하였습니다!!")
        print(f"\n-{damage}")
        print(f"\n남은 체력: {self.hp}\n")

    # 캐릭터 체력 감소
    def playerdmg(self, var):# 함수: 보스와의 전투에서 캐릭터 체력 감소
        damage = random.randrange(var-5,var+5+1) #기본공격력 무작위 데미지
        self.hp -= damage
        print(f"살인마의 공격이 당신에게 적중했습니다..")
        time.sleep(1)
        print(f"\n-{damage}")
        time.sleep(1)
        print(f"\n플레이어 체력: {self.hp}\n")

    # 함수: 미니게임3 캐릭터 승리
    def mini3_sub(self):
        print(f"{self.name} 승리") 
        self.count3 += 1  
        print(f"\n지금까지 {self.count3}번 이겼습니다.\n\n")

    # 플레이어의 hp를 회복
    def healplayer(self): 
        self.band -= 1
        heal = random.randrange(5,30+1)
        self.hp  += heal
        print(f"\n당신은 붕대를 사용했습니다 ")
        time.sleep(1)
        print(f"당신은 {heal}만큼의 체력를 회복했습니다.. ")
        time.sleep(1)
        print(f"\n 남은 붕대 수 = {self.band} ")
        time.sleep(1)

class Boss:
    # 살인마의 체력, 공격력 초기화
    def __init__(self) :
        self.bshp = 100
        self.battack = random.randrange(10,20+1)

    # 살인마의 체럭 감소
    def bossdmg(self, var):# 함수: 살인마와의 전투에서 살인마 체력 감소
        damage = random.randrange(var-5,var+5+1)#기본공격력 무작위 데미지
        self.bshp -= damage
        print(f"\n당신의 공격이 살인마에게 적중했습니다.")
        time.sleep(1)
        print(f"\n-{damage}")
        time.sleep(1)
        if self.bshp <= 0:
            self.bshp = 0
        print(f"\n살인마 체력: {self.bshp}\n")   

    # 살인마의 상태
    def bstatus(self):
        print(f""" 
            [살인마 스테이터스]
            공격력: {self.battack}
            체력: {self.bshp}\n""")
        input("                 엔터하면 넘어갑니다..\n")