import random
import time
from player import Player
from random import randint

# 전역변수 체력,체력1,카운트 
# Player = player.Player()
# global hp1
# hp1=player.hp
global count3
count3 = 0

#----------------------------------------
def mini3_sub(): # 함수: 미니게임3 캐릭터 승리
    global count3
    print(f"\n{player.name} 승리") 
    count3 += 1  
    print(f"\n 지금까지 {count3}번 이겼습니다.")

#===========================함수: 캐릭터 체력 감소===========================
def dmg():
    damage = random.randrange(1, 5)
    player.hp -= damage
    print(f"\n살인마에게 공격당하였습니다!!")
    print(f"\n -{damage}")
    print(f"\n남은 체력 = {player.hp}\n")

#===========================메인 코드===========================
print("\n       눈을 떠보니 당신은 처음 보는 공간에 와있습니다.")
time.sleep(1)
print("         어두워서 으스스한 분위기가 감돌고 있습니다.\n")
time.sleep(1)

# ===========================캐릭터 이름 설정===========================
while 1:
    print("---------------플레이어 이름을 입력하세요---------------\n")
    player = Player()
    print("정말 ", str(player.name) ,"(으)로 결정하셨습니까? : 1 = 네, 2 = 아니오\n")
    B = input("입력: ")
    if B == "1":
        print("         결정되었습니다.\n")
        break
    elif B == "2":
        continue
print("         플레이어의 닉네임은 ", str(player.name),"입니다.\n")

print("\n살인마: {}, 당신은 납치되어 이곳에 갇혀있습니다.".format(player.name))
print("          저와의 게임에서 승리하여 탈출하십시오.\n")       
time.sleep(2)
print(f"\n                 남은 체력 = {player.hp}\n")
input("                 엔터하면 넘어갑니다..")
print("\n")
 
#===========================첫 번째 미니게임===========================

print("======================첫번째 게임을 진행합니다======================\n") 
time.sleep(1)
print('                  첫번째 게임은 업다운 게임 입니다.')
print('살인마: 1~99 중 생각한 숫자를 맞출 때 3번의 기회 이후부터는 공격을 합니다.\n')
time.sleep(1)

hp1 = player.hp# 체력 저장

number = random.randrange(1,100)

#세 번 안에 맞추면 피가 감소되지 않음
#그 이후로는 피가 2씩 감소함
for _ in range(3): #피 깎이지 않는 세번의 기회
    guess = input('생각한 숫자를 맞추세요 (1 ~ 99): ') #플레이어가 유추한 숫자 적는 란
    if number == int(guess):
        print('생각한 숫자가 맞습니다. 다음 게임으로 넘어가겠습니다.')
        res = 0
        break
    elif number > int(guess):
        print('틀렸습니다. 생각한 숫자는 더 큰 숫자 입니다.\n')
        res = 2
    else:
        print('틀렸습니다. 생각한 숫자는 더 작은 숫자 입니다.\n')
        res = 2

print("\n")
if (res == 2): # 세번 안에 못 맞추면 체력이 감소되며 게임실행
    print("이제부터 못 맞출 시 체력이 감소합니다")
    while 1: #게임이 맞추는 기회
        guess = input('생각한 숫자를 맞추세요 (1 ~ 99): ') #플레이어가 유추한 숫자 적는 란
        if number == int(guess):
            print('\n생각한 숫자가 맞습니다. 다음 게임으로 넘어가겠습니다.\n')
            break
        elif number > int(guess):
            print('틀렸습니다. 생각한 숫자는 더 큰 숫자입니다.\n')
            dmg()
            if player.hp <= 0:
                player.die()
        else:
            print('틀렸습니다. 생각한 숫자는 더 작은 숫자입니다.\n')
            dmg()
            if player.hp <= 0:
                player.die()


print(f"\n남은 체력 = {player.hp}")
time.sleep(1)
Player.moving()
time.sleep(1)

#===========================두 번째 게임진행===========================

print("======================두 번째 게임을 진행합니다======================\n") 
time.sleep(1)
print('         두 번째 게임은 영단어 맞추기 게임 입니다.')
time.sleep(1)
print("\n 총 5개의 영어 단어를 맞추는 동안 살아남는다면 게임을 클리어 합니다.\n")
time.sleep(1)

words = ["lion" , "apple", "game", "zoo", "sun"]
correct = 0# 영어단어 맞춘 개수 

iChoice = -1# 5문제 전부 나오면 함수 종료하는 변수

while iChoice:
    for word in words:
        charaters = list(word)
        random.shuffle(charaters)
        shuffled_word = ''.join(charaters)

        english = input("{}의 원래 영어 단어를 알아 맞추세요 : ".format(shuffled_word))

        if english == word:
            print("원래 영어 단어가 맞습니다.\n")
            correct += 1
        else:
            print("원래 영어 단어가 아닙니다.")
            print(f"\n정답은 {word}이었습니다.")
            dmg()
            if player.hp <= 0:
                break
        
    if player.hp <= 0:
        player.die()
    if player.hp > 0:
        iChoice=0

print(f"\n총 {correct}개의 문제를 맞추셨습니다.")
print('살아남으셨습니다. 다음 게임으로 넘어가겠습니다.')
time.sleep(1)
print(f"\n남은 체력 = {player.hp}")
time.sleep(1)

Player.moving()

#===========================세 번째 게임 진행===========================

print("---------------세 번째 게임을 진행합니다---------------\n") 
time.sleep(1)
print('\n         세 번째 게임은 가위바위보 게임 입니다.')
time.sleep(1)
print("\n 총 5번의 가위바위보를 승리하기 전까지 살아남으세요")
time.sleep(1)


while 1:

    RSP = ['가위', '바위', '보']
    RSP_player = input("가위 바위 보 중 하나를 입력하세요: ")
    computer = randint(0,2)

    # player이 입력한 가위 바위 보를 숫자로 바꾼 다음, 컴퓨터와 비교하자
    for x in range(0,len(RSP)):  # RSP 길이 만큼 x 를 돌려 가면서 비교
        if RSP[x] == RSP_player:  # x 번째 리스트가 입력과 같으면
            RSP_player = x  # RSP_player을 숫자로 바꿔준다.
            break

    print(f"\n살인자는 {RSP[computer]}를 냈습니다.")
    print(f"\n {str(player.name)}는 {RSP[RSP_player]}를 냈습니다.")

    if RSP_player == computer:
        print("무승부")
        dmg()
        if player.hp <= 0:
            Player.die()

    elif (RSP_player==0 and computer == 2) or (RSP_player - computer == 1):
        mini3_sub()

    else :
        print("살인마 승리")
        dmg()
        if player.hp <= 0:
            Player.die()

    if count3 == 5:
        break
