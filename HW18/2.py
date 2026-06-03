def caesar_encode(text: str, shift: int = 3) -> str: # +3칸
    result = "" # 빈 문자열 만들기

    for c in text: # 문장에서 글자를 하나씩 꺼내기
        if "A" <= c <= "Z": # 대문자
            n = ord(c) + shift # 문자를 숫자로 바꾼 후 3 더하기
            if n > ord("Z"):
                n -= 26 # 알파벳은 총 26개이므로

            result += chr(n) # 문자로 저장

        elif "a" <= c <= "z":
            n = ord(c) + shift  # 문자를 숫자로 바꾼 후 3 더하기
            if n > ord("z"):
                 n -= 26  # 알파벳은 총 26개이므로

            result += chr(n)  # 문자로 저장

    return result


def caesar_decode(text: str, shift: int = 3) -> str: #-3칸
    result = ""  # 빈 문자열 만들기

    for c in text:  # 문장에서 글자를 하나씩 꺼내기
        if "A" <= c <= "Z":  # 대문자
            n = ord(c) - shift  # 문자를 숫자로 바꾼 후 3 빼기
            if n > ord("Z"):
                n -= 26  # 알파벳은 총 26개이므로

            result += chr(n)  # 문자로 저장

        elif "a" <= c <= "z":
            n = ord(c) - shift  # 문자를 숫자로 바꾼 후 3 빼기
            if n > ord("z"):
                n -= 26  # 알파벳은 총 26개이므로

            result += chr(n)  # 문자로 저장

    return result

def main():
    print(caesar_encode("ABC"))
    print(caesar_decode("Def"))



if __name__ == "__main__":
    main()