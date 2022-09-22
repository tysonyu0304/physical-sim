from vpython import *
import os

scene = canvas(width = 600 , height = 600 , center=vector(10, 0, 0), background=vector(0.605, 0.789, 0.789))

ball = sphere(radius = 1, color = color.yellow, make_trail = True, trail_type = "curve", interval = 1)

dt = 0.001
t = 0
m = 1
F = vec(4, 0, 0)
ball.v = vec(0, 6.0, 0)
ball.a = vec(0, 0, 0)

def stop():
    os.system("pause")

while True:                     #無窮迴圈
    rate(1/dt)
    t += dt
    
    ball.a = F/m
    ball.v = ball.v + ball.a*dt
    ball.pos = ball.pos + ball.v*dt

    F_vec = ball.v.rotate(angle = pi/2)  
    # print(F_vec)  #請使用rotate的語法，找出F向量的方向
    F = 4.0*F_vec/mag(F_vec)    #沿力的方向(F_vec)長出大小為4.0的力
    
    if ball.v.x >= 0 and ball.v.x + F.x/m < 0:    #右端點條件
        right = ball.pos.x
    if ball.v.x <= 0 and ball.v.x + F.x/m > 0:    #左端點條件
        left = ball.pos.x
        print ("theoretical radius = ", m*mag(ball.v)**2/mag(F))
        print ("simulated radius = " , abs(right - left)/2)    #模擬的半徑值
