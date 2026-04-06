choice = float(input("1. C-> F, 2. F -> C  선택 : "))

if choice == 1:
    temp_c = float(input("섭씨 온도를 입력하시오 : "))
    temp_f = temp_c * 9 / 5 + 32
    print(f"{temp_c:.1f}C =>  {temp_f:.1f}F")

if choice == 2:
    temp_f = float(input("화씨 온도를 입력하시오 : "))
    temp_f = temp_c * 9 / 5 + 32
    print(f"{temp_f:.1f}F =>  {temp_c:.1f}C")
