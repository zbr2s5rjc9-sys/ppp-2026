import time
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()

def gui_input(text):
    return simpledialog.askstring(
        title="Test",
        prompt=text
    )

gui_input("카운트다운 시작하려면 아무거나 입력")

for i in range(5, 0, -1):
    print(f"\r{i:3d}", end="")
    time.sleep(1)

print()