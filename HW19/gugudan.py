import random # 구구단 숫자 랜덤으로 뽑기

def gugudan_correct():
    a = random.randint(2, 9) # a에 2~9까지 숫자 중 하나를 랜덤으로 넣기
    b = random.randint(1, 9) # b에 1~9까지 숫자 중 하나를 랜덤으로 넣기
    ans = input(f"{a} x {b} =>> ?")

    return int(ans) == a*b


def main():
    score = 0
    for i in range(10): # 구구단 10문제
        if gugudan_correct():
            score += 10

    print(f"총 10문제 중 {score / 10:.0f}개 맞추었습니다.") # 개수 구하기
    print(f"따라서 총 점수는 {score}점 입니다.")


if __name__ == "__main__":
    main()