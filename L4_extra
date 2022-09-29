from vpython import *

g = 9.8                 #重力加速度 9.8 m/s^2
size = 0.05             #球半徑 0.05 m            
L = 0.5                 #彈簧原長 0.5m
k = 100000              #彈簧力常數 100000 N/m
m = 0.1                 #球質量 0.1 kg
theta = 30 * pi/180     #初始擺角
Fg = m*vector(0,-g,0)   #球所受重力向量
damp = 0.1

def SpringForce(r,L):
    return -k*(mag(r)-L)*norm(r)

def SpringDamp(v, r):  #避震器
    cos_theta = dot(v,r)/(mag(v)*mag(r))                    #用向量內積找v和r夾角的餘弦函數
    r_unit_vector = norm(r)                                 #沿彈簧軸方向的單位向量
    projection_vector = mag(v) * cos_theta * r_unit_vector  #計算v在r方向的分量
    spring_damp = - damp * projection_vector                #沿彈簧軸方向的阻力
    return spring_damp

scene = canvas(width=600, height=600, center=vector(0, -L*0.8, 0), range=1.2*L)#設定畫面
ceiling = box(length=0.4, height=0.005, width=0.4, opacity = 0.2)#畫天花板
ball = sphere(radius = size,  color=color.yellow, make_trail = True, retain = 1000, interval=1)#畫球
rod = cylinder(radius=size/10)#畫繩子
	
ball.pos = vector(L*sin(theta), -L*cos(theta), 0)   #球的初始位置
ball.v = vector(0, 0, 0)                            #球初速
rod.pos = vector(0, 0, 0)                           #繩子頭端的位置

v_vector = arrow(shaftwidth = 0.01, color=color.green)
Ftot_vector = arrow(shaftwidth = 0.01, color=color.red)
mg_vector = arrow(shaftwidth = 0.01, color=color.yellow)
Fs_vector = arrow(shaftwidth = 0.01, color=color.white) #箭頭們
X = 0.2 

v_text = label(box=False, opacity=0, height=15, color=color.green, text='V')
Ftot_text = label(box=False, opacity=0, height=15, color=color.red, text="F_tot")
mg_text = label(box=False, opacity=0, height=15, color=color.yellow, text="Fg")
Fs_text = label(box=False, opacity=0, height=15, color=color.white, text="Fs")#標籤們

dt = 0.001    #時間間隔
t = 0.0       #初始時間
t_right = 0   #右端點時間

right1 = 0
right2 = 0
right_times = 0
run = True

while True:
    rate(1/dt)
    rod.axis = ball.pos - rod.pos                #繩子的軸方向：由繩子頭端指向尾端的向量
    
    if mag(ball.v) != 0:
        ball.a = (Fg + SpringForce(rod.axis,L) + SpringDamp(ball.v, SpringForce(rod.axis,L)))/m    #牛頓第二定律：加速度＝合力/質量
    else:
        ball.a = (Fg + SpringForce(rod.axis,L))/m
    ball.v += ball.a*dt    
    ball.pos += ball.v*dt  
    t += dt

    v_vector.pos = ball.pos     #將速度箭頭設定在球上
    Ftot_vector.pos = ball.pos  #將合力箭頭設定在球上
    mg_vector.pos = ball.pos    #將重力箭頭設定在球上
    Fs_vector.pos = ball.pos    #將彈力箭頭設定在球上

    if v_vector.axis.y > 0:
        v_text.pos = v_vector.pos + v_vector.axis*1.1
    else:
        v_text.pos = v_vector.pos + v_vector.axis*1.1
    if Ftot_vector.axis.y > 0:
        Ftot_text.pos = Ftot_vector.pos + Ftot_vector.axis*1.1
    else:
        Ftot_text.pos = Ftot_vector.pos + Ftot_vector.axis*1.1
    if mg_vector.axis.y > 0:
        mg_text.pos = mg_vector.pos + mg_vector.axis*1.1
    else:
        mg_text.pos = mg_vector.pos + mg_vector.axis*1.1
    if Fs_vector.axis.y > 0:
        Fs_text.pos = Fs_vector.pos + Fs_vector.axis*1.1
    else:
        Fs_text.pos = Fs_vector.pos + Fs_vector.axis*1.1 #移動字的位置

    v_vector.axis = ball.v * X                                #設定速度箭頭，將軸方向設定為速度向量
    Ftot_vector.axis = (Fg + SpringForce(rod.axis,L)) * X  #設定合力箭頭，將軸方向設定為合力向量
    mg_vector.axis = Fg * X                                   #設定重力箭頭，將軸方向設定為重力向量
    Fs_vector.axis = SpringForce(rod.axis,L) * X  