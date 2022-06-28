import tkinter as tk

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
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canvas.coords("koka", cx + 20, cy)
    root.after(100, main_proc)

#本文
if __name__ == "__main__":
    key = ""
    root = tk.Tk()
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(100, main_proc)
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,
                       width = 1500,
                       height = 900,
                       bg = "black"
                      )
    canvas.pack()
    koka = tk.PhotoImage(file = "ex03/fig/3.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image = koka, tag = "koka")

    root.mainloop()