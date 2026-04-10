def gugudan():
    dan = int(input("몇 단의 구구단을 원하시나요? : "))
    for n in range(1, 9 + 1):
        print(f"{dan}x{n} = {dan * n}")


if __name__ == "__main__":
    gugudan()
