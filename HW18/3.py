import random

def initial_game():
    words = ["프원실", "전북대학교", "요거트", "아메리카노", "토마토", "시험"]
    answer = random.choice(words)
    #print(answer)

    chosung = ['ㄱ','ㄲ','ㄴ','ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
               'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    hint = "" # 초성 힌트 제시

    for chr in answer: # 문자열 안 글자를 하나씩 커내서 출력하라는 거
        code = ord(chr) - ord('가') # "가"를 기준으로 몇 번째 한글인지 계산
        chos = code // 588
        hint += chosung[chos]
        # ①의 값을 (21 x 28)로 나눈 몫은 초성,
        # ①의 값을 (21 x 28)로 나눈 나머지를 28로 나눈 몫은 중성,
        # ①의 값을 28로 나눈 나머지는 종성

    print(hint)

    return answer

def main():
    answer = initial_game()
    game_start = input("정답 입력 : ")

    if game_start == answer:
        print("정답입니다!")

    else:
        print("오답입니다.")
        print(f"정답은 {answer}입니다!")


if __name__ == "__main__":
    main()