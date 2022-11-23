import time

class Ending:
    def __init__(self, name) :
        self.name = name

    def true(self):
        print(f"""
        {self.name}(은)는 탈출에 성공했습니다.
        """)
        time.sleep(1)
        print(f"""
        거의 다치지 않은 채로 탈출하여 바로 경찰서에 
        찾아가 신고를 합니다.
        곧바로 경찰은 도주하던 살인마를 체포하고 전적
        이 있던 살인마는 얼마 후 감옥으로 잡혀갑니다.
        살인마가 감옥에서 평생 살게 된다는 소식을 접한
        {self.name}(은)는 안심하고 평범한 생활 속으로 
        돌아가 지낼 수 있게 됩니다. 
        \n\n""")
        input("                    엔터하면 게임이 종료됩니다..")

    def normal(self):
        print(f"""
        {self.name}(은)는 탈출에 성공했습니다.
        """)
        time.sleep(1)
        print(f"""
        곧바로 경찰서로 뛰어갔지만, 이내 지쳐 정신을 
        잃어 쓰러집니다.
        병원에서 깨어난 {self.name}(은)는 치료받아 회복하
        지만 잘 때마다 납치당할 수 있다는 불안감에
        쉽게 잠들지 못하고 가끔 악몽을 꾸게 됩니다.
        """)
        time.sleep(1)
        print(f"""
        {self.name}(은)는 언젠가 이 악몽이 끝나기를 기
        다릴 뿐입니다..
        \n\n""")
        input("                    엔터하면 게임이 종료됩니다..")

    def sad(self):
        print(f"""
        {self.name}(은)는 탈출에 성공합니다.
        """)
        time.sleep(1)
        print(f"""
        탈출한 지 얼마 지나지 않아 알 수 없는 곳에서 쓰
        러지고 병원으로 이송됩니다.
        공격을 많이 받아 병원에서도 치료하기가 어려웠지
        만 {self.name}(은)는 기적적으로 살았습니다. 
        수술이 끝난 후에도 몸이 회복되지 않아 병원에서 
        지내게 되고 정신적인 후유증에 시달려 일상 생활
        이 불가능해졌습니다.
        """)
        print(f"""
        그 사건 이후 {self.name}(은)는 병원에서 생을 보
        내다 마감하게 됩니다.
        \n\n""")
        input("                    엔터하면 게임이 종료됩니다..")   
    
    def bad(self):
        print(f"\n======================  GAME OVER  ======================")
        time.sleep(1)
        print(f"""\n
        살인마의 공격으로 눈앞이 깜깜해졌다...
        """)
        time.sleep(1)
        print(f"""
        {self.name}(은)는 게임에서 탈출하지 못하고 결국
        살인마에게 살인 당합니다.
        """)
        input("                    엔터하면 게임이 종료됩니다..")   
        exit()