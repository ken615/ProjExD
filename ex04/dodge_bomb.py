import pygame as pg
import sys
import random

def main():
    #時間計測用
    clock = pg.time.Clock()

    #基本画面
    pg.display.set_caption("逃げろ！こうかとん")#タイトルの設定
    screen = pg.display.set_mode((1600, 900))#1600x900のSurface
    screen_rect = screen.get_rect()#screenのRect
    background = pg.image.load("fig/pg_bg.jpg")#背景画像のSurface
    bg_rect = background.get_rect()#backgroundのRect
    screen.blit(background, bg_rect)#背景をscreenに張り付ける

    #こうかとんの画像
    tori_img = pg.image.load("fig/6.png")#Surfaceクラスオブジェクト
    tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)#tori_imgを2.0倍の大きさに
    tori_rect = tori_img.get_rect()#Rectクラスオブジェクト
    tori_rect.center = (900, 400)#900,400に表示

    #爆弾
    bomb_img = pg.Surface((20, 20))#Surface
    bomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), (10))
    bomb_rect = bomb_img.get_rect()#Rect
    bomb_rect.centerx = random.randint(0, screen_rect.width)#screen内のランダムな位置に生成
    bomb_rect.centery = random.randint(0, screen_rect.height)#screen内のランダムな位置に生成
    vx = +1#爆弾の横方向の速度
    vy = +1#爆弾の縦方向の速度

    while True:
        screen.blit(background, bg_rect)#背景をscreenに張り付ける

        for event in pg.event.get():#イベントを繰り返し処理
            if event.type == pg.QUIT: return
        

        key_list = pg.key.get_pressed()#すべてのキーの入力状態を保持
        if key_list[pg.K_UP] == True: tori_rect.centery -= 1
        if key_list[pg.K_DOWN] == True: tori_rect.centery += 1
        if key_list[pg.K_LEFT] == True: tori_rect.centerx -= 1
        if key_list[pg.K_RIGHT] == True: tori_rect.centerx += 1
        screen.blit(tori_img, tori_rect)#こうかとんをscreenに張り付ける

        bomb_rect.move_ip(vx, vy)
        screen.blit(bomb_img, bomb_rect)#爆弾をscreenに張り付ける

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()#モジュールを初期化（開始）
    main()
    pg.quit()#モジュールの初期化を解除（終了）
    sys.exit()#プログラムの終了