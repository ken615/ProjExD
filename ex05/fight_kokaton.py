import pygame as pg
import sys
import random

def main():
    clock = pg.time.Clock()

    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")#スクリーン
    scr.blit()#スクリーンの貼り付け
    kkt = Bird("fig/6.png", 2.0, (900, 400))#こうかとん生成
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)#爆弾生成
    ball = 0

    while True:
        scr.blit()#背景の貼り付け

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_w:
                ball = Shot((0, 255, 0), 10, (0, -2), kkt)
            if event.type == pg.KEYDOWN and event.key == pg.K_a:
                ball = Shot((0, 255, 0), 10, (-2, 0), kkt)
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                ball = Shot((0, 255, 0), 10, (0, 2), kkt)
            if event.type == pg.KEYDOWN and event.key == pg.K_d:
                ball = Shot((0, 255, 0), 10, (2, 0), kkt)

        kkt.update(scr)#こうかとんの動き
        bkd.update(scr)#爆弾の動き
        if ball != 0:
            ball.update(scr)

        if kkt.rct.colliderect(bkd.rct):
            return
        if ball != 0:
            if ball.rct.colliderect(bkd.rct):
                return
        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


#Screenクラス
class Screen:
    #コンストラクタ
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)      # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.bgi_sfc = pg.image.load(image)     # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()  # Rect

    #インスタンスメソッド
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


#Birdクラス
class Bird:
    #クラス変数
    #コンストラクタ
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    #インスタンスメソッド
    def blit(self, scr: Screen):#（: 型）で型を指定できる。
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN]: 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)


#Bombクラス
class Bomb:
    #コンストラクタ
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2 * size, 2 * size)) # Surface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    #インスタンスメソッド
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        scr.sfc.blit(self.sfc, self.rct)      


#Shotクラス
class Shot:
    #コンストラクタ
    def __init__(self, color, size, vxy, bird):
        self.sfc = pg.Surface((2 * size, 2 * size))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect()
        self.rct.center = bird.rct.center
        self.vx, self.vy = vxy

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        if check_bound(self.rct, scr.rct) != (1, 1):
            self = 0
            return
        scr.sfc.blit(self.sfc, self.rct)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()