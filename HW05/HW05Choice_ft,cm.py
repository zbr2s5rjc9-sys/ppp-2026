choice = float(input("1. ft -> cm , 2. cm -> ft 변환 기능을 선택하세요 : "))

if choice == 1:
    ft = float(input("길이(ft)를 입력해주세요 : "))
    cm = ft * 30.48
    print(f"{ft:.1f}ft -> {cm:.1f}cm")

elif choice == 2:
    cm = float(input("길이(cm)를 입력해주세요 : "))
    ft  = cm / 30.48
    print(f"{cm:.1f}cm -> {ft:.1f}ft")

