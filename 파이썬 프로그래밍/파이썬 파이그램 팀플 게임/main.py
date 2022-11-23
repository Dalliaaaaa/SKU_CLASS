import random
import time
from characters import Player, Boss
from items import Box
from ending import Ending  
from random import randint

global hp
hp = 100
global band
band = 0

#===========================   메인  코드   ===========================
print("\n            눈을 떠보니 당신은 처음 보는 공간에 와있습니다.")
time.sleep(1)
print("              어두워서 으스스한 분위기가 감돌고 있습니다.\n")
time.sleep(1)

# ===========================캐릭터 이름 설정===========================
while 1:
    print("======================플레이어 이름을 입력하세요======================\n")
    name = input("플레이어의 이름: ")
    end = Ending(name)
    attack = random.randrange(5,15+1)
    pl_1 = Player(name, attack, hp, band)
    print("\n정말 ", pl_1.name ,"(으)로 결정하셨습니까? : 1 = 네, 2 = 아니오")
    B = input("입력: ")
    if B == "1":
        print("\n결정되었습니다.\n")
        break
    elif B == "2":
        continue

pl_2 = Player

print("\n살인마: {}, 당신은 납치되어 이곳에 갇혀있습니다.".format(pl_1.name))
print("          저와의 게임에서 승리하여 탈출하십시오.\n")       
time.sleep(1)
pl_1.status()
pl_2.moving_1()

# ===========================첫 번째 미니게임===========================

print("===========================게임을 진행합니다===========================\n") 
print('                   첫번째 게임은 업다운 게임 입니다.\n')
time.sleep(1)
print('살인마: 1~99 중 생각한 숫자를 맞출 때 3번의 기회 이후부터는 공격을 합니다.\n')
time.sleep(1)

#hp1 = pl.hp# 체력 저장

number = random.randrange(1,100+1)

for _ in range(3): #피 깎이지 않는 세번의 기회
    guess = input("생각한 숫자를 맞추세요 (1 ~ 99): ") #플레이어가 유추한 숫자 적는 란
    if number == int(guess):
        print("생각한 숫자가 맞습니다. 다음 게임으로 넘어가겠습니다.")
        res = 0
        break
    elif number > int(guess):
        print("틀렸습니다. 생각한 숫자는 더 큰 숫자 입니다.\n")
        res = 2
    else:
        print("틀렸습니다. 생각한 숫자는 더 작은 숫자 입니다.\n")
        res = 2

if (res == 2): # 세번 안에 못 맞추면 체력이 감소되며 게임실행
    print("\t이제부터 못 맞출 시 체력이 감소합니다\n")
    while 1: #게임이 맞추는 기회
        guess = input('생각한 숫자를 맞추세요 (1 ~ 99): ') #플레이어가 유추한 숫자 적는 란
        if number == int(guess):
            print('\n생각한 숫자가 맞습니다. 다음 게임으로 넘어가겠습니다.\n')
            break
        elif number > int(guess):
            print('틀렸습니다. 생각한 숫자는 더 큰 숫자입니다.\n')
            pl_1.dmg(1,3+1)
            if pl_1.hp <= 0:
                end.bad()
        else:
            print('틀렸습니다. 생각한 숫자는 더 작은 숫자입니다.\n')
            pl_1.dmg(1,3+1)
            if pl_1.hp <= 0:
                end.bad()

print(f"\n남은 체력: {pl_1.hp}")
time.sleep(1)

b = Box(pl_1.attack, pl_1.hp, pl_1.band)

b.box_1()
pl_1.attack = b.attack
pl_1.status()
pl_2.moving_2()

#===========================두 번째 게임진행===========================

print('                  두 번째 게임은 영어 단어 맞추기 게임 입니다.')
time.sleep(1)
print("\n       총 5개의 영어 단어를 맞추는 동안 살아남는다면 게임을 클리어 합니다.\n")
time.sleep(1)

words = ["lion" , "apple", "minute", "country", "person", "fire", "adventure", "project", "math", "animal", "killer", "code", "choco", "class", "manner", "perfume", "delicious", "name"]
random_word = random.shuffle(words)

correct = 0 # 영어단어 맞춘 개수 

iChoice = -1 # 5문제 전부 나오면 함수 종료하는 변수

def make_random(word):
    global shuffled_word
    charaters = list(word)
    random.shuffle(charaters)
    shuffled_word = ''.join(charaters)
    if shuffled_word in words:
        make_random(word)

while iChoice:
    for x in words[0:5]:
        make_random(x)

        english = input("{}의 원래 영어 단어를 알아 맞추세요 : ".format(shuffled_word))

        if english == x:
            print("원래 영어 단어가 맞습니다.\n")
            correct += 1
        else:
            print("원래 영어 단어가 아닙니다.")
            print(f"\n정답은 {x}이었습니다.")
            pl_1.dmg(1,10)
            if pl_1.hp <= 0:
                break
        
    if pl_1.hp <= 0:
        end.bad()
    if pl_1.hp > 0:
        iChoice=0

print(f"\n총 {correct}개의 문제를 맞추셨습니다.")
time.sleep(1)

b.hp = pl_1.hp
b.box_2()
pl_1.hp = b.hp
pl_1.status()
pl_2.moving_2()

#===========================세 번째 게임 진행===========================

print('\n                  세 번째 게임은 가위바위보 게임 입니다.')
time.sleep(1)
print("\n           총 3번의 가위바위보를 승리하기 전까지 살아남으세요.\n")
time.sleep(1)

while 1:

    RSP = ['가위', '바위', '보']
    RSP_player = input("가위 바위 보 중 하나를 입력하세요: ")
    computer = randint(0,2)

    if RSP_player == "가위" or RSP_player == "바위" or RSP_player == "보":
        # player이 입력한 가위 바위 보를 숫자로 바꾼 다음, 컴퓨터와 비교하자
        for x in range(0,len(RSP)):  # RSP 길이 만큼 x 를 돌려 가면서 비교
            if RSP[x] == RSP_player:  # x 번째 리스트가 입력과 같으면
                RSP_player = x  # RSP_player을 숫자로 바꿔준다.
                break

        print(f"\n살인자는 {RSP[computer]}를 냈습니다.")
        time.sleep(1)
        print(f"{str(pl_1.name)}는 {RSP[RSP_player]}를 냈습니다.")
        time.sleep(1)
        print()

        if RSP_player == computer:
            print("무승부")
            pl_1.dmg(1,3+1)
            if pl_1.hp <= 0:
                end.bad()

        elif (RSP_player==0 and computer == 2) or (RSP_player - computer == 1):
            pl_1.mini3_sub()

        else :
            print("살인마 승리")
            pl_1.dmg(1,5+1)
            if pl_1.hp <= 0:
                end.bad()

        if pl_1.count3 == 3:
            break
    else:
        continue

print(f"\t남은 체력: {pl_1.hp}")
time.sleep(1)

b.hp = pl_1.hp
b.box_3()
pl_1.band = b.band
pl_1.status()
pl_2.moving_2()

# ===========================마지막 방===========================
bs = Boss()

time.sleep(1)
print("\n                  당신은 한 방 앞에 도착했습니다..")
time.sleep(1)
print("\n           방을 들어선 순간, 당신은 살인마를 마주했습니다.")
time.sleep(1)
print("\n1 = 도망친다, 2 = 싸운다")
print("(1. 도망친다를 선책하시면 체력은 40으로 끝이 납니다.)\n")
answer = int(input('입력: '))
while 1:
    if answer == 1:# 반드시 노멀 엔딩
        print("\n               당신은 낯선 공간에서 탈출하였습니다. END")
        bs.bshp = 0
        pl_1.hp = 40
        break
    elif answer == 2:# 배드, 새드, 노말, 트루 엔딩
        print("\n살인마와 싸워서 승리하십시오!")
        bs.bstatus()
        time.sleep(1)
        while 1:
            print('행동을 선택하세요: 1 = 공격, 2 = 붕대 사용, 3 = 도망')
            player = int(input('입력: '))
            boss = random.choice(['공격' , '칼던지기' , '빗나감'])
            if player == 1 or player == "공격":
                bs.bossdmg(pl_1.attack)
                if bs.bshp <= 0:
                    break
            elif player == 2 or player == "붕대 사용":
                if pl_1.band > 0:
                    pl_1.healplayer()
                else:
                    print("\n붕대를 다 사용했습니다!")
            elif player == 3 or player =="도망친다":
                print("\n 살인마의 체력이 낮을수록 도망치기 쉬워진다!")
                run = random.random()# 0과 1사이의 수 무작위 생성
                if run + (1 - bs.bshp/100) >= 1:# 보스 체력이 낮을수록 도주 확률 업
                    print(f"\n간신히 도망쳤다...")
                    break
                else:
                    print("\n도망에 실패했다!")
            else:
                continue

            time.sleep(1)
            print(f'\n살인마의 공격이 시작됩니다.')
            time.sleep(1)

            if boss == '공격':
                pl_1.playerdmg(bs.battack)
                if pl_1.hp <=0:
                    end.bad()
            elif boss == '칼던지기':
                print("살인마가 칼을 던졌습니다!\n")
                pl_1.playerdmg(bs.battack + 5)
                if pl_1.hp <=0:
                    end.bad()
            elif boss == '빗나감':
                print ("살인마의 공격이 당신을 빗겨나갔습니다...\n\n")
        break
    else:
        continue

#===========================엔딩===========================

print(f"\t\t\t  남은 체력: {pl_1.hp}\n")
time.sleep(1)
print("===========================  엔   딩  ===========================\n\n")
time.sleep(1)

if pl_1.hp >= 70:
    end.true()
elif pl_1.hp >= 20:
    end.normal()
elif pl_1.hp > 0:
    end.sad()
else:
    end.bad()