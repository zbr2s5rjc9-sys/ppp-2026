mart = {"우유" : 2500,
        "물" : 1000,
        "반숙란" : 1700,
        "콜라" : 1500,
        "빵" : 2000}

cart = ["반숙란", "콜라", "빵"]

total_cost = 0

for item in cart:
    total_cost += mart[item]
    print(total_cost)

print(f"총 {total_cost}원 입니다.")