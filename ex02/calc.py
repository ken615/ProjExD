import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":

#ボタンを押したときの関数
    def button_click(event):
        btn = event.widget
        txt = btn["text"]#クリックされたボタン
        #=がクリックされたとき
        if txt == "=":
            try:
                eqn = entry.get()
                res = eval(eqn)
                entry.delete(0, tk.END)
                entry.insert(tk.END, res)
            except SyntaxError:
                pass

        #ACがクリックされたとき
        elif txt == "AC":
            entry.delete(0, tk.END)

        #bin+=がクリックされたとき
        elif txt == "bin+=":
            try:
                eqn = entry.get()
                res = eval(eqn)
                b_res = bin(res)#足し算の結果を2進数にする
                b_res = b_res[2:]#先頭の0bをとる
                entry.delete(0, tk.END)
                entry.insert(tk.END, b_res)
            except SyntaxError:
                pass

        #bin=がクリックされたとき
        elif txt == "bin=":
            try:
                eqn = entry.get()
                oprnds = eqn.split("+")#+を区切り文字として左オペランドと右オペランドに分割する。
                op1 = int(oprnds[0], 2)#左オペランドで、入力した2進数を10進数に直したもの
                op2 = int(oprnds[1], 2)#右オペランドで、入力した2進数を10進数に直したもの
                res = op1 + op2#10進数の計算
                b_res = bin(res)#計算結果を2進数に変換
                entry.delete(0, tk.END)#テキストを消去
                entry.insert(tk.END, b_res[2:])#計算結果の2進数を表示
            except ValueError:
                pass
            
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

    #ボタンの作成
    r = 1
    c = 0
    display = [9, 8, 7, "AC", 6, 5, 4, "-", 3, 2, 1, "+", 0, "bin+=", "bin=", "="]
    for i, d in enumerate(display, 0):
        button = tk.Button(root,
                           text = f"{d}",
                           width = 4,
                           height = 1,
                           font = ("Times New Roman", 30)
                           )
        button.bind("<1>", button_click)#ボタンをクリックしたとき
        button.bind("<Enter>", mouse_on)#マウスカーソルがボタンの上に来た時
        button.bind("<Leave>", mouse_out)#マウスカーソルがボタンから離れたとき
        button.grid(row = r, column = c)
        c += 1
        if (i + 1) % 4 == 0:
            c = 0
            r += 1

    #表示欄
    entry = tk.Entry(root, justify = "right", width = 12, font = ("Times New Roman", 40))
    entry.grid(row = 0, column = 0, columnspan = 5)


    root.mainloop()
