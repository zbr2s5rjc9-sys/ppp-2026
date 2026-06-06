import random
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()


def gui_input(text):
    return simpledialog.askstring(
        title="Test",
        prompt=text
    )


count = int(gui_input("추출 횟수 : "))

for i in range(count):  #count번 반복

    lotto = []

    while len(lotto) < 6: # 로또 안의 숫자가 6개보다 적으면 계속 랜덤 돌리라는 거

        num = random.randint(1, 45)

        if num not in lotto: # 중복되지 않게 하는 것!
            lotto.append(num)

    print(lotto)

def main():
    pass

if __name__ == "__main__":
    main()