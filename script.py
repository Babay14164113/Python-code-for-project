# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Parametric UI Mockup")

count = tk.IntVar(value=5)
scale = tk.DoubleVar(value=1.0)

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(side="right", expand=True, fill="both")

widgets = []

def build_widgets():
    widgets.clear()
    for i in range(count.get()):
        widgets.append({
            "w": 60 * scale.get(),
            "h": 40 * scale.get(),
            "id": i + 1
        })
    draw()

def draw():
    canvas.delete("all")
    x, y = 20, 20
    for w in widgets:
        canvas.create_rectangle(x, y, x + w["w"], y + w["h"], fill="#cfe3ff", outline="black")
        canvas.create_text(x + 5, y + 5, anchor="nw", text=f"W{w['id']}")
        y += w["h"] + 10

def optimize():
    for w in widgets:
        w["h"] = 35 * scale.get()
    draw()

def rebuild(*args):
    build_widgets()

panel = ttk.Frame(root)
panel.pack(side="left", fill="y", padx=5, pady=5)

ttk.Label(panel, text="Количество").pack(anchor="w")
ttk.Scale(panel, from_=1, to=10, orient="horizontal", variable=count,
          command=rebuild).pack(fill="x")

ttk.Label(panel, text="Масштаб").pack(anchor="w")
ttk.Scale(panel, from_=0.5, to=2.0, orient="horizontal", variable=scale,
          command=rebuild).pack(fill="x")

ttk.Button(panel, text="Оптимизировать", command=optimize).pack(fill="x", pady=10)

build_widgets()
root.mainloop()