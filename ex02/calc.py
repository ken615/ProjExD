import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":

#ボタンを押したときの関数
    def button_click(event):
        btn = event.widget
        txt = btn["text"]#クリックされたボタン
        #=がクリックされたとき
        if txt == "=":
            eqn = entry.get()
            res = eval(eqn)
            entry.delete(0, tk.END)
            entry.insert(tk.END, res)

        #ACがクリックされたとき
        elif txt == "AC":
            entry.delete(0, tk.END)

        #bin+=がクリックされたとき
        elif txt == "bin+=":
            eqn = entry.get()
            res = eval(eqn)
            b_res = bin(res)#足し算の結果を2進数にする
            b_res = b_res[2:]#先頭の0bをとる
            entry.delete(0, tk.END)
            entry.insert(tk.END, b_res)

        #2-2がクリックされたとき
        elif txt == "2-2":
            eqn = entry.get()
            oprnds = eqn.split("+")#+を区切り文字として左オペランドと右オペランドに分割する。
            op1 = int(oprnds[0], 2)#左オペランドで、入力した2進数を10進数に直したもの
            op2 = int(oprnds[1], 2)#右オペランドで、入力した2進数を10進数に直したもの
            res = op1 + op2#10進数の計算
            b_res = bin(res)#計算結果を2進数に変換
            entry.delete(0, tk.END)#テキストを消去
            entry.insert(tk.END, b_res[2:])#計算結果の2進数を表示
            
        #それ以外の時
        else:
            entry.insert(tk.END, f"{txt}")

    #マウスカーソルがボタンに乗ったら色を変える
    def mouse_on(event):
        event.widget["bg"] = "#ffffbf"

    #マウスカーソルがボタンから離れたら色を戻す
    def mouse_out(event):
        event.widget["bg"] = "SystemButtonFace"

            
    root = tk.Tk()
    root.title("すごそうな電卓")
    #root.geometry("300x550")#ウィンドウの表示

    #grid()のための変数r=row, c=column
    r = 1
    c = 0

    #数字のボタン
    for i in range(9, -1, -1):
        button = tk.Button(root, text = f"{i}", width = 4, height = 1, 
                           font = ("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.bind("<Enter>", mouse_on)
        button.bind("<Leave>", mouse_out)
        button.grid(row = r, column = c)
        c += 1
        if ((i - 1) % 3) == 0:
            r += 1
            c = 0
    
    #+のボタン
    button = tk.Button(root, text = "+", width = 4, height = 1, 
                           font = ("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.bind("<Enter>", mouse_on)
    button.bind("<Leave>", mouse_out)
    button.grid(row = r, column = c)

    #=のボタン
    button = tk.Button(root, text = "=", width = 4, height = 1, 
                           font = ("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.bind("<Enter>", mouse_on)
    button.bind("<Leave>", mouse_out)
    button.grid(row = r, column = c + 1)

    #AC(オールクリア)のボタン
    button = tk.Button(root, text = "AC", width = 4, height = 1, 
                           font = ("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.bind("<Enter>", mouse_on)
    button.bind("<Leave>", mouse_out)
    button.grid(row = r + 1, column = 0)

    #計算結果を2進数にするボタン
    button = tk.Button(root, text = "bin+=", width = 4, height = 1, 
                           font = ("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.bind("<Enter>", mouse_on)
    button.bind("<Leave>", mouse_out)
    button.grid(row = r + 1, column = 1)

    #2進数同士の計算をするボタン
    button = tk.Button(root, text = "2-2", width = 4, height = 1,
                        font = ("Times New Roman", 30))
    button.bind("<1>", button_click)
    button.bind("<Enter>", mouse_on)
    button.bind("<Leave>", mouse_out)
    button.grid(row = r + 1, column = 2)

    #表示欄
    entry = tk.Entry(root, justify = "right", width = 10, font = ("Times New Roman", 40))
    entry.grid(row = 0, column = 0, columnspan = 3)


    root.mainloop()
