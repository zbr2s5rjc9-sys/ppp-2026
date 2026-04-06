import math

x1 = float(input("x1의 좌표를 입력하세세요 : "))
x2 = float(input("x2의 좌표를 입력하세요 : "))
y1 = float(input("y1의 좌표를 입력하세요 : "))
y2 = float(input("y2의 좌표를 입력하세요 : "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(distance)