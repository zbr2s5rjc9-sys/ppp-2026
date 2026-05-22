def str2float(text: str, default_value: float = -999): #문자열을 숫자로 바꾸되 실패하면 기본값 부여
    try:
        return float(text)

    except ValueError: #만약 오류가 난다면 이걸 실행하겠다는 뜻
        return default_value

def main():
    #input_str = "123"
    result = str2float("ㄴ")
    print(result)

if __name__ == "__main__":
    main()