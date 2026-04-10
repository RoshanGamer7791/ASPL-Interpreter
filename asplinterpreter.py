import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen
import io

root = tk.Tk()
root.geometry("1200x800")
root.title("Drawing Preview")
style = ttk.Style()
style.theme_use("clam")
canvas = tk.Canvas(root, bg="black")
canvas.place(x=0, y=0, width=1200, height=800)

font_style = "Arial"

def START(): ...
def PRINT(text: str):
    if "$" in text:
        url = text.strip("$")
        with urlopen(url) as response:
            contents = response.read().decode("utf-8")
        canvas.create_text(600, 400, fill="white", text=contents, font=(font_style, 10))
    else:
        canvas.create_text(600, 400, fill="white", text=text, font=(font_style, 10))

def SETFONT(font: str):
    global font_style
    font_style = font

def SPECIALTEXT(
    text: str, x: int, y: int, color: str):
    canvas.create_text(
        x, y, fill=color, text=text, font=(font_style, 10)
    )


def SQUARE(x1: int, y1: int, x2: int, y2: int, color: str):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)


def LINE(x1: int, y1: int, x2: int, y2: int, color: str, thickness: int):
    canvas.create_line(x1, y1, x2, y2, fill=color, width=thickness)


def TRI(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, color: str):
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)


def BGCOLOR(color: str):
    canvas.config(bg=color)


def PIXEL(x: int, y: int, color: str):
    canvas.create_rectangle(x, y, x, y, fill=color)


def END(): ...
def CREATEVAR(var, val):
    exec(f"{var} = {val}")


def SETVAR(var, val):
    exec(f"{var} = {val}")


def ADDVAR(var, val):
    exec(f"{var} += {val}")


def IMAGE(x: int, y: int, image_path: str, width: int, height: int):
    if "$" in image_path:
        url = image_path.strip("$")
        with urlopen(url) as response:
            imgcontent = response.read()
        imgdecoded = io.BytesIO(imgcontent)
        img = Image.open(imgdecoded)
        resizedimg = img.resize((width, height))
        imgtk = ImageTk.PhotoImage(resizedimg)
        label = tk.Label(canvas, image=imgtk)
        label.image = imgtk
        label.place(x=x, y=y)
    else:
        img = Image.open(image_path)
        resizedimg = img.resize((width, height))
        imgtk = ImageTk.PhotoImage(resizedimg)
        label = tk.Label(canvas, image=imgtk)
        label.image = imgtk
        label.place(x=x, y=y)


import file

root.mainloop()
1
