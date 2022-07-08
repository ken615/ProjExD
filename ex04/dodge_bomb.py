import pygame as pg
import sys
import random
import tkinter.messagebox as tkm

def main():
    #時間計測用
    clock = pg.time.Clock()

    #基本画面
    pg.display.set_caption("Escape from bombs")#タイトルの設定
    screen = pg.display.set_mode((1280, 680))#1600x900のSurface
    screen_rect = screen.get_rect()#screenのRect
    background = pg.image.load("fig/pg_bg.jpg")#背景画像のSurface
    bg_rect = background.get_rect()#backgroundのRect
    screen.blit(background, bg_rect)#背景をscreenに張り付ける

    #こうかとんの画像
    tori_img = pg.image.load("fig/6.png")#Surfaceクラスオブジェクト
    tori_img = pg.transform.rotozoom(tori_img, 0, 1.5)#tori_imgを2.0倍の大きさに
    tori_rect = tori_img.get_rect()#Rectクラスオブジェクト
    tori_rect.center = (900, 400)#900,400に表示
    rev = False#移動方向反転のフラグ

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
    rbomb_img = pg.Surface((20, 20))#Surface
    rbomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(rbomb_img, (0, 0, 255), (10,10), (10))
    rbomb_rect = rbomb_img.get_rect()#Rect
    rbomb_rect.centerx = screen_rect.width/2
    rbomb_rect.centery = screen_rect.height/2
    rvx = +1
    rvy = +1   
    pg.time.set_timer(30, 500)#500msごとに青爆弾の向きをランダムに変える。
    
    #爆弾黄
    ybomb_img = pg.Surface((20, 20))#Surface
    ybomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(ybomb_img, (255, 255, 0), (10, 10), (10))#黄色の半径10の円
    ybomb_rect = ybomb_img.get_rect()#Rect
    ybomb_rect.centerx = screen_rect.width/2
    ybomb_rect.centery = screen_rect.height/2
    yvx = 1
    yvy = 1 
    pg.time.set_timer(31, 200)#500msごとに黄爆弾の向きをこうかとんの方向に変える。

    #アイテム
    item_img = pg.image.load("fig/hatena.jpeg")#Surface
    item_img = pg.transform.rotozoom(item_img, 0, 0.1)
    item_rect = item_img.get_rect()#Rect
    item_rect.centerx = random.randint(0, screen_rect.width)#screen内のランダムな位置に生成
    item_rect.centery = random.randint(0, screen_rect.height)#screen内のランダムな位置に生成
    ivx = 1
    ivy = 1


    while True:
        screen.blit(background, bg_rect)#背景をscreenに張り付ける

        for event in pg.event.get():#イベントを繰り返し処理
            if event.type == pg.QUIT: return
            if event.type == 30:
                rx = random.randint(0,1)#0なら+方向、1なら-方向に向きをかえる
                ry = random.randint(0,1)#0なら+方向、1なら-方向に向きを変える
                if rx == 0 and ry == 0: rvx *= 1; rvy *= 1
                elif rx == 0 and ry == 1: rvx *= 1; rvy *= -1
                elif rx == 1 and ry == 0: rvx *= -1; rvy *= 1
                elif rx == 1 and ry == 1: rvx *= -1; rvy *= -1
            if event.type == 31:
                yoko, tate = search_tori(ybomb_rect, tori_rect)#爆弾黄に対してのこうかとんの位置を判定
                yvx = yoko #移動方向
                yvy = tate #移動方向

        key_list = pg.key.get_pressed()#すべてのキーの入力状態を保持
        if rev == False:#反転が無効なら
            if key_list[pg.K_UP] == True: tori_rect.centery -= 2#上キーを入力したらこうかとんを上に移動
            if key_list[pg.K_DOWN] == True: tori_rect.centery += 2#下キーを入力したらこうかとんを下に移動
            if key_list[pg.K_LEFT] == True: tori_rect.centerx -= 2#左キーを入力したらこうかとんを左に移動
            if key_list[pg.K_RIGHT] == True: tori_rect.centerx += 2#右キーを入力したらこうかとんを右に移動
            if check_bound(tori_rect, screen_rect) != (1, 1):#移動先が画面外なら
                if key_list[pg.K_UP] == True: tori_rect.centery += 2#画面外なら上キーを押しても下に移動
                if key_list[pg.K_DOWN] == True: tori_rect.centery -= 2#画面外なら下キーを押しても上に移動
                if key_list[pg.K_LEFT] == True: tori_rect.centerx += 2#画面外なら左キーを押しても右に移動
                if key_list[pg.K_RIGHT] == True: tori_rect.centerx -= 2#画面外なら右キーを押しても左に移動
        elif rev == True:#反転が有効なら
            if key_list[pg.K_UP] == True: tori_rect.centery += 2#画面外なら上キーを押しても下に移動
            if key_list[pg.K_DOWN] == True: tori_rect.centery -= 2#画面外なら下キーを押しても上に移動
            if key_list[pg.K_LEFT] == True: tori_rect.centerx += 2#画面外なら左キーを押しても右に移動
            if key_list[pg.K_RIGHT] == True: tori_rect.centerx -= 2#画面外なら右キーを押しても左に移動
            if check_bound(tori_rect, screen_rect) != (1, 1):#移動先が画面外なら
                if key_list[pg.K_UP] == True: tori_rect.centery -= 2#画面外なら上キーを押しても下に移動
                if key_list[pg.K_DOWN] == True: tori_rect.centery += 2#画面外なら下キーを押しても上に移動
                if key_list[pg.K_LEFT] == True: tori_rect.centerx -= 2#画面外なら左キーを押しても右に移動
                if key_list[pg.K_RIGHT] == True: tori_rect.centerx += 2#画面外なら右キーを押しても左に移動
        screen.blit(tori_img, tori_rect)#こうかとんをscreenに張り付ける
        screen.blit(item_img, item_rect)#アイテムをscreenに貼り付ける
        item_rect.move_ip(ivx, ivy)#アイテムを移動させる
        yoko, tate = check_bound(item_rect, screen_rect)#アイテムのスクリーン外判定
        ivx *= yoko
        ivy *= tate

        bomb_rect.move_ip(vx, vy)#爆弾赤を移動させる
        screen.blit(bomb_img, bomb_rect)#爆弾赤をscreenに張り付ける
        screen.blit(ybomb_img, ybomb_rect)#爆弾黄をscreenに張り付ける
        screen.blit(rbomb_img, rbomb_rect)#爆弾青をscreenに張り付ける
        yoko, tate = check_bound(bomb_rect, screen_rect)#爆弾赤のスクリーン外判定
        vx *= yoko
        vy *= tate

        now = pg.time.get_ticks()
        if now > 10000:#開始から10秒たったら
            rbomb_rect.move_ip(rvx, rvy)#爆弾青を移動させる
            screen.blit(rbomb_img, rbomb_rect)#爆弾青をscreenに張り付ける
            yoko, tate = check_bound(rbomb_rect, screen_rect)
            rvx *= yoko
            rvy *= tate
        if now > 20000:#開始から20秒たったら
            ybomb_rect.move_ip(yvx, yvy)#爆弾黄を移動させる
            screen.blit(ybomb_img, ybomb_rect)#爆弾黄をscreenに張り付ける
            

            
        if item_rect.colliderect(tori_rect):
            #アイテム
            item_img = pg.image.load("fig/hatena.jpeg")#Surface
            item_img = pg.transform.rotozoom(item_img, 0, 0.1)
            item_rect = item_img.get_rect()#Rect
            item_rect.centerx = random.randint(0, screen_rect.width)#screen内のランダムな位置に生成
            item_rect.centery = random.randint(0, screen_rect.height)#screen内のランダムな位置に生成
            if rev == True: rev = False
            elif rev == False: rev = True
        if bomb_rect.colliderect(tori_rect): 
            tkm.showinfo("ゲームオーバー", f"ゲームオーバー！\n記録:{pg.time.get_ticks() // 1000}秒！")
            return#こうかとんと爆弾赤が接触したら終了      
        if rbomb_rect.colliderect(tori_rect): 
            tkm.showinfo("ゲームオーバー", f"ゲームオーバー！\n記録:{pg.time.get_ticks() // 1000}秒！")
            return#こうかとんと爆弾青が接触したら終了
        if ybomb_rect.colliderect(tori_rect): 
            tkm.showinfo("ゲームオーバー", f"ゲームオーバー！\n記録:{pg.time.get_ticks() // 1000}秒！")
            return#こうかとんと爆弾黄が接触したら終了黄
        pg.display.update()
        clock.tick(1000)


#領域外に出たかどうかの判定をする関数
def check_bound(rect, scr_rect):#第一引数はこうかとんと爆弾のrect、第二引数はスクリーンのrect
    yoko, tate = +1, +1#領域内
    if rect.left < scr_rect.left or scr_rect.right < rect.right: yoko *= -1#領域外
    if rect.top < scr_rect.top or scr_rect.bottom < rect.bottom: tate *= -1#領域外
    return (yoko, tate)

#自分から見てこうかとんがどの方向にいるかを判定する関数
def search_tori(myposi, toriposi):
    yoko, tate = 1, 1#移動方向の指定
    if myposi.centerx < toriposi.centerx and myposi.centery < toriposi.centery: yoko, tate = 1, 1#こうかとんの方が右下にあるとき
    if myposi.centerx < toriposi.centerx and myposi.centery > toriposi.centery: yoko, tate = 1, -1#こうかとんの方が右上にあるとき
    if myposi.centerx < toriposi.centerx and myposi.centery == toriposi.centery: yoko, tate = 1, 0#こうかとんが真右にあるとき
    if myposi.centerx > toriposi.centerx and myposi.centery < toriposi.centery: yoko, tate = -1, 1#こうかとんの方が左下にあるとき
    if myposi.centerx > toriposi.centerx and myposi.centery > toriposi.centery: yoko, tate = -1, -1#こうかとんの方が左上にあるとき
    if myposi.centerx > toriposi.centerx and myposi.centery == toriposi.centery: yoko, tate = -1, 0#こうかとんが真左にあるとき
    if myposi.centerx == toriposi.centerx and myposi.centery < toriposi.centery: yoko, tate = 0, 1#こうかとんが真下にあるとき
    if myposi.centerx == toriposi.centerx and myposi.centery > toriposi.centery: yoko, tate = 0, -1#こうかとんが真上にあるとき
    return (yoko, tate)


if __name__ == "__main__":
    pg.init()#モジュールを初期化（開始）
    main()
    pg.quit()#モジュールの初期化を解除（終了）
    sys.exit()#プログラムの終了