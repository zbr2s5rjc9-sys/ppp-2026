import math

for angle in range(0, 10+1):
    rad = math.radians(angle)

    sin = math.sin(rad)
    cos = math.cos(rad)
    tan = math.tan(rad)
    print("각도  sin  cos  tan")

    print(f"{angle}  {sin:.4f}  {cos:.4f}  {tan:.4f}")