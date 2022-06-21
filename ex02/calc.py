import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget
    x = btn["text"]
    #tkm.showinfo("",f"{x}のボタンがクリックされました")
    entry.insert(tk.END, x)


if __name__ == "__main__":
    #calc_list = [0,1,2,3,4,5,6,7,8,9]
    root = tk.Tk()
    #root.geometry("300x500")
    root.title("超高性能電卓")

    entry = tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)

    r,c = 1,0
    for x in range(9,-1,-1):
        btn = tk.Button(root,text=x,width=4,height=2, font=("Times New Roman",30))
        btn.grid(row=r,column=c)
        c += 1
        if (x-1)%3 == 0:
            r += 1
            c = 0
        btn.bind("<1>", button_click)


    root = tk.mainloop()