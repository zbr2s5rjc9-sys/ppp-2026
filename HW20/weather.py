import requests
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib
import numpy as np



def download_weather(filename, stid, sy, ey ):
    url = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}2022&format=csv"

    if not os.path.exists(filename):
        resp = requests.get(url) # 파일을 찾는 경로
        with open(filename, "w") as fout:
            fout.write(resp.text)
    else:
        print(f"이미 {filename}이 있습니다.")



def main():
    filename = "weather_jeonju_1980-2024.csv"
    filename_sw = "weather_suwon_1980-2024.csv"
    download_weather(filename, 146, 1980, 2024)
    download_weather(filename_sw, 119, 1980, 2024)

    df_jj = pd.read_csv(filename, skipinitialspace = True)
    df_sw = pd.read_csv(filename_sw, skipinitialspace=True)
    print(df_jj.head())
    print(df_sw.head())

    temp_jj = []
    temp_sw = []

    for y in range(1980, 2025):
        jj = df_jj[df_jj["year"] == y]["tavg"]
        sw = df_sw[df_sw["year"] == y]["tavg"]

        temp_jj.append(sum(jj) / len(jj))
        temp_sw.append(sum(sw) / len(sw))

    plt.plot(temp_jj, color="r", label="전주")
    plt.plot(temp_sw, color="b", label="수원")

    plt.ylabel("평균기온(℃)")
    plt.legend()
    plt.savefig("./line_temp.png")

    rain_jj = []

    for y in range(1980, 2025):
        total = df_jj[df_jj["year"] == y]["rainfall"].sum()
        rain_jj.append(total)

    fig, ax = plt.subplots(figsize=(30, 6))
    year = [str(x + 1980) for x in range(45)]
    ax.bar(year, rain_jj, color="b")
    ax.set_ylabel("전주시의 연 평균 강우량(mm)")
    fig.savefig("bar_rain.png")
    # plt.show()


# 7번
    birth_temp = [] #1980~2024년의 4월 16일 기온을 저장할 공간!

    for y in range(1980, 2025):
        temp = df_jj[df_jj["year"] == y] #2006년만 뽑기
        temp = temp[temp["month"] == 4] #4월만 뽑기
        temp = temp[temp["day"] == 16] #16일만 뽑기

        birth_temp.append(sum(temp["tavg"])) # 기온 저장

# 7번 그래프를 그려보자!

    plt.figure(figsize=(15, 6))
    plt.plot(birth_temp, color="r")
    plt.ylabel("기온(℃)")
    plt.savefig("./birthday_temp.png")

    print(birth_temp[:5])


    a = (df_jj[df_jj["year"]==2012]["rainfall"].sum())
    print(f"전주시의 2012년 연 강수량은? : {a:.1f}mm")

    b = df_jj[df_jj["year"] == 2024]["tmax"].max()
    print(f"전주시의 2024년 최대기온은?: {b:.1f}도")

    df_jj["tdiff"]= df_jj["tmax"] - df_jj["tmin"]
    c = df_jj[df_jj["year"] == 2020]["tdiff"].max()
    print(f"전주시의 2020년 최대 일교차: {c:.1f}도")

    df_sw = pd.read_csv(filename_sw, skipinitialspace = True)
    prec_jj = df_jj[df_jj["year"]==2019]["rainfall"].sum()
    prec_sw = df_sw[df_sw["year"]==2019]["rainfall"].sum()

    d = abs(prec_jj) - (prec_sw)
    print(f"2019년 수원과 전주의 총강수량 차이: {d:.1f}mm")


    high = max(birth_temp) #가장 따뜻했던 4월 16일 기온
    for i in range(45): # 그게 몇년인지 찾는 것(45번 반복)
        if birth_temp[i] == high: #현재 값과 최고기온이 같다면
            print(f"가장 온도가 높았던 해 : {1980 + i}년")

    low = min(birth_temp)  # 가장 추웠던 4월 16일 기온
    for i in range(45):  # 그게 몇년인지 찾는 것(45번 반복)
        if birth_temp[i] == low:  # 현재 값과 최저기온이 같다면
            print(f"가장 온도가 낮았던 해 : {1980 + i}년")

    temp_2006 = birth_temp[2006 - 1980] #45개 중 26번째

    rank = 1 #처음에는 1등이라고 가정
    for i in range(35):
        if birth_temp[i] > temp_2006:
            rank += 1 # 점점 순위가 밀리는 것

    print(f"2006년은 {rank}번째로 온도가 높다!")



if __name__ == "__main__":
    main()