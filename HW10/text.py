def read_text(filename):
    print(filename)

    with open(filename) as f:
        text = f.read()         # 파일 안 내용을 문자열로 저장!
        print(f"{text}")
    return text # 함수 안에서 읽은 결과를 밖으로 보내버리기

def text2list(text): #아직 문자열 -> 그래서 숫자 리스트가 필요!
    text.split()
    num_list = []
    for num_text in text.split():
        num_list.append(int(num_text))
        print(num_list)
    return num_list


def main():
    filename = "numbers22"
    text = read_text(filename)
    numbers = text2list(text)

    count = len(numbers)
    avg = sum(numbers) / count
    max_num = max(numbers)
    min_num = min(numbers)

    numbers.sort()
    if count % 2 == 1: #만약에 홀수라면?
        median = numbers[count // 2] # 홀수니까 가운데 값이 하나!
    else:
        median = numbers[count // 2 - 1] + numbers[count // 2] #짝수라서 오른쪽 가운데 값 + 왼쪽 가운데 값 !!


    print("개수 : ", count)
    print("평균 : ",avg)
    print("최대 : ", max_num)
    print("최소 : ", min_num)
    print("중앙값 : ", median)


if __name__ == "__main__":
    main()

