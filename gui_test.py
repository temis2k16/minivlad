from tkinter import *
from math import *

dot_size = 2
dot_color = "black"

root = Tk()
root.title("test")
root.geometry("800x600+200+100")
root.resizable(FALSE, FALSE)

mode = "line"

click_count = 0
first_dot = {"x":0, "y":0}
second_dot = {"x":0, "y":0}

dots = []
circles = []
lines = []


def dot(event):
    dots.append(c.create_oval(event.x - dot_size,
                              event.y - dot_size,
                              event.x + dot_size,
                              event.y + dot_size,
                              fill=dot_color, outline=dot_color))
    print("Точка: ", event.x, event.y)


def delete(event):
    if mode == "dot":
        if len(dots):
            c.delete(dots[-1])
            dots.pop()
    if mode == "circle":
        if len(circles):
            c.delete(circles[-1])
            c.delete(circles[-1]-1)
            circles.pop()



def line(event):
    global click_count
    click_count += 1
    if click_count % 2 == 1:
        print("1 dot:", event.x, event.y)
        first_dot['x'] = event.x
        first_dot['y'] = event.y
        c.create_oval(event.x - dot_size,
                      event.y - dot_size,
                      event.x + dot_size,
                      event.y + dot_size,
                      fill=dot_color, outline=dot_color)
    else:
        print("2 dot:", event.x, event.y)
        second_dot['x'] = event.x
        second_dot['y'] = event.y
        click_count = 0
        c.create_line(first_dot['x'], first_dot['y'], second_dot['x'], second_dot['y'], width=dot_size - 1)
        c.create_oval(event.x - dot_size,
                      event.y - dot_size,
                      event.x + dot_size,
                      event.y + dot_size,
                      fill=dot_color, outline=dot_color)


def circle(event):
    global click_count
    click_count += 1
    if click_count % 2 == 1:
        print("1 dot:", event.x, event.y)
        first_dot['x'] = event.x
        first_dot['y'] = event.y
        c.create_oval(event.x - dot_size,
                      event.y - dot_size,
                      event.x + dot_size,
                      event.y + dot_size,
                      fill=dot_color, outline=dot_color)
    else:
        print("2 dot:", event.x, event.y)
        second_dot['x'] = event.x
        second_dot['y'] = event.y
        click_count = 0
        r = sqrt((first_dot['x']-second_dot['x'])**2 + (first_dot['y']-second_dot['y'])**2)
        circles.append(c.create_oval(first_dot['x'] - r,
                                     first_dot['y'] - r,
                                     first_dot['x'] + r,
                                     first_dot['y'] + r, width=dot_size - 1))


c = Canvas(root, width=800, height=600)
c.pack()
if mode == "dot":
    c.bind("<Button-1>", dot)
    c.bind("<Button-2>", delete)

if mode == "line":
    c.bind("<Button-1>", line)

if mode == "circle":
    c.bind("<Button-1>", circle)
    c.bind("<Button-2>", delete)

root.mainloop()
