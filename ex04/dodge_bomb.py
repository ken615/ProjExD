import pygame as pg
import sys
import random

def main():
    #時間計測用
    clock = pg.time.Clock()

    #基本画面
    pg.display.set_caption("Escape from blue bomb")#タイトルの設定
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

    #爆弾赤
    bomb_img = pg.Surface((20, 20))#Surface
    bomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), (10))
    bomb_rect = bomb_img.get_rect()#Rect
    bomb_rect.centerx = random.randint(0, screen_rect.width)#screen内のランダムな位置に生成
    bomb_rect.centery = random.randint(0, screen_rect.height)#screen内のランダムな位置に生成
    vx = +1#爆弾の横方向の速度
    vy = +1#爆弾の縦方向の速度

    #爆弾青
    rbomb_img = pg.Surface((50, 50))#Surface
    rbomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(rbomb_img, (0, 0, 255), (25,25), (25))
    rbomb_rect = rbomb_img.get_rect()#Rect
    rbomb_rect.centerx = screen_rect.width/2
    rbomb_rect.centery = screen_rect.height/2
    rvx = +9
    rvy = +9    


    while True:
        screen.blit(background, bg_rect)#背景をscreenに張り付ける

        for event in pg.event.get():#イベントを繰り返し処理
            if event.type == pg.QUIT: return
        

        key_list = pg.key.get_pressed()#すべてのキーの入力状態を保持
        if key_list[pg.K_UP] == True: tori_rect.centery -= 1#上キーを入力したらこうかとんを上に移動
        if key_list[pg.K_DOWN] == True: tori_rect.centery += 1#下キーを入力したらこうかとんを下に移動
        if key_list[pg.K_LEFT] == True: tori_rect.centerx -= 1#左キーを入力したらこうかとんを左に移動
        if key_list[pg.K_RIGHT] == True: tori_rect.centerx += 1#右キーを入力したらこうかとんを右に移動
        if check_bound(tori_rect, screen_rect) != (1, 1):
            if key_list[pg.K_UP] == True: tori_rect.centery += 1#上キーを入力したらこうかとんを上に移動
            if key_list[pg.K_DOWN] == True: tori_rect.centery -= 1#下キーを入力したらこうかとんを下に移動
            if key_list[pg.K_LEFT] == True: tori_rect.centerx += 1#左キーを入力したらこうかとんを左に移動
            if key_list[pg.K_RIGHT] == True: tori_rect.centerx -= 1
        screen.blit(tori_img, tori_rect)#こうかとんをscreenに張り付ける

        bomb_rect.move_ip(vx, vy)#爆弾赤を移動させる
        screen.blit(bomb_img, bomb_rect)#爆弾赤をscreenに張り付ける
        screen.blit(rbomb_img, rbomb_rect)#爆弾青をscreenに張り付ける
        yoko, tate = check_bound(bomb_rect, screen_rect)
        vx *= yoko
        vy *= tate

        now = pg.time.get_ticks()
        if now > 10000:
            rbomb_rect.move_ip(rvx, rvy)#爆弾青を移動させる
            screen.blit(rbomb_img, rbomb_rect)#爆弾青をscreenに張り付ける
            yoko, tate = check_bound(rbomb_rect, screen_rect)
            rvx *= yoko
            rvy *= tate
            rx = random.randint(0,1)#0なら+方向、1なら-方向に向きをかえる
            ry = random.randint(0,1)#0なら+方向、1なら-方向に向きを変える
            if rx == 0 and ry == 0: rvx *= 1; rvy *= 1
            elif rx == 0 and ry == 1: rvx *= 1; rvy *= -1
            elif rx == 1 and ry == 0: rvx *= -1; rvy *= 1
            elif rx == 1 and ry == 1: rvx *= -1; rvy *= -1
            

        if bomb_rect.colliderect(tori_rect): return#こうかとんと爆弾赤が接触したら終了            
        if rbomb_rect.colliderect(tori_rect): return#こうかとんと爆弾青が接触したら終了
        pg.display.update()
        clock.tick(1000)


#領域外に出たかどうかの判定をする関数
def check_bound(rect, scr_rect):#第一引数はこうかとんと爆弾のrect、第二引数はスクリーンのrect
    yoko, tate = +1, +1#領域内
    if rect.left < scr_rect.left or scr_rect.right < rect.right: yoko *= -1#領域外
    if rect.top < scr_rect.top or scr_rect.bottom < rect.bottom: tate *= -1#領域外
    return (yoko, tate)


if __name__ == "__main__":
    pg.init()#モジュールを初期化（開始）
    main()
    pg.quit()#モジュールの初期化を解除（終了）
    sys.exit()#プログラムの終了