import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")#タイトルの設定
    screen = pg.display.set_mode((1600, 900))#1600x900のSurface
    screen_rect = screen.get_rect()#screenのRect
    background = pg.image.load("fig/pg_bg.jpg")#背景画像のSurface
    bg_rect = background.get_rect()#backgroundのRect
    screen.blit(background, bg_rect)#背景をscreenに張り付ける

    pg.display.update()
    clock.tick(0.5)


if __name__ == "__main__":
    pg.init()#モジュールを初期化（開始）
    main()
    pg.quit()#モジュールの初期化を解除（終了）
    sys.exit()#プログラムの終了