from vpython import *

g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 100000              #彈簧力常數 100000 N/m
m = 0.1                 #球質量 0.1 kg
theta = 30 * pi/180     #初始擺角
Fg = m*vector(0,-g,0)   #球所受重力向量

def SpringForce(r,L):
    return -k*(mag(r)-L)*norm(r)

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow, make_trail = True,
              retain = 1000, interval=1)#畫球
rod = cylinder(radius=size/10)#畫繩子
	
ball.pos = vector(L*sin(theta), -L*cos(theta), 0)   #球的初始位置
ball.v = vector(0, 0, 0)                            #球初速
rod.pos = vector(0, 0, 0)                           #繩子頭端的位置

dt = 0.001    #時間間隔
t = 0.0       #初始時間 
right1 = 0
right2 = 0
run = False

while True:
    rate(1/dt)
    rod.axis = ball.pos - rod.pos                #繩子的軸方向：由繩子頭端指向尾端的向量
    
    ball.a = (Fg + SpringForce(rod.axis,L))/m    #牛頓第二定律：加速度＝合力/質量
    ball.v += ball.a*dt    
    ball.pos += ball.v*dt  
    t += dt

    if ball.v.x > 0 and ball.v.x + ball.a.x*dt < 0: # 右端點
        right2 = right1
        right1 = t
        run = True
    
    if run:
        time = abs(right1 - right2)
        print(f"Simulated period = {time}, Theoretical period = {2*pi*sqrt(L/g)}")
        run = False
