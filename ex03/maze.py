import tkinter as tk
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
    global cx, cy, mx, my, mz
    if key == "Up":
        if mz[my - 1][mx] == 0:#移動した先が0なら
            my -= 1
    if key == "Down":
        if mz[my + 1][mx] == 0:#移動した先が0なら
            my += 1
    if key == "Left":
        if mz[my][mx - 1] == 0:#移動した先が0なら
            mx -= 1
    if key == "Right":
        if mz[my][mx + 1] == 0:#移動した先が0なら
            mx += 1
    cx = mx * 100 + 50#マスの中心
    cy = my * 100 + 50#マスの中心
    canvas.coords("koka", cx, cy)
    root.after(100, main_proc)

#本文
if __name__ == "__main__":
    key = ""
    root = tk.Tk()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(100, main_proc)
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
    #こうかとん生成
    koka = tk.PhotoImage(file = "ex03/fig/3.png")
    cx, cy = mx*100 + 50, my*100 + 50
    canvas.create_image(cx, cy, image = koka, tag = "koka")
    #ウィンドウ生成
    root.mainloop()