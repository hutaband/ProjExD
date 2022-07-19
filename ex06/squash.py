import random
import sys
import pygame as pg


class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

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


class Ball:
    def __init__(self, fname, rack):
        self.image = pg.image.load(fname).convert_alpha()
        self.image = pg.transform.scale(self.image,(50,50))
        self.rct = self.image.get_rect()
        self.v_x = 1
        self.v_y = 1
        self.racket = rack

    def ball_move(self, scr: Screen):
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

        if self.rct.colliderect(self.racket.rct):
            dist = self.rct.centerx - self.racket.rct.centerx
            if dist < 0:
                self.v_x = -1
            elif dist > 0:
                self.v_x = 1
            else:
                self.v_x = random.randint(-5,5)
            self.v_y = -1

        if self.rct.bottom > scr.rct.bottom:
            font = pg.font.Font(None, 100)
            text = font.render("GAME OVER", True,(255,0,0))
            scr.text_blit(text, 400,200)


    def draw(self, sfc):
        sfc.blit(self.image, self.rct)


    def update(self,scr:Screen):
        scr.sfc.blit(self.image,self.rct)

def main():
    clock = pg.time.Clock()
    scr = Screen("squash", (1200, 600), "fig/haikei.png")
    rack = Racket("fig/beam.png",0.08,(550,550))
    ball = Ball("fig/boss.png", rack)

    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        ball.ball_move(scr)
        rack.update(scr)
        ball.update(scr)
        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()