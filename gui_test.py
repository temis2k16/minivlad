from tkinter import *
from math import *

# def dot(event):
#     dots.append(c.create_oval(event.x - dot_size,
#                               event.y - dot_size,
#                               event.x + dot_size,
#                               event.y + dot_size,
#                               fill=color, outline=color))
#     print("Точка: ", event.x, event.y)
#
#
# def delete(event):
#     if mode == "dot":
#         if len(dots):
#             c.delete(dots[-1])
#             dots.pop()
#     if mode == "circle":
#         if len(circles):
#             c.delete(circles[-1], circles[-1]-1)
#             circles.pop()
#     if mode == "line":
#         if len(lines):
#             c.delete(lines[-1], lines[-1]-1, lines[-1]-2)
#             lines.pop()
#
#
# def line(event):
#     global click_count
#     click_count += 1
#     if click_count % 2 == 1:
#         print("1 dot:", event.x, event.y)
#         first_dot['x'] = event.x
#         first_dot['y'] = event.y
#         c.create_oval(event.x - (dot_size+0.5),
#                       event.y - (dot_size+0.5),
#                       event.x + (dot_size+0.5),
#                       event.y + (dot_size+0.5),
#                       fill=color, outline=color)
#     else:
#         print("2 dot:", event.x, event.y)
#         second_dot['x'] = event.x
#         second_dot['y'] = event.y
#         click_count = 0
#         c.create_line(first_dot['x'], first_dot['y'],
#                                    second_dot['x'], second_dot['y'],
#                                    width=dot_size)
#         lines.append( c.create_oval(event.x - (dot_size+0.5),
#                       event.y - (dot_size+0.5),
#                       event.x + (dot_size+0.5),
#                       event.y + (dot_size+0.5),
#                       fill=color, outline=color))
#
#
# def circle(event):
#     global click_count
#     click_count += 1
#     if click_count % 2 == 1:
#         print("1 dot:", event.x, event.y)
#         first_dot['x'] = event.x
#         first_dot['y'] = event.y
#         c.create_oval(event.x - dot_size,
#                       event.y - dot_size,
#                       event.x + dot_size,
#                       event.y + dot_size,
#                       fill=color, outline=color)
#     else:
#         print("2 dot:", event.x, event.y)
#         second_dot['x'] = event.x
#         second_dot['y'] = event.y
#         click_count = 0
#         r = sqrt((first_dot['x']-second_dot['x'])**2 + (first_dot['y']-second_dot['y'])**2)
#         circles.append(c.create_oval(first_dot['x'] - r,
#                                      first_dot['y'] - r,
#                                      first_dot['x'] + r,
#                                      first_dot['y'] + r, width=dot_size))


# def change_mode():
#     global mode
#     res = ""
#     if mode == "line":
#         res = "circle"
#     if mode=="circle":
#         res = "dot"
#     if mode=="dot":
#         res = "line"
#     mode = res
#     if mode == "dot":
#         c.bind("<Button-1>", dot)
#         c.bind("<Button-2>", delete)
#
#     if mode == "line":
#         c.bind("<Button-1>", line)
#         c.bind("<Button-2>", delete)
#
#     if mode == "circle":
#         c.bind("<Button-1>", circle)
#         c.bind("<Button-2>", delete)
#     print(mode)


class Window(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.dot_size = 1
        self.color = "black"
        self.mode = "line"
        self.click_count = 0
        self.first_dot = {"x": 0, "y": 0}
        self.second_dot = {"x": 0, "y": 0}
        self.dots = []
        self.circles = []
        self.lines = []
        self.setUI()

    def dot(self, event):
        self.dots.append(self.canv.create_oval(event.x - self.dot_size,
                                               event.y - self.dot_size,
                                               event.x + self.dot_size,
                                               event.y + self.dot_size,
                                               fill=self.color, outline=self.color))
        print("Точка: ", event.x, event.y)

    def delete(self, event):
        if self.mode == "dot":
            if len(self.dots):
                self.canv.delete(self.dots[-1])
                self.dots.pop()
        if self.mode == "circle":
            if len(self.circles):
                self.canv.delete(self.circles[-1], self.circles[-1] - 1)
                self.circles.pop()
            if len(self.circles)==0:
                self.help_def['text'] = "Нажмите ЛКМ, чтобы указать центр окружности"
        if self.mode == "line":
            if len(self.lines):
                self.canv.delete(self.lines[-1], self.lines[-1] - 1, self.lines[-1] - 2)
                self.lines.pop()
            if len(self.lines)==0:
                self.help_def['text'] = "Нажмите ЛКМ, чтобы начать рисовать линию"

    def delete_all(self):
        self.canv.delete("all")
        self.lines = []
        self.circles = []
        self.dots = []
        if self.mode == "line":
            self.help_def['text'] = "Нажмите ЛКМ, чтобы начать рисовать линию"

    def line(self, event):
        self.click_count += 1
        if self.click_count % 2 == 1:
            self.help_def['text'] = "Нажмите ЛКМ, чтобы закончить линию."
            print("1 dot:", event.x, event.y)
            self.first_dot['x'] = event.x
            self.first_dot['y'] = event.y
            self.canv.create_oval(event.x - (self.dot_size + 0.5),
                                  event.y - (self.dot_size + 0.5),
                                  event.x + (self.dot_size + 0.5),
                                  event.y + (self.dot_size + 0.5),
                                  fill=self.color, outline=self.color)
        else:
            print("2 dot:", event.x, event.y)
            self.help_def['text'] = "Нажмите ЛКМ, чтобы начать рисовать линию. Нажмите ПКМ, " \
                                    "чтобы удалить предыдущую линию."
            self.second_dot['x'] = event.x
            self.second_dot['y'] = event.y
            self.click_count = 0
            self.canv.create_line(self.first_dot['x'], self.first_dot['y'],
                                  self.second_dot['x'], self.second_dot['y'],
                                  width=self.dot_size, fill=self.color)
            self.lines.append(self.canv.create_oval(event.x - (self.dot_size + 0.5),
                                                    event.y - (self.dot_size + 0.5),
                                                    event.x + (self.dot_size + 0.5),
                                                    event.y + (self.dot_size + 0.5),
                                                    fill=self.color, outline=self.color))

    def circle(self, event):

        self.click_count += 1
        if self.click_count % 2 == 1:
            self.help_def['text'] = "Нажмите ЛКМ, чтобы задать радиус окружности."
            print("1 dot:", event.x, event.y)
            self.first_dot['x'] = event.x
            self.first_dot['y'] = event.y
            self.canv.create_oval(event.x - self.dot_size,
                                  event.y - self.dot_size,
                                  event.x + self.dot_size,
                                  event.y + self.dot_size,
                                  fill=self.color, outline=self.color)
        else:
            self.help_def['text'] = "Нажмите ЛКМ, чтобы указать центр окружности. Нажмите ПКМ, " \
                                    "чтобы удалить предыдущую окружность."
            print("2 dot:", event.x, event.y)
            self.second_dot['x'] = event.x
            self.second_dot['y'] = event.y
            self.click_count = 0
            r = sqrt((self.first_dot['x'] - self.second_dot['x']) ** 2 +
                        (self.first_dot['y'] - self.second_dot['y']) ** 2)
            self.circles.append(self.canv.create_oval(self.first_dot['x'] - r,
                                                      self.first_dot['y'] - r,
                                                      self.first_dot['x'] + r,
                                                      self.first_dot['y'] + r, width=self.dot_size))

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.dot_size = new_size

    def set_dot_mode(self):
        self.mode = "dot"
        self.help_def['text'] = "Нажмите ЛКМ, чтобы поставить точку. Нажмите ПКМ, чтобы удалить точку"
        self.canv.bind("<Button-1>", self.dot)
        self.canv.bind("<Button-2>", self.delete)

    def set_circle_mode(self):
        self.mode = "circle"
        if self.circles:
            self.help_def['text'] = "Нажмите ЛКМ, чтобы указать центр окружности. Нажмите ПКМ, " \
                                    "чтобы удалить предыдущую окружность."
        else:
            self.help_def['text'] = "Нажмите ЛКМ, чтобы указать центр окружности"

        self.canv.bind("<Button-1>", self.circle)
        self.canv.bind("<Button-2>", self.delete)

    def set_line_mode(self):
        self.mode = "line"
        if self.lines:
            self.help_def['text'] = "Нажмите ЛКМ, чтобы начать рисовать линию. Нажмите ПКМ, " \
                                    "чтобы удалить предыдущую линию."
        else:
            self.help_def['text'] = "Нажмите ЛКМ, чтобы начать рисовать линию"
        self.canv.bind("<Button-1>", self.line)
        self.canv.bind("<Button-2>", self.delete)

    def show_tip(self, event, string):
        self.tool_def['text'] = string

    def setUI(self):
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

        self.columnconfigure(6, weight=1)   # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки
                                            # не будут разъезжаться при ресайзе
        self.rowconfigure(2, weight=1)      # То же самое для третьего ряда

        self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=1, sticky=E+W+S+N)
        self.help = Label(self, text="Подсказка:",height=1)
        self.help.grid(row=3, column=0, sticky=S+W)

        self.help_def = Label(self, text="", height=1)
        self.help_def.grid(row=3, column=1, columnspan=6, sticky=S+W)

        if self.mode == "dot":
            self.help_def['text'] = "Нажмите ЛКМ, чтобы поставить точку. Нажмите ПКМ, чтобы удалить точку"
            self.canv.bind("<Button-1>", self.dot)
            self.canv.bind("<Button-2>", self.delete)

        if self.mode == "line":
            self.help_def['text'] = "Нажмите ЛКМ, чтобы начать рисовать линию"
            self.canv.bind("<Button-1>", self.line)
            self.canv.bind("<Button-2>", self.delete)

        if self.mode == "circle":
            self.help_def['text'] = "Нажмите ЛКМ, чтобы указать центр окружности"
            self.canv.bind("<Button-1>", self.circle)
            self.canv.bind("<Button-2>", self.delete)

        self.tools_lab = Label(self, text="Инструмент: ", width=10, height=1)
        self.tools_lab.grid(row=0, column=0, sticky=NW)

        self.tool_def = Label(self, text="", width=10, height=1)
        self.tool_def.grid(row=1, column=0, sticky=NW)

        # del_lab = Label(self, text="Delete all:")
        # del_lab.grid(row=0, column=6, padx=6, sticky=N + E)

        self.dot_im = PhotoImage(file="resources/3dot_button.png")
        dot_btn = Button(self, compound=CENTER,width=31, height=31, border=0, )
        self.dot_im = self.dot_im.subsample(2,2)
        dot_btn["command"] = self.set_dot_mode
        dot_btn["image"] = self.dot_im
        dot_btn.grid(row=0, column=1, padx=5, rowspan=2)
        dot_btn.bind("<Enter>", lambda event: self.show_tip(event, string="Точка"))
        dot_btn.bind("<Leave>", lambda event: self.show_tip(event, string=""))

        self.round_im = PhotoImage(file="resources/circle_button.png")
        circle_btn = Button(self, compound=CENTER,width=31, height=31, border=0, )
        self.round_im = self.round_im.subsample(2,2)
        circle_btn["command"] = self.set_circle_mode
        circle_btn["image"] = self.round_im
        circle_btn.grid(row=0, column=2,padx=5,rowspan=2)
        circle_btn.bind("<Enter>", lambda event: self.show_tip(event, string="Окружность"))
        circle_btn.bind("<Leave>", lambda event: self.show_tip(event, string=""))

        self.line_im = PhotoImage(file="resources/line_button.png")
        line_btn = Button(self, compound=CENTER, width=31, height=31, border=0, )
        self.line_im = self.line_im.subsample(2, 2)
        line_btn["command"] = self.set_line_mode
        line_btn["image"] = self.line_im
        line_btn.grid(row=0, column=3, padx=5,rowspan=2)
        line_btn.bind("<Enter>", lambda event: self.show_tip(event, string="Линия"))
        line_btn.bind("<Leave>", lambda event: self.show_tip(event, string=""))

        self.pick_im = PhotoImage(file="resources/pick_button.png")
        pick_btn = Button(self, compound=CENTER, width=31, height=31, border=0, )
        self.pick_im = self.pick_im.subsample(2, 2)
        pick_btn["command"] = self.set_line_mode
        pick_btn["image"] = self.pick_im
        pick_btn.grid(row=0, column=4, padx=5,rowspan=2)
        pick_btn.bind("<Enter>", lambda event: self.show_tip(event, string="Выбор"))
        pick_btn.bind("<Leave>", lambda event: self.show_tip(event, string=""))

        self.del_im = PhotoImage(file="resources/refresh.png")
        del_btn = Button(self, compound=CENTER, width=31, height=31, border=0, )
        self.del_im = self.del_im.subsample(2, 2)
        del_btn["command"] = self.delete_all
        del_btn["image"] = self.del_im
        del_btn.grid(row=0, column=6, padx=10, rowspan=2,sticky=E)
        del_btn.bind("<Enter>", lambda event: self.show_tip(event, string="Удалить всё"))
        del_btn.bind("<Leave>", lambda event: self.show_tip(event, string=""))

        # clear_btn = Button(self, text="Clear all", width=10,
        #                    command=lambda: self.canv.delete("all"))
        # clear_btn.grid(row=0, column=5, sticky=W)

        # size_lab = Label(self, text="Brush size: ")
        # size_lab.grid(row=1, column=0, padx=5)
        # one_btn = Button(self, text="Two", width=3,
        #                  command=lambda: self.set_brush_size(2))
        # one_btn.grid(row=1, column=1)
        #
        # two_btn = Button(self, text="Five", width=10,
        #                  command=lambda: self.set_brush_size(5))
        # two_btn.grid(row=1, column=2)
        #
        # five_btn = Button(self, text="Seven", width=10,
        #                   command=lambda: self.set_brush_size(7))
        # five_btn.grid(row=1, column=3)
        #
        # seven_btn = Button(self, text="Ten", width=10,
        #                    command=lambda: self.set_brush_size(10))
        # seven_btn.grid(row=1, column=4)
        #
        # ten_btn = Button(self, text="Twenty", width=10,
        #                  command=lambda: self.set_brush_size(20))
        # ten_btn.grid(row=1, column=5)
        #
        # twenty_btn = Button(self, text="Fifty", width=10,
        #                     command=lambda: self.set_brush_size(50))
        # twenty_btn.grid(row=1, column=6, sticky=W)

# buttons_frame = Frame(root, bg='grey', height=50)
# buttons_frame.pack(fill='x', side='top')

# c = Canvas(root, bg='white')
# c.grid(row=2, column=0, columnspan=7,
#                        padx=5, pady=5, sticky=E+W+S+N)
# c.grid(row=0, column=0, sticky='WE')
# c.pack(fill=BOTH, expand=1)

# hint_frame = Frame(root, bg='green', height=20)
# hint_frame.grid(row=1, column=0, sticky='WE')
# hint_frame.pack(fill="x", side='bottom')

# button_line = Button(buttons_frame, text="mode")
# button_line.grid(row=0, column=1)
# button_line['command'] = change_mode
#
# if mode == "dot":
#     c.bind("<Button-1>", dot)
#     c.bind("<Button-2>", delete)
#
# if mode == "line":
#     c.bind("<Button-1>", line)
#     c.bind("<Button-2>", delete)
#
# if mode == "circle":
#     c.bind("<Button-1>", circle)
#     c.bind("<Button-2>", delete)


if __name__ == "__main__":
    root = Tk()
    root.title("test")
    root.geometry("900x600+200+100")
    # root.resizable(FALSE, FALSE)
    app = Window(root)
    root.mainloop()
