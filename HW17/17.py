def str2int(text: str, defalut_value: int = -999):
    try:
        return int(text) #문자열 -> 정수로 변환

    except ValueError:
        return defalut_value

def main():
    values = []
    while True: #무한반복
        x = input("x => ?")
        x_value = str2int(x)
        if x_value == -1:
            break #끝내버리는 것

        if x_value > 0 and type(x_value) == int: #자연수만 받기
         values.append(x_value)

    print(f"입력된 값은 {values}이고 총 {len(values)}개의 자연수가 입력되었으며"
          f" 입력된 값들의 평균은 {sum(values)/len(values)} 입니다.")

if __name__  == "__main__":
    main()