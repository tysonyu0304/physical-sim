from vpython import *  
import os

m1 = 2.0    #球1質量
x1 = -20.0  #球1X軸初位置
v1= 5.5 #球1初速度
size1 = 1.0 #球1大小

m2 = 1.0    #球2質量
x2 = -5.0   #球2X軸初位置
v2= 1.0 #球2初速度
size2 = 1.0 #球2大小

spring_L = 5.0  #彈簧長度
k = 2.0 #彈力常數

def F_s(r):    #定義彈力
    return -k*(r-spring_L)

scene = canvas(width=1000, height=300, background=vec(0.6,0.8,0.8), center=vec(5,0,10)) #設定畫面
v1_text = label(box = False, opacity = 0, height = 25, color=color.red, text = 'v1')
v2_text = label(box = False, opacity = 0, height = 25, color=color.blue, text = 'v2')

ball1 = sphere(pos = vec(x1,0,0), v = vec(v1,0,0), a = vec(0,0,0), radius=size1, color = color.red) #設定球1
v1_arrow = arrow(pos=ball1.pos,axis=ball1.v,shaftwidth=0.2*size1 ,color = color.red)

ball2 = sphere(pos = vec(x2,0,0), v = vec(v2,0,0), a = vec(0,0,0), radius=size2, color = color.blue) #設定球2
v2_arrow = arrow(pos=ball2.pos,axis=ball2.v,shaftwidth=0.2*size2 ,color = color.blue)

spring = helix(pos=ball2.pos, axis = vec(-spring_L,0,0), radius=0.5, thickness =0.1, coils = 10 ) #畫彈簧

dt = 0.001
t = 0

def collision(v1, m1, v2, m2):
    vc = (v1*m1 + v2*m2)/(m1 + m2)
    return [2*vc - v1, 2*vc - v2]

while t < 7 :
    rate(2000)
    
    if ball2.pos.x - ball1.pos.x < spring_L:  #請思考如何判斷m1壓縮到m2上的彈簧
        ball1.a.x = -F_s((ball2.pos - ball1.pos).x)/m1 #壓縮期間的加速度分別為何？
        ball2.a.x = F_s((ball2.pos - ball1.pos).x)/m2
        spring.axis = ball1.pos-ball2.pos 
    else :                             
        ball1.a.x = 0    #若沒有壓縮彈簧時，加速度為何？
        ball2.a.x = 0
        spring.axis = vec(-spring_L,0,0)

    ball1.v += ball1.a *dt  
    ball2.v += ball2.a *dt
    
    ball1.pos += ball1.v*dt  #控制球1的運動
    ball2.pos += ball2.v*dt  #控制球2的運動

    v1_arrow.pos = ball1.pos #球1速度向量箭頭的起始點在球1上
    v1_arrow.axis = ball1.v  #球1速度向量箭頭的長度與方向等於球1速度
    v1_text.pos = ball1.pos  + vector(0,3,0)
    
    v2_arrow.pos = ball2.pos #球2速度向量箭頭的起始點在球2上
    v2_arrow.axis = ball2.v  #球1速度向量箭頭的長度與方向等於球2速度
    v2_text.pos = ball2.pos +vector(0,3,0)

    spring.pos= ball2.pos  #彈簧的起始點位置在球2上
        
    t += dt
    
print ("simulated v1' = %.2f"%ball1.v.x ,"simulated v2' =%.2f"%ball2.v.x )
tv = collision(v1, m1, v2, m2)
print ("theoretical v1' = ", tv[0], "theoretical v2' = ", tv[1])  #填入彈性碰撞公式解
