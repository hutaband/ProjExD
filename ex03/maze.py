import tkinter as tk

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}キーが押されました")

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy
    #delta = {"Up"   : [0,-20],
    #         "Down" : [0,+20],
    #         "Left" : [-20,0],
    #         "Right": [+20,0],
    #         ""     : [0,  0],
    # }
    
    #cx,cy = cx+delta[key][0],cy+delta[key][1]
    #canvas.coords("tori",cx,cy)
    # root.after(100)   
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20  
    canvas.coords("tori",cx,cy) 
    root.after(20,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("1500x900")
    #root.configure(bg="black")
    root.title("迷えるこうかとん")
    
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    
    tori = tk.PhotoImage(file="fig/3.png")
    cx, cy = 300,400
    canvas.create_image(cx,cy,image=tori,tag="tori")
    key = " "
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()