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

def hangman_game():
    words = ["orange", "apple", "yogurt", "egg", "jeonbuk", "pasta"]

    answer = random.choice(words)
    ba = ["_"] * len(answer) #진행상황을 보려면 터미널을 봐야함!

    trial = 7

    while trial > 0:

        print("".join(ba), f"(trial = {trial})")

        ch = gui_input("답을 입력하세요")

        if ch in answer:

            for i in range(len(answer)):
                if answer[i] == ch:
                    ba[i] = ch

        else:
            print("틀렸습니다")
            trial -= 1

        if "".join(ba) == answer:
            print(f"{answer}!! 정답입니다.")
            break

    if trial == 0:
        print(f"게임 종료! 정답 : {answer}")

def main():
    hangman_game()

if __name__ == "__main__":
    main()
