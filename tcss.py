# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:46:23 2021

@author: 14346
"""

import pygame
import sys 
import random
#初始化变量
bgcolor=pygame.Color(0,0,0)
red=pygame.Color(255,0,0)
scolor=pygame.Color(33,255,33)
cell_size=20
#游戏结束的函数
def gameover():
    pygame.quit()
    sys.exit()
#主函数
def main():
    pygame.init()
    speed_clock = pygame.time.Clock()
    pygame.display.set_caption("贪吃蛇") #设置窗口标题
    screen=pygame.display.set_mode([600,400]) #初始化窗口
    head=0
    body=[{'x':3,'y':3},{'x':2,'y':3},{'x':1,'y':3}]
    food={'x':random.randint(0,29),'y':random.randint(0,19)}
    direction='right'  
    
    while True:
        #确定方向 蛇不可以180度换方向
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if direction in ['left','right']:
                    if event.key==pygame.K_UP:
                        direction='up'
                    elif event.key==pygame.K_DOWN:
                        direction='down'
                elif direction in ['up','down']:
                    if event.key==pygame.K_LEFT:
                        direction='left'
                    elif event.key==pygame.K_RIGHT:
                        direction='right'
        #移动贪吃蛇
        if direction=='up':
            newhead={'x':body[head]['x'],'y':body[head]['y']-1}
        elif direction=='down':
            newhead={'x':body[head]['x'],'y':body[head]['y']+1}
        elif direction=='left':
            newhead={'x':body[head]['x']-1,'y':body[head]['y']}
        elif direction=='right':
            newhead={'x':body[head]['x']+1,'y':body[head]['y']}
        body.insert(0,newhead)
        #判断蛇是否吃到食物
        if body[head]['x']==food['x'] and body[head]['y']==food['y']:
            food['x']=random.randint(0,29)
            food['y']=random.randint(0,19)
        else:
            body.pop()
        #填充背景颜色
        screen.fill(bgcolor)
        #画蛇
        for i in body:
            x=i['x']*cell_size
            y=i['y']*cell_size
            srect=pygame.Rect(x,y,cell_size,cell_size)
            pygame.draw.rect(screen,scolor,srect)
        #画食物
        x=food['x']*cell_size
        y=food['y']*cell_size
        frect=pygame.Rect(x,y,cell_size,cell_size)
        pygame.draw.rect(screen,red,frect)
        #更新到屏幕
        pygame.display.flip()
        #判断蛇是否撞到墙
        if body[head]['x']<0 or body[head]['x']>29 or body[head]['y']<0 or body[head]['y']>19:
            gameover()
        #判断蛇是否撞到自己身体
        for cell in body[1:]:
            if cell['x']==body[head]['x'] and cell['y']==body[head]['y']:
                gameover()
        #控制游戏速度
        speed_clock.tick(5)
#启动入口函数
if __name__ =='__main__':       
    main()
