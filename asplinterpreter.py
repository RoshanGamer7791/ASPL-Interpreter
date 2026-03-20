import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")
root.title("Drawing Preview")
style = ttk.Style()
style.theme_use("clam")
canvas = tk.Canvas(root, bg="black")
canvas.place(x=0, y=0, width=800, height=600)
def PRINT(text: str):
    print(text)

def SQUARE(x1:int, y1:int, x2:int, y2:int, color:str):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)
def LINE(x1:int, y1:int, x2:int, y2:int, color:str, thickness:int):
    canvas.create_line(x1, y1, x2, y2, fill=color, width=thickness)
def TRI(x1:int, y1:int, x2:int, y2:int, x3:int, y3:int, color:str):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)
def BGCOLOR(color:str):
    canvas.config(bg=color)
def PIXEL(x:int, y:int, color:str):
    canvas.create_rectangle(x, y, x, y, fill=color)
import file

root.mainloop()