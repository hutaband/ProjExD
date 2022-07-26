import random
import sys
import pygame as pg


class Screen:
    def __init__(self, title, wh, image):  
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     #
        self.rct = self.sfc.get_rect()         
        self.bgi_sfc = pg.image.load(image)    
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

    def text_blit(self,text,t_x,t_y):
        self.sfc.blit(text,[t_x,t_y])


class Racket:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1
        
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 1
        self.blit(scr)


class Ball:  #ボール生成
    def __init__(self, fname, rack):
        self.image = pg.image.load(fname).convert_alpha()
        self.image = pg.transform.scale(self.image,(50,50))
        self.rct = self.image.get_rect()
        self.v_x = 1
        self.v_y = 1
        self.racket = rack

    def ball_move(self, scr: Screen): #ボールの挙動
        self.rct.centerx += int(self.v_x)
        self.rct.centery += int(self.v_y)

        if self.rct.left < scr.rct.left:
            self.rct.left = scr.rct.left
            self.v_x = -self.v_x
        if self.rct.right > scr.rct.right:
            self.rct.right = scr.rct.right
            self.v_x = -self.v_x
        if self.rct.top < scr.rct.top:
            self.rct.top = scr.rct.top
            self.v_y = -self.v_y

        if self.rct.colliderect(self.racket.rct): #ボールとバーの衝突
            dist = self.rct.centerx - self.racket.rct.centerx
            if dist < 0:
                self.v_x = -1
            elif dist > 0:
                self.v_x = 1
            else:
                self.v_x = random.randint(-5,5)
            self.v_y = -1

        if self.rct.bottom > scr.rct.bottom: #ボールが画面の下に行った場合
            font = pg.font.Font(None, 100)
            text = font.render("GAME OVER", True,(255,0,0))
            scr.text_blit(text, 400,200)


    def draw(self, sfc): #ボールの描画
        sfc.blit(self.image, self.rct)


    def update(self,scr:Screen): #更新
        scr.sfc.blit(self.image,self.rct)

def main(): #メイン関数
    clock = pg.time.Clock()
    scr = Screen("squash", (1200, 600), "fig/haikei.png") #スクリーン設定
    rack = Racket("fig/beam.png",0.08,(550,550)) #バーの設定
    ball = Ball("fig/boss.png", rack) #ボールの設定

    while True:
        scr.blit()
        for event in pg.event.get(): #×ボタンで終了
            if event.type == pg.QUIT: return
        
        ball.ball_move(scr)
        rack.update(scr)
        ball.update(scr)
        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct): #バーと壁の判定
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__": #関数の呼び出し
    pg.init()
    main()
    pg.quit()
    sys.exit()