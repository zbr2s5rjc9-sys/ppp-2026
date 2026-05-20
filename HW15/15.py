import requests

def read_tavg(filename):
    dataset = []

    with open(filename) as f:
        lines = f.readlines()

    for line in lines[1:]:
        tokens = line.split(",")
        dataset.append(float(tokens[4]))

    return dataset

def read_rainfall(filename):
    dataset = []

    with open(filename) as f:
        lines = f.readlines()

    for line in lines[1:]:
        tokens = line.split(",")
        dataset.append(float(tokens[9]))

    return dataset


def count_five_mm_rainy_days(rainfall):
    count = 0
    for i in rainfall:
        if i >= 5:
            count += 1 # 5mm 이상인 날 하루를 찾을 때마다 1을 더하는 것!

    return count


def main():
    year = 2023
    url = f"https://api.taegon.kr/stations/146/?sy={year}&ey={year}&format=csv"

    resp = requests.get(url)
    filename = f"weather_{year}.csv"

    with open(filename, "w") as fout:
        fout.write(resp.text)

    tavg = read_tavg(filename)
    rainfall = read_rainfall(filename)
    five_mm_rainy_days =  count_five_mm_rainy_days(rainfall)

    with open("result.txt", "w") as fout:
        fout.write(f"연 평균 기온 : {sum(tavg) / len(tavg):.1f}도")
        fout.write(f"5mm 이상 강우일수 : {five_mm_rainy_days}일")
        fout.write(f"총 강우량 : {sum(rainfall)}mm")



if __name__ == "__main__":
    main()