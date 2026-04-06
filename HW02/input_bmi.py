weight = float(input("몸무게(kg)를 입력해보세요 : "))
height = float(input("키(cm)를 입력해보세요 : "))

height_m = height / 100
BMI = weight / (height_m **2)

print(BMI)

print(f"나의 BMI 지수는 {BMI}다!")