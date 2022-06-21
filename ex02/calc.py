import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":

    def button_click(event):
        btn = event.widget
        txt = btn["text"]#クリックされたボタン
        if txt == "=":
            eqn = entry.get()
            res = eval(eqn)
            entry.delete(0, tk.END)
            entry.insert(tk.END, res)
        #tkm.showinfo("報告", f"{txt}のボタンがクリックされました。")
        else:
            entry.insert(tk.END, f"{txt}")

    root = tk.Tk()
    root.title("calc")
    root.geometry("300x550")#ウィンドウの表示

    #grid()のための変数r=row, c=column
    r = 1
    c = 0

    #数字のボタン
    for i in range(9, -1, -1):
        button = tk.Button(root, text = f"{i}", width = 4, height = 2, 
                           font = ("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row = r, column = c)
        c += 1
        if ((i - 1) % 3) == 0:
            r += 1
            c = 0
    
    #+のボタン
    button = tk.Button(root, text = "+", width = 4, height = 2, 
                           font = ("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.grid(row = r, column = c)

    #=のボタン
    button = tk.Button(root, text = "=", width = 4, height = 2, 
                           font = ("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.grid(row = r, column = c + 1)

    #表示欄
    entry = tk.Entry(root, justify = "right", width = 10, font = ("Times New Roman", 40))
    entry.grid(row = 0, column = 0, columnspan = 3)


    root.mainloop()
