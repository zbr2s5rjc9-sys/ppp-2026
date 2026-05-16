def read_dates(weather_filename):
    dates = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            date = [int(tokens[0]), int(tokens[1]), int(tokens[2])] # year, month, day
            dates.append(date)

    return dates

def read_weather_col(weather_filename, col_idx):
    values = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
            values.append(value)

    return values

def get_max_diff(dates, tmax, tmin):
    max_diff = 0

    for i in range(len(dates)):
        diff = tmax[i] - tmin[i]
        if diff > max_diff:
            max_diff = diff # 이렇게 변환이 된다는 거!
            max_diff_date = dates[i] # 최대 일교차가 나온 걸로 날짜를 저장하는 것!

    return max_diff_date, max_diff # 일교차가 가장 큰 날, 그 날짜의 일교차


def gdd_season(dates, tavg): # 5~9월까지 적산 온도
    gdd_value = 0

    for i in range(len(dates)):
        date = dates[i]
        t = tavg[i]
        if date[1] in [5,6,7,8,9]: # date[1]은 month
            if t > 5: # 5도를 기준으로 함
                gdd_value += (t-5)

    return gdd_value


def main():
    weather_filename = "weather(146)_2001-2022 (1).csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename, 3)
    tmin = read_weather_col(weather_filename, 5)
    date, temp_diff = get_max_diff(dates, tmax, tmin)

    print(f"일교차가 가장 큰 날 : {date}")
    print(f"일교차가 가장 큰 날의 일교차 : {temp_diff}")

    tavg = read_weather_col(weather_filename, 4)
    gdd_value = gdd_season(dates, tavg)

    print(f"5월 ~ 9월 적산 온도 : {gdd_value:.1f}도")


if __name__ == "__main__":
    main()