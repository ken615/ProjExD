import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mzmk

#キーが押されたとき
def key_down(event):
    global key
    key = event.keysym

#キーが離れたとき
def key_up(event):
    global key
    key = ""

#キーが押されたときのこうかとんの動き
def main_proc():
    global cx, cy, mx, my, mz, koka
    if key == "Up":
        if mz[my - 1][mx] == 0:#移動した先が0なら進む
            my -= 1
        koka = tk.PhotoImage(file = "ex03/fig/4.png")
    if key == "Down":
        if mz[my + 1][mx] == 0:#移動した先が0なら進む
            my += 1
        koka = tk.PhotoImage(file = "ex03/fig/3.png")
    if key == "Left":
        if mz[my][mx - 1] == 0:#移動した先が0なら進む
            mx -= 1
        koka = tk.PhotoImage(file = "ex03/fig/0.png")
    if key == "Right":
        if mz[my][mx + 1] == 0:#移動した先が0なら進む
            mx += 1
        koka = tk.PhotoImage(file = "ex03/fig/2.png")
    cx = mx * 100 + 50#マスの中心
    cy = my * 100 + 50#マスの中心
    canvas.create_image(cx, cy, image = koka, tag = "koka")
    canvas.coords("koka", cx, cy)
    if (mx, my) == (13, 7):#ゴール地点に到達したら、
        root.after_cancel(jid)#count_down関数を停止する。（時間制限を停止する）
        tkm.showinfo("結果", f"残り{tmr}秒でゴール")#結果を表示
        quit()
    root.after(100, main_proc)

#時間制限を表す関数
def count_down():
    global tmr, jid
    tmr -= 1
    if tmr == 10:
        tkm.showinfo("報告", "あと10秒!")
    if tmr == 0:
        tkm.showinfo("報告", "残念! タイムアップ!")
        quit()
    jid = root.after(1000, count_down)#キャンセルできるようにjidに代入

#本文
if __name__ == "__main__":
    key = ""#押されたキーを保持する変数
    tmr = 20#経過時間を保持する変数
    root = tk.Tk()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(100, main_proc)
    root.bind("<KeyPress>")
    jid = root.after(1000, count_down)#キャンセルできるようにjidに代入しておく
    root.title("迷えるこうかとん")
    #背景
    canvas = tk.Canvas(root,
                       width = 1500,
                       height = 900,
                       bg = "black"
                      )
    canvas.pack()
    #迷路作成
    mz = mzmk.make_maze(15, 9)#1:壁/0:床
    mzmk.show_maze(canvas, mz)
    mx, my = 1, 1#マス
    canvas.create_rectangle(1300, 700, 1400, 800, fill = "blue")
    canvas.create_rectangle(100, 100, 200, 200, fill = "red")
    #こうかとん生成
    koka = tk.PhotoImage(file = "ex03/fig/1.png")
    cx, cy = mx*100 + 50, my*100 + 50
    canvas.create_image(cx, cy, image = koka, tag = "koka")
    #ウィンドウ生成
    root.mainloop()