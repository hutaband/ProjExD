import random
import sys
import pygame as pg


class Screen:
    def __init__(self, title, wh, image):  #初期メソッド
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

    def text_blit(self,text,t_x,t_y):
        self.sfc.blit(text,[t_x,t_y])

class Mato:#的のクラス
    def __init__(self,image,size,xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):#貼り付け
        scr.sfc.blit(self.sfc, self.rct)

    def update(self,scr:Screen): #更新
        scr.sfc.blit(self.sfc,self.rct)


class Racket:
    def __init__(self, image: str, size: float, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size*15)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 5
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 5
        
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_LEFT]: 
                self.rct.centerx += 5
            if key_states[pg.K_RIGHT]: 
                self.rct.centerx -= 5
        self.blit(scr)



class Ball:
    def __init__(self, fname, rack,mato,mato2):


        self.image = pg.image.load(fname).convert_alpha()
        self.image = pg.transform.scale(self.image,(50,50))
        self.rct = self.image.get_rect()
        self.v_x = 2
        self.v_y = 2
        self.racket = rack
        self.mato = mato
        self.mato2 = mato2


    def ball_move(self, scr: Screen):
        global score

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
            if dist < -1:
                self.v_x =-2 #-2*(2+dist/200/2)
            elif dist > 1:
                self.v_x = 2 #2*(2-dist/200/2)
            else:
                self.v_x = random.randint(-5,5)
            self.v_y = -self.v_y

        if self.rct.colliderect(self.mato.rct):#的1の判定
            self.v_x *= -1#-1をかけて反転する
            self.v_y *= -1#-1をかけて反転する
            self.v_x+= 0.2#動きを加速させる
            self.v_y+= 0.2#動きを加速させる
            score += 100

        if self.rct.colliderect(self.mato2.rct):#的2の判定
            self.v_x *= -1#-1をかけて反転する
            self.v_y *= -1#-1をかけて反転する
            self.v_x+= 1#動きを加速させる
            self.v_y+= 1#動きを加速させる
            score += 500    

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

    scr = Screen("squash", (1100, 600), "fig/haikei.png")
    rack = Racket("fig/bou3.png",0.08,(550,550))
    mato =  Mato("fig/mato1.png",0.5,(random.randint(220,550),110))
    mato2 = Mato("fig/mato1.png",0.3,(random.randint(600,900),120))
    ball = Ball("fig/0.png", rack,mato,mato2)

    while True:
        scr.blit()
        mato.blit(scr)
        mato2.blit(scr)
        font = pg.font.SysFont(None,60)
        message = font.render("score",False,(255,255,0))#scoreという文字を作成
        scr.text_blit(message, 900,50)
        font = pg.font.Font(None, 80)
        text = font.render(f"{score}", True,(255,0,0))#score(数字)を表示
        scr.text_blit(text, 900,80)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        ball.ball_move(scr)
        rack.update(scr)
        mato.update(scr)
        mato2.update(scr)
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
    score = 0
    main()
    pg.quit()
    sys.exit()