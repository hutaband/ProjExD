import random
import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn = event.widget
    x = btn["text"]
    if x == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END, res)
    elif x == "C":
        entry.delete(0,tk.END)
    elif x == "Q":
        h = ["*","+","-","/"]
        a = random.randint(1,9)
        b = random.randint(1,9)
        c = random.choice(h)
        ques = f"{str(a)} {c} {str(b)}"
        entry.delete(0,tk.END)
        entry.insert(tk.END,ques)
    #elif x == "%":
        #eqn = entry.get()
    #    par = "{:.0%}".format(entry)
    #    pa = str(par)
    #    entry.delete(0,tk.END)
    #    entry.insert(tk.END,pa)


    else:

    #tkm.showinfo("",f"{x}のボタンがクリックされました")
        entry.insert(tk.END, x)

#def button_sum(sum):
  #  btn2 = sum.widget["text"]
 #   if btn2 == "=":




if __name__ == "__main__":
    #calc_list = [0,1,2,3,4,5,6,7,8,9]
    root = tk.Tk()
    #root.geometry("300x500")
    root.title("超高性能電卓")

    entry = tk.Entry(root,justify="right",width=20,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=4)
    
    r,c = 1,0
    for i,x in enumerate([1,2,3,"C",4,5,6,"=",7,8,9,"*","+",0,"-"]+["/","%","Q"]):
        btn = tk.Button(root,text=x,width=6,height=1, font=("Times New Roman",30))
        btn.grid(row=r,column=c)
        c += 1
        if (i+1)%4 == 0:
            r += 1
            c = 0
        btn.bind("<1>", button_click)


    root = tk.mainloop()