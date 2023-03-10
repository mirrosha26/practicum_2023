import tkinter as tk
from math import sin, cos, pi

width = 600
height = 600
root = tk.Tk()
c = tk.Canvas(root, width=width, heigh=height)
points_list = []


def drawer(canvas, x, y, a, b):
    x = a + x
    y = b + y

    x1, y1 = (x - 1), (y - 1)
    x2, y2 = (x + 1), (y + 1)

    point = canvas.create_oval(x1, y1, x2, y2, fill="#f6f6f6", outline="#f6f6f6")

    points_list.append(point)


def sign(x):
    return ((x > 0) - (x < 0)) * 1


def processing(canvas, n):
    a, b = width // 2, height // 2
    na = 2 / n
    step = 1000
    piece = (pi * 2) / step
    xp = []
    yp = []

    t = 0
    for _ in range(step + 1):
        x = (abs((cos(t))) ** na) * a * sign(cos(t))
        y = (abs((sin(t))) ** na) * b * sign(sin(t))
        xp.append(x)
        yp.append(y)
        t += piece

    if len(xp) == len(yp):
        for i in range(len(xp)):
            drawer(canvas, xp[i], yp[i], a, b)
    else:
        raise ValueError("Точки x и y не совпадают")


def scale_processing(number):
    if len(points_list) != 0:
        for point in points_list:
            c.delete(point)

    processing(c, float(number))


def main():

    root.title("Суперэллипс")

    c.configure(bg="#0a95ff")
    c.pack(fill=tk.BOTH, expand=1)

    scale = tk.Scale(
        root,
        from_=0.01,
        to=3.75,
        digits=3,
        resolution=0.01,
        command=scale_processing,
        orient=tk.HORIZONTAL,
    )
    scale.pack(side=tk.LEFT, padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()
