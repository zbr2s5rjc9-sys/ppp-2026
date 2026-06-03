def toggle(alphabet):
    if ord(alphabet) >= 65 and ord(alphabet) <= 90:
        return chr(ord(alphabet) + 32)  #글자로 바꿈

    if ord(alphabet) >= 97 and ord(alphabet) <= 122:  #대문자에 32를 더하면 소문자가 됨
        return chr(ord(alphabet) - 32)

    return alphabet


def toggle_text(text: str) -> str: # 이 함수는 문자열을 반환한다!
        result = ""
        for c in text:
            result += toggle(c)
        # result = result + toggle(c)

        return result


def main():
    text = input("영어를 입력하세요 : ")
    print(toggle_text(text))


if __name__ == "__main__":
    main()