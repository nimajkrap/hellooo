
import random
print('게임 스타트')
# 오징어 게임 구슬 게임(홀짝 맞추기)
# 플레이어 구슬 20
p_gs = 20
# 컴퓨터 구슬20
c_gs = 20 
# 선을 정하기(랜덤하게)
print('오징어 게임에 오신 것을 환엽합니다.')
print('이번 게임은 홀짝입니다')
print('각 각 구슬은 20개씩 주어집니다')
print(f'플레이어 구슬: {p_gs}')
print(f'컴퓨터 구슬: {c_gs}')
# 구슬 갯수가 둘중에 하나라도 0이 되면 게임 종료
while True: # 무한 반복
    # 선물 정하기(랜덤하게)
    p = 1 # 플레이어
    c = 2 # 컴퓨터
    r = random.randrange(1,3) # 2명이라서 3으로
    r = 1 # 플레이어가 계속 선을 유지하기 위한 치트키
    # 정답 변수
    dab = "홀"
    print(r)
    if p == r:
        print('플레이어가 선')
        #사용자에게 플레이어의 구슬 갯수를 입력받게 만들기
        number = int(input("구슬 갯수를 입렵하세요: ")) #입력받은 문자를 숫자로 변경
        # 홀인지 짝인지 정답을 먼저 셋팅
        if number%2 == 0:
            p_dab = "짝"
        else:
            p_dab = "홀"
        print(f"플레이어 답: {dab}")
        # 컴퓨터가 가진 구슬의 갯수 중에 랜덤하게 배팅한다
        c_bat = random.randrange(1,c_gs + 1) # 컴퓨터가 가진 갯수 만큼 배팅
        print(f"컴퓨터가 배팅한 구슬: {c_bat}")
        # 컴퓨터가 정답을 맞출 차례
        c_dab = random.choice(['홀', '짝'])
        print(f"컴퓨터 답: {c_dab}")
        # 만약에 플레이어답과 컴퓨터답이 같으면 맞다. 아니면 틀렸다.
        if p_dab == c_dab:
            print('컴퓨터가 이겼다')
            # 내가 가진 구슬을 컴퓨터에게 준다
            # 내 구슬은 빠지고
            p_gs = p_gs - c_bat
            # 컴퓨터 구슬은 더해지고
            c_gs = c_gs + c_bat

        else:
            print('플레이어가 이겼다')
            # 위에거 거꾸로
            p_gs = p_gs + c_bat
            c_gs = c_gs - c_bat

        print(f"플레이어의 구슬 갯수: {p_gs}")
        print(f"컴퓨터의 구슬 갯수: {c_gs}")
        # 만약에 플레이어든 컴퓨터든 구슬 갯수가 0이 되면 게임 종료(무한 반복 break)
        if c_gs <= 0:
            print("컴퓨터 다이")
            break
        if p_gs <= 0:
            print("플레이어 다이")
            break


    else:
        print('컴퓨터가 선')

# 선이 정해졌으면 플레이어든 컴퓨터든 구슬 갯수를 지정 
# 구슬 갯수에 따라서 홀이냐 짝이냐가 정해질 것 같은데...
# 상대방이나 내가 정답을 맞추기(홀이냐 짝이냐)
# 맞추면 구슬 가져오기 상대는 구슬을 준다