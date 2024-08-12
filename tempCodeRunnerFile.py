from tkinter import * 
from tkinter.ttk import *

import tkinter as tk 
import tkinter.ttk as ttk 

from view import * 
import view as vw

#import Image
#import ImageTk
from PIL import ImageTk, Image 


class App(tk.Tk):
	def __init__(self,*args,**kwargs):
		super().__init__()
		def initiating():
			self.bgcolor = "#404040"
			self.geometry("1200x600+100+50")
			self.configure(bg=self.bgcolor)
			self.title("Tarot Fortune Teller")
			self.attributes("-fullscreen",-1)
		initiating()
		v = vw.View(self)
		v.grid(row=0,column=0,pady=40,padx=100)


if __name__ == "__main__":
	app = App()
	app.mainloop()


