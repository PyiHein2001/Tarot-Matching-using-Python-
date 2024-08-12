from controller import *
import controller as ctlr

import time
import random
import json

from main import *
import main as m

from tkinter import * 
import tkinter as tk 

from tkinter.messagebox import *
import tkinter.messagebox as mb

from tkinter.ttk import * 
import tkinter.ttk as ttk

from PIL import ImageTk, Image

class View(tk.Frame):
    def __init__(self, parent, *args):
        super().__init__()

        def _clear_another_win():
            for i in parent.winfo_children():
                parent.destroy()
                parent.quit()
                if hasattr(parent, "win"):
                    parent.win.destroy()
                    parent.win.quit()
                else:
                    print("no")

        def _back_to_main_menu():
            self.win.destroy()
            app = m.App(parent)
            app.mainloop()

        def _onecard():
            _clear_another_win()
            self.win = tk.Tk()

            def shuffle():
                counter = 0
                for i in self.win.winfo_children():
                    counter += 1
                    if counter > 3:
                        i.destroy()
                card_creator()

            self.bgcolor = "#404040"
            self.win.geometry("1400x800+10+10")
            self.win.configure(bg=self.bgcolor)
            self.win.title(self.onecard_mm)
            self.win.attributes("-fullscreen", -1)

            self.back = tk.Button(self.win, text="<< Back Menu", bg=self.bgcolor, fg="blue", font=("Times New Roman", 12, "bold"), command=_back_to_main_menu)
            self.back.grid(row=0, column=0, pady=10, padx=30)

            button = tk.Button(self.win, text="Shuffle", fg="blue", bg="#404040", command=shuffle)
            button.grid(row=3, column=0, pady=0, padx=30, sticky="nesw")

            title = tk.Label(self.win, text=self.onecard_mm, bg=self.bgcolor, fg="blue")
            title.grid(row=3, column=1, pady=10, padx=10)

            self.img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/tarot_back.jpg")
            self.resize_img = self.img.resize((100, 200), Image.Resampling.LANCZOS)
            self.new_img = ImageTk.PhotoImage(self.resize_img)

            self.canvasDict = {}
            self.canvasDict2 = {}
            self.canvasDict3 = {}

            def card_delay():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].grid(row=4, column=1+i, padx=10, pady=3)

            def card_delay2():
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)].grid(row=5, column=1+i, padx=10, pady=3)

            def card_delay3():
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)].grid(row=6, column=1+i, padx=10, pady=3)

            self.choosecard_list = [
                "fool", "magician", "popess", "empress", "emperor", "hierophant", "lovers", "chariot", "strength", "hermit",
                "wheel_of_fortune", "justice", "hanged_man", "death", "temperance", "devil", "tower", "star", "moon", "sun",
                "judgement", "earth"
            ]

            def chooseCard(event):
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].destroy()
                    self.canvasDict3["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i+1)].destroy()

                x = random.randrange(0, 22)
                try:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpeg".format(self.choosecard_list[x]))
                except Exception:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpg".format(self.choosecard_list[x]))

                self.imagecard_resize = self.imagecard.resize((150, 280), Image.Resampling.LANCZOS)
                self.imagecard_new = ImageTk.PhotoImage(self.imagecard_resize)

                self.canvasCard = Canvas(self.win, width=150, height=280)
                self.canvasCard.create_image(0, 0, anchor=NW, image=self.imagecard_new)
                self.canvasCard.grid(row=4, column=0, rowspan=4, pady=30, padx=30)

                self.choosecard_name = self.choosecard_list[x]
                namelb = tk.Label(self.win, text="The card name is the '{}'.".format(self.choosecard_name), fg="lightblue", bg="#404040", font=('Times New Roman', 12, 'bold'))
                namelb.grid(row=4, rowspan=2, column=1, padx=20, pady=30, sticky=W)

                self.predict_img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/one/{}.jpg".format(self.choosecard_name))
                self.predict_img_resize = self.predict_img.resize((800, 350), Image.Resampling.LANCZOS)
                self.predict_img_new = ImageTk.PhotoImage(self.predict_img_resize)

                self.canvasPredict = Canvas(self.win, width=800, height=350)
                self.canvasPredict.create_image(0, 0, anchor=NW, image=self.predict_img_new)
                self.canvasPredict.grid(row=6, column=1, rowspan=4, pady=30, padx=30)

            def card_creator():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(1000, card_delay)
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict2["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict2["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(2000, card_delay2)
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict3["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict3["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(3000, card_delay3)

            card_creator()

            self.win.mainloop()

        def _past():
            _clear_another_win()
            self.win = tk.Tk()

            def shuffle():
                counter = 0
                for i in self.win.winfo_children():
                    counter += 1
                    if counter > 3:
                        i.destroy()
                card_creator()

            self.bgcolor = "#404040"
            self.win.geometry("1200x600+60+30")
            self.win.configure(bg=self.bgcolor)
            self.win.title(self.onecard_mm)
            self.win.attributes("-fullscreen", -1)

            self.back = tk.Button(self.win, text="<< Back Menu", bg=self.bgcolor, fg="blue", font=("Times New Roman", 12, "bold"), command=_back_to_main_menu)
            self.back.grid(row=0, column=0, pady=10, padx=30)

            button = tk.Button(self.win, text="Shuffle", fg="blue", bg="#404040", command=shuffle)
            button.grid(row=3, column=0, pady=0, padx=30, sticky="nesw")

            title = tk.Label(self.win, text="Your Past Life", bg=self.bgcolor, fg="blue")
            title.grid(row=3, column=1, pady=10, padx=10)

            self.img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/tarot_back.jpg")
            self.resize_img = self.img.resize((100, 200), Image.Resampling.LANCZOS)
            self.new_img = ImageTk.PhotoImage(self.resize_img)

            self.canvasDict = {}
            self.canvasDict2 = {}
            self.canvasDict3 = {}

            def card_delay():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].grid(row=4, column=1+i, padx=10, pady=3)

            def card_delay2():
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)].grid(row=5, column=1+i, padx=10, pady=3)

            def card_delay3():
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)].grid(row=6, column=1+i, padx=10, pady=3)

            self.choosecard_list = [
                "fool", "magician", "popess", "empress", "emperor", "hierophant", "lovers", "chariot", "strength", "hermit",
                "wheel_of_fortune", "justice", "hanged_man", "death", "temperance", "devil", "tower", "star", "moon", "sun",
                "judgement", "earth"
            ]

            def chooseCard(event):
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].destroy()
                    self.canvasDict3["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i+1)].destroy()

                x = random.randrange(0, 22)
                try:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpeg".format(self.choosecard_list[x]))
                except Exception:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpg".format(self.choosecard_list[x]))

                self.imagecard_resize = self.imagecard.resize((150, 280), Image.Resampling.LANCZOS)
                self.imagecard_new = ImageTk.PhotoImage(self.imagecard_resize)

                self.canvasCard = Canvas(self.win, width=150, height=280)
                self.canvasCard.create_image(0, 0, anchor=NW, image=self.imagecard_new)
                self.canvasCard.grid(row=4, column=0, rowspan=4, pady=30, padx=30)

                self.choosecard_name = self.choosecard_list[x]
                namelb = tk.Label(self.win, text="The card name is the '{}'.".format(self.choosecard_name), fg="lightblue", bg="#404040", font=('Times New Roman', 12, 'bold'))
                namelb.grid(row=4, rowspan=2, column=1, padx=20, pady=30, sticky=W)

                self.predict_img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/past/{}.jpg".format(self.choosecard_name))
                self.predict_img_resize = self.predict_img.resize((800, 350), Image.Resampling.LANCZOS)
                self.predict_img_new = ImageTk.PhotoImage(self.predict_img_resize)

                self.canvasPredict = Canvas(self.win, width=800, height=350)
                self.canvasPredict.create_image(0, 0, anchor=NW, image=self.predict_img_new)
                self.canvasPredict.grid(row=6, column=1, rowspan=4, pady=30, padx=30)

            def card_creator():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(1000, card_delay)
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict2["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict2["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(2000, card_delay2)
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict3["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict3["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(3000, card_delay3)

            card_creator()

            self.win.mainloop()

        def _love():
            _clear_another_win()
            self.win = tk.Tk()

            def shuffle():
                counter = 0
                for i in self.win.winfo_children():
                    counter += 1
                    if counter > 3:
                        i.destroy()
                card_creator()

            self.bgcolor = "#404040"
            self.win.geometry("1200x600+60+30")
            self.win.configure(bg=self.bgcolor)
            self.win.title(self.onecard_mm)
            self.win.attributes("-fullscreen", -1)

            self.back = tk.Button(self.win, text="<< Back Menu", bg=self.bgcolor, fg="blue", font=("Times New Roman", 12, "bold"), command=_back_to_main_menu)
            self.back.grid(row=0, column=0, pady=10, padx=30)

            button = tk.Button(self.win, text="Shuffle", fg="blue", bg="#404040", command=shuffle)
            button.grid(row=3, column=0, pady=0, padx=30, sticky="nesw")

            title = tk.Label(self.win, text="Your Love Life", bg=self.bgcolor, fg="blue")
            title.grid(row=3, column=1, pady=10, padx=10)

            self.img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/tarot_back.jpg")
            self.resize_img = self.img.resize((100, 200), Image.Resampling.LANCZOS)
            self.new_img = ImageTk.PhotoImage(self.resize_img)

            self.canvasDict = {}
            self.canvasDict2 = {}
            self.canvasDict3 = {}

            def card_delay():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].grid(row=4, column=1+i, padx=10, pady=3)

            def card_delay2():
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)].grid(row=5, column=1+i, padx=10, pady=3)

            def card_delay3():
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)].grid(row=6, column=1+i, padx=10, pady=3)

            self.choosecard_list = [
                "fool", "magician", "popess", "empress", "emperor", "hierophant", "lovers", "chariot", "strength", "hermit",
                "wheel_of_fortune", "justice", "hanged_man", "death", "temperance", "devil", "tower", "star", "moon", "sun",
                "judgement", "earth"
            ]

            def chooseCard(event):
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].destroy()
                    self.canvasDict3["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i+1)].destroy()

                x = random.randrange(0, 22)
                try:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpeg".format(self.choosecard_list[x]))
                except Exception:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpg".format(self.choosecard_list[x]))

                self.imagecard_resize = self.imagecard.resize((150, 280), Image.Resampling.LANCZOS)
                self.imagecard_new = ImageTk.PhotoImage(self.imagecard_resize)

                self.canvasCard = Canvas(self.win, width=150, height=280)
                self.canvasCard.create_image(0, 0, anchor=NW, image=self.imagecard_new)
                self.canvasCard.grid(row=4, column=0, rowspan=4, pady=30, padx=30)

                self.choosecard_name = self.choosecard_list[x]
                namelb = tk.Label(self.win, text="The card name is the '{}'.".format(self.choosecard_name), fg="lightblue", bg="#404040", font=('Times New Roman', 12, 'bold'))
                namelb.grid(row=4, rowspan=2, column=1, padx=20, pady=30, sticky=W)

                self.predict_img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/love/{}.jpg".format(self.choosecard_name))
                self.predict_img_resize = self.predict_img.resize((800, 350), Image.Resampling.LANCZOS)
                self.predict_img_new = ImageTk.PhotoImage(self.predict_img_resize)

                self.canvasPredict = Canvas(self.win, width=800, height=350)
                self.canvasPredict.create_image(0, 0, anchor=NW, image=self.predict_img_new)
                self.canvasPredict.grid(row=6, column=1, rowspan=4, pady=30, padx=30)

            def card_creator():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(1000, card_delay)
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict2["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict2["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(2000, card_delay2)
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict3["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict3["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(3000, card_delay3)

            card_creator()

            self.win.mainloop()

        def _education():
            _clear_another_win()
            self.win = tk.Tk()

            def shuffle():
                counter = 0
                for i in self.win.winfo_children():
                    counter += 1
                    if counter > 3:
                        i.destroy()
                card_creator()

            self.bgcolor = "#404040"
            self.win.geometry("1200x600+60+30")
            self.win.configure(bg=self.bgcolor)
            self.win.title(self.onecard_mm)
            self.win.attributes("-fullscreen", -1)

            self.back = tk.Button(self.win, text="<< Back Menu", bg=self.bgcolor, fg="blue", font=("Times New Roman", 12, "bold"), command=_back_to_main_menu)
            self.back.grid(row=0, column=0, pady=10, padx=30)

            button = tk.Button(self.win, text="Shuffle", fg="blue", bg="#404040", command=shuffle)
            button.grid(row=3, column=0, pady=0, padx=30, sticky="nesw")

            title = tk.Label(self.win, text="Your Education Path", bg=self.bgcolor, fg="blue")
            title.grid(row=3, column=1, pady=10, padx=10)

            self.img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/tarot_back.jpg")
            self.resize_img = self.img.resize((100, 200), Image.Resampling.LANCZOS)
            self.new_img = ImageTk.PhotoImage(self.resize_img)

            self.canvasDict = {}
            self.canvasDict2 = {}
            self.canvasDict3 = {}

            def card_delay():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].grid(row=4, column=1+i, padx=10, pady=3)

            def card_delay2():
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)].grid(row=5, column=1+i, padx=10, pady=3)

            def card_delay3():
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)].grid(row=6, column=1+i, padx=10, pady=3)

            self.choosecard_list = [
                "fool", "magician", "popess", "empress", "emperor", "hierophant", "lovers", "chariot", "strength", "hermit",
                "wheel_of_fortune", "justice", "hanged_man", "death", "temperance", "devil", "tower", "star", "moon", "sun",
                "judgement", "earth"
            ]

            def chooseCard(event):
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].destroy()
                    self.canvasDict3["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i+1)].destroy()

                x = random.randrange(0, 22)
                try:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpeg".format(self.choosecard_list[x]))
                except Exception:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpg".format(self.choosecard_list[x]))

                self.imagecard_resize = self.imagecard.resize((150, 280), Image.Resampling.LANCZOS)
                self.imagecard_new = ImageTk.PhotoImage(self.imagecard_resize)

                self.canvasCard = Canvas(self.win, width=150, height=280)
                self.canvasCard.create_image(0, 0, anchor=NW, image=self.imagecard_new)
                self.canvasCard.grid(row=4, column=0, rowspan=4, pady=30, padx=30)

                self.choosecard_name = self.choosecard_list[x]
                namelb = tk.Label(self.win, text="The card name is the '{}'.".format(self.choosecard_name), fg="lightblue", bg="#404040", font=('Times New Roman', 12, 'bold'))
                namelb.grid(row=4, rowspan=2, column=1, padx=20, pady=30, sticky=W)

                self.predict_img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/edu/{}.jpg".format(self.choosecard_name))
                self.predict_img_resize = self.predict_img.resize((600, 350), Image.Resampling.LANCZOS)
                self.predict_img_new = ImageTk.PhotoImage(self.predict_img_resize)

                self.canvasPredict = Canvas(self.win, width=600, height=350)
                self.canvasPredict.create_image(0, 0, anchor=NW, image=self.predict_img_new)
                self.canvasPredict.grid(row=6, column=1, rowspan=4, pady=30, padx=30)

            def card_creator():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(1000, card_delay)
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict2["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict2["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(2000, card_delay2)
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict3["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict3["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(3000, card_delay3)

            card_creator()

            self.win.mainloop()

        def _career():
            _clear_another_win()
            self.win = tk.Tk()

            def shuffle():
                counter = 0
                for i in self.win.winfo_children():
                    counter += 1
                    if counter > 3:
                        i.destroy()
                card_creator()

            self.bgcolor = "#404040"
            self.win.geometry("1200x600+60+30")
            self.win.configure(bg=self.bgcolor)
            self.win.title("Your career path")
            self.win.attributes("-fullscreen", -1)

            self.back = tk.Button(self.win, text="<< Back Menu", bg=self.bgcolor, fg="blue", font=("Times New Roman", 12, "bold"), command=_back_to_main_menu)
            self.back.grid(row=0, column=0, pady=10, padx=30)

            button = tk.Button(self.win, text="Shuffle", fg="blue", bg="#404040", command=shuffle)
            button.grid(row=3, column=0, pady=0, padx=30, sticky="nesw")

            title = tk.Label(self.win, text="Your Career Path", bg=self.bgcolor, fg="blue")
            title.grid(row=3, column=1, pady=10, padx=10)

            self.img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/tarot_back.jpg")
            self.resize_img = self.img.resize((100, 200), Image.Resampling.LANCZOS)
            self.new_img = ImageTk.PhotoImage(self.resize_img)

            self.canvasDict = {}
            self.canvasDict2 = {}
            self.canvasDict3 = {}

            def card_delay():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].grid(row=4, column=1+i, padx=10, pady=3)

            def card_delay2():
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)].grid(row=5, column=1+i, padx=10, pady=3)

            def card_delay3():
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)].grid(row=6, column=1+i, padx=10, pady=3)

            self.choosecard_list = [
                "fool", "magician", "popess", "empress", "emperor", "hierophant", "lovers", "chariot", "strength", "hermit",
                "wheel_of_fortune", "justice", "hanged_man", "death", "temperance", "devil", "tower", "star", "moon", "sun",
                "judgement", "earth"
            ]

            def chooseCard(event):
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)].destroy()
                    self.canvasDict3["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i)].destroy()
                    self.canvasDict2["canvas_{}".format(i+1)].destroy()

                x = random.randrange(0, 22)
                try:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpeg".format(self.choosecard_list[x]))
                except Exception:
                    self.imagecard = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/Tarot/{}.jpg".format(self.choosecard_list[x]))

                self.imagecard_resize = self.imagecard.resize((150, 280), Image.Resampling.LANCZOS)
                self.imagecard_new = ImageTk.PhotoImage(self.imagecard_resize)

                self.canvasCard = Canvas(self.win, width=150, height=280)
                self.canvasCard.create_image(0, 0, anchor=NW, image=self.imagecard_new)
                self.canvasCard.grid(row=4, column=0, rowspan=4, pady=30, padx=30)

                self.choosecard_name = self.choosecard_list[x]
                namelb = tk.Label(self.win, text="The card name is the '{}'.".format(self.choosecard_name), fg="lightblue", bg="#404040", font=('Times New Roman', 12, 'bold'))
                namelb.grid(row=4, rowspan=2, column=1, padx=20, pady=30, sticky=W)

                self.predict_img = Image.open("/Users/pyiheinsan/Desktop/tarot-project-main/career/{}.jpg".format(self.choosecard_name))
                self.predict_img_resize = self.predict_img.resize((800, 350), Image.Resampling.LANCZOS)
                self.predict_img_new = ImageTk.PhotoImage(self.predict_img_resize)

                self.canvasPredict = Canvas(self.win, width=800, height=350)
                self.canvasPredict.create_image(0, 0, anchor=NW, image=self.predict_img_new)
                self.canvasPredict.grid(row=6, column=1, rowspan=4, pady=30, padx=30)

            def card_creator():
                for i in range(7):
                    self.canvasDict["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(1000, card_delay)
                for i in range(8):
                    self.canvasDict2["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict2["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict2["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(2000, card_delay2)
                for i in range(7):
                    self.canvasDict3["canvas_{}".format(i)] = Canvas(self.win, width=100, height=200)
                    self.canvasDict3["canvas_{}".format(i)].create_image(0, 0, anchor=NW, image=self.new_img)
                    self.canvasDict3["canvas_{}".format(i)].bind("<Button-1>", chooseCard)
                    self.win.after(3000, card_delay3)

            card_creator()

            self.win.mainloop()

        def _exit():
            if ctlr.Controller._exit():
                for i in parent.winfo_children():
                    parent.destroy()
                    parent.quit()
                    if hasattr(parent, "win"):
                        parent.win.destroy()
                        parent.win.quit()
                else:
                    print("no")

        def _menu():
            self.bgimg = ImageTk.PhotoImage(Image.open('/Users/pyiheinsan/Desktop/tarot-project-main/tarot.jpg'))
            self.hdlb_mm = "Tarot Fortune Teller "
            self.hdlb = tk.Label(self, text=self.hdlb_mm, bg=parent.bgcolor, fg="White", font=('Times New Roman', 25, 'bold'))
            self.bgimglb = Label(self, i=self.bgimg, border="5")

            self.hdlb.grid(row=0, column=0, pady=10, padx=30)
            self.bgimglb.grid(row=1, column=0, rowspan=20, pady=5, padx=0)

            self.onecard_mm = "One Card Predict "
            self.onecard = tk.Button(self, text=self.onecard_mm, bg=parent.bgcolor, fg="blue", font=('Times New Roman', 14, 'bold'), command=_onecard)
            self.onecard.grid(row=1, column=1, pady=10, padx=20, sticky="nesw")

            self.txtp_mm = "Your Past Life "
            self.past = tk.Button(self, text=self.txtp_mm, bg=parent.bgcolor, fg="blue", font=('Times New Roman', 14, 'bold'), command=_past)
            self.past.grid(row=3, column=1, pady=10, padx=20, sticky="nesw")

            self.lov_mm = "Your Love Life "
            self.love = tk.Button(self, text=self.lov_mm, bg=parent.bgcolor, fg="blue", font=('Times New Roman', 14, 'bold'), command=_love)
            self.love.grid(row=5, column=1, pady=10, padx=20, sticky="nesw")

            self.edu_mm = "Your Education Path ?"
            self.education = tk.Button(self, text=self.edu_mm, bg=parent.bgcolor, fg="blue", font=('Times New Roman', 14, 'bold'), command=_education)
            self.education.grid(row=7, column=1, pady=10, padx=20, sticky="nesw")

            self.career_mm = "Your Career Path ?"
            self.career = tk.Button(self, text=self.career_mm, bg=parent.bgcolor, fg="blue", font=('Times New Roman', 14, 'bold'), command=_career)
            self.career.grid(row=9, column=1, pady=10, padx=20, sticky="nesw")

            self.exit_mm = "Exit"
            self.exit = tk.Button(self, text=self.exit_mm, bg=parent.bgcolor, fg="blue", font=('Times New Roman', 12, 'bold'), command=_exit)
            self.exit.grid(row=14, column=1, pady=10, padx=20, sticky="nesw")

            self.fgcolor = "blue"
            self.configure(bg=parent.bgcolor)

        _menu()

if __name__ == "__main__":
    view = View()
    view.mainloop()
