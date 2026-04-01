cal_dict = {"한라봉" : 50, "딸기" : 34, "바나나": 77, "사과" : 90}

eat_dict = {"한라봉" : 100, "딸기" : 300, "사과" : 200, "배" : 400}

total_cal = 0

for key, val in eat_dict.items():
       print(key, val)
       if key in cal_dict:
              total_cal += val * cal_dict[key]

print(total_cal)
