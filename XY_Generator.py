from tkinter import *

# 處理隨機生成
import random
# 處理複製的功能
import pyperclip

# 基本設定
win = Tk()
win.title("Random X,Y Generator")
# win.geometry(長x寬 +X +Y)
win.geometry("800x720+500+200")
win.config(bg="#323232")
# 透明度
win.attributes("-alpha",0.8) #1~0 1=100% 0=0%

# ////////////////////////////////////////// #
## Part 0 (插入圖片用的)
img = PhotoImage(file="C:\\Users\\William\\Downloads\\3654.png")
btn = Button(text="")
btn.config(image = img)
btn.pack() # 按鈕顯示用
## Part I
title_text = Label(bg="#323232",fg="skyblue",text="Random X,Y Generator")
# obj.config(font="字型 大小")
title_text.config(font="微軟正黑體 15")
title_text.pack()
## Part II
min_range = Label(bg="#323232",fg="white",text="Min range")
min_range.pack()
min_entry = Entry()
min_entry.pack()
## Part III
max_range = Label(bg="#323232",fg="white",text="Max range")
max_range.pack()
max_entry = Entry()
max_entry.pack()

x_show = Label(bg="#323232",fg="white",text="")
x_show.pack()
y_show = Label(bg="#323232",fg="white",text="")
y_show.pack()

def gen_xy():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    # random.randint(min,max)
    x = str(random.randint(min_val,max_val))
    y = str(random.randint(min_val,max_val))
    x_show.config(text="X:" + x)
    y_show.config(text="Y:" + y)

def copy():
    xy = x_show.cget("text") + y_show.cget("text")
    pyperclip.copy(xy)

generate_btn = Button(text="Generate !",command=gen_xy)
generate_btn.pack()
copy_btn = Button(text="Copy !",command=copy)
copy_btn.pack()

win.mainloop() # 常駐主視窗