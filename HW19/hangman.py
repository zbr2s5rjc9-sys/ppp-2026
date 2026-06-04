import random


def hangman_game():
    words = ["orange", "apple", "yogurt", "egg", "jeonbuk", "pasta"]
    answer = random.choice(words)
    ba = ["_"] * len(answer)  # 단어 수 만큼 만들기

    trial = 7  # 목숨 7개

    while trial > 0:  # 기회가 남아있는 동안 게임 진행
        print("".join(ba), f"(trial = {trial})") # joint는 리스트 안의 문자들을 이어붙여라~

        ch = input("답을 입력하세요 : ")

        if ch in answer:  # 입력한 글자가 정답에 있으면

            for i in range(len(answer)): #for문은 같은 일을 정해진 횟수만큼 반복할 때 사용
                if answer[i] == ch:
                    ba[i] = ch  # 해당 위치에 글자 넣기

        else:
            print("틀렸습니다")
            trial -= 1  # 목숨 하나 삭제!

        if "".join(ba) == answer:
            print(f"{answer}!! 정답입니다!")
            break # 정답이니까 끝내

    if trial == 0:
        print(f"게임 종료! 정답 : {answer} ")

def main():
    hangman_game()


if __name__ == "__main__":
    main()