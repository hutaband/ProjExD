import math
import tkinter as tk
from tkinter import font
import maze_maker as mm
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}キーが押されました")

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx,my,cx,cy,time
    time = time-0.1
    if time < 0:
        tkm.showinfo("迷えるこうかとん","GAMEOVER")
        return 
               #１秒ずつ減る
    #delta = {"Up"   : [0,-20],
    #         "Down" : [0,+20],
    #         "Left" : [-20,0],
    #         "Right": [+20,0],
    #         ""     : [0,  0],
    # }
    
    #cx,cy = cx+delta[key][0],cy+delta[key][1]
    #canvas.coords("tori",cx,cy)
    # root.after(100)   
    if key == "Up" and maze_bg[my-1][mx] == 0:
        my -= 1
    elif key == "Down" and maze_bg[my+1][mx] == 0:
        my += 1
    elif key == "Left" and maze_bg[my][mx-1] == 0:
        mx -= 1
    elif key == "Right" and maze_bg[my][mx+1] == 0:
        mx += 1

    cx, cy = mx*100+50,my*100+50  
    canvas.coords("tori",cx,cy) 
    label_2["text"]=math.floor(time)
    if label_2["text"] == 0:          #制限時間
        time = 0
    root.after(100,main_proc)


if __name__ == "__main__":
    time = 10
    root = tk.Tk()
    #root.geometry("1500x900")
    #root.configure(bg="black")
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()

    maze_bg = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg)
    label_1 = tk.Label(root,text="スタート")   #スタート位置
    label_1.place(x = 100,y = 100)
    label_2 = tk.Label(root,text = time,font=("MSゴシック",30))   #時間表示
    label_2.place(x = 750,y = 50)
    label_3 = tk.Label(root,text="GAMEOVER")    #ゲームオーバー
    tori = tk.PhotoImage(file="fig/3.png")
    mx, my = 1,1
    cx,cy = mx*100+50,my*100+50
    canvas.create_image(mx,my,image=tori,tag="tori")
    key = " "
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()