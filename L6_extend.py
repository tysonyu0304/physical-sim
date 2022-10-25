from vpython import *

size = 1    #球的大小                  
m1 = 2    #球1質量                 
m2 = 2    #球2質量           
side = 4.0    #箱子牆壁所在位置  
thk = 0.3    #牆壁厚度
s2 = 2*side - thk    #牆壁大小
s3 = 2*side + thk

scene = canvas(width=800, height=800, center = vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定畫面
#畫牆壁
wall_R = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wall_L = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wall_B = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue)
wall_T = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
wall_BK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))

ball1 = sphere(radius = size, color=color.yellow , pos = vec(-3,0.5,0) ,v = vec(6,0,1), make_trail = True, retain = 100) #畫球1

# 定義3D碰撞公式
def collision(v1, v2, x1, x2):
    v1_f = v1 - (2*m2/(m1 + m2))*((dot(v1 - v2, x1 - x2))/(mag(x1 - x2)**2))*(x1 - x2)   #請嘗試將碰撞公式填入其中
    v2_f = v2 - (2*m1/(m1 + m2))*((dot(v2 - v1, x2 - x1))/(mag(x2 - x1)**2))*(x2 - x1)
    return (v1_f, v2_f)
    
t = 0
dt = 0.001 #時間間隔 0.001 秒

while True:             
    rate(1/dt) #每一秒跑 1000 次

    ball1.pos += ball1.v*dt

    #若兩球球心距離小於兩倍球半徑，則代入碰撞公式改變速度
    if mag(ball1.pos - ball2.pos) < 2*size :    #請思考如何判斷兩球相撞
        ball1.v, ball2.v = collision(ball1.v, ball2.v, ball1.pos, ball2.pos)

    #球撞擊牆面時，使球反彈
    if abs(ball1.pos.x - side) <= size or abs(ball1.pos.x + side) <= size:    #請思考如何判斷球1撞擊左右兩牆
        ball1.v.x = -ball1.v.x
    if abs(ball1.pos.y - side) <= size or abs(ball1.pos.y + side) <= size:    #請思考如何判斷球1撞擊上下兩牆
        ball1.v.y = -ball1.v.y
    if abs(ball1.pos.z - side) <= size or abs(ball1.pos.z + side) <= size:    #請思考如何判斷球1撞擊前後兩牆
        ball1.v.z = -ball1.v.z