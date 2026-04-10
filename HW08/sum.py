def sum_n():
    n = int(input("숫자를 입력하세요 : "))
    total = 0
    for i in range (1, n+1):
        total += i
        print(total)

if __name__ == "__main__":
    sum_n()