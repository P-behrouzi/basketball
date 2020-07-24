import sympy as sp
import math
import os.path
import random
import sys
from random import randint
import pygame
from pygame.locals import *
import time
pygame.init()
basket_pos_x=410
basket_pos_y=100
x_page = 1024
y_page = 768
ball_x=randint(80,x_page-200)
ball_y=600
speed=1
speed_ball_x=1
speed_ball_y=1
pos=(0,0)
#score=0
text_x=20
text_y=20


def main(lvl,user):
    score=0
    black=(0,0,0)
    font1=pygame.font.SysFont("Megahunt.ttf", 40)
    score_disp=font1.render("score: "+str(score),True,black)
    font=pygame.font.SysFont("Megahunt.ttf", 30)
    user_disp=font.render("username: "+user,True,black)
    black=(0,0,0)
    red=(255,0,0)
    green=(0,255,0)
    blue=(0,0,255)
    pygame.init()
    screen = pygame.display.set_mode((x_page,y_page ))
    pygame.display.set_caption("basketball game")
    basket=pygame.image.load("basket.png")
    basket_width=125
    ball=pygame.image.load("ball.png")
    def basket_mediun():
        global basket_pos_x,x_page,speed
        basket_pos_x+=speed*(lvl-4)
    def enforce_border():
        global basket_pos_x,basket_pos_y,x_page,y_page,speed
        if basket_pos_x<80:
            basket_pos_x=80
            speed=1
        if basket_pos_x>x_page-200:
            basket_pos_x=x_page-200
            speed=-1

    def basket_hard():
        global basket_pos_x,basket_pos_y
        if(basket_pos_x==824 and basket_pos_y<200):
            basket_pos_y+=(1*(lvl-14))
            if(basket_pos_y>200):
                basket_pos_y=200
        elif(basket_pos_x<824 and basket_pos_y==100):
            basket_pos_x+=(1*(lvl-14))
            if(basket_pos_x>824):
                basket_pos_x=824
        elif(basket_pos_x==80 and basket_pos_y>100):
            basket_pos_y-=(1*(lvl-14))
            if(basket_pos_y<100):
                basket_pos_y=100
        elif(basket_pos_x>80 and basket_pos_y==200):
            basket_pos_x-=(1*(lvl-14))
            if(basket_pos_x<80):
                basket_pos_x=80

    def move_ball():
        global ball_y,ball_x,pos
        #time.sleep(5)
        ball_y=pos[1]
        ball_x=pos[0]

    def show_image():
        screen.blit(basket,(basket_pos_x,basket_pos_y))
        screen.blit(ball,(ball_x,ball_y))
        screen.blit(score_disp,(text_x,text_y))
        screen.blit(user_disp,(20,60))
    play=True
    i=0
    number=0
    while play:
        global ball_x,ball_y,pos
        if(5<lvl<=15):
            basket_mediun()
            enforce_border()
        if(lvl>15):
            basket_hard()
        if(number==5):
            play=False
            #pygame.quit
            #pygame.display.quit()
            #pygame.quit()
            return score
        if(i==1):
            move_ball()
            if(ball_x==pos[0] and ball_y==pos[1]):
                i=-1
        elif(i==-1):
            time.sleep(4)

            if (ball_x in range(basket_pos_x-100,basket_pos_x+100) and ball_y in range(basket_pos_y-100,basket_pos_y+100)):

                #global score
                score+=1
                score_disp=font1.render("score: "+str(score),True,black)
                #print(score)
                i=0
                ball_x=randint(80,x_page-200)
                ball_y=600
            else:
                i=0
                ball_x=randint(80,x_page-200)
                ball_y=600
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONUP):
                if (event.button == 1 and i==0):
                    pos = pygame.mouse.get_pos()
                    i=1
                    number+=1
            if event.type == pygame.QUIT:
                play=False


        screen.fill((255,255,255))
        show_image()

        pygame.display.flip()
    #pygame.display.quit()
    pygame.quit()
