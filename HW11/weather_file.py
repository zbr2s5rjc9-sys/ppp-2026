def read_rainfall(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))

    return dataset


def read_tavg(weather_filename):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line. split(",")
            dataset.append(float(tokens[4]))

    return dataset

def count_five_mm_rainy_days(rainfall):
    count = 0
    for r in rainfall:
        if r >= 5:
            count += 1 # 5mm 이상인 날 하루를 찾을 때마다 1을 더하는 것!

    return count



def main():
    weather_filename = "weather(146)_2022-2022.csv"

    rainfall = read_rainfall(weather_filename)
    print(f"총 강우량 :  {sum(rainfall)}")

    tavg = read_tavg(weather_filename)
    print(f"연 평균 온도 : {sum(tavg) / len(tavg)}")

    five_mm_rainy_days = count_five_mm_rainy_days(rainfall)
    print(f"5mm이상 강우일수 : {five_mm_rainy_days}")




if __name__ == "__main__":
    main()