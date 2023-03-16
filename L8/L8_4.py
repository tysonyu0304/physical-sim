from vpython import*

A = 1.0            #振幅
N = 100            #介質個數
omega = 2*pi/1.0   #振動角頻率
size = 0.1         #介質的大小
m = 0.1            #介質的質量
k = 400.0          #每一小段彈簧的彈力常數
d = 0.4            #介質之間的初始間隔
     
scene = canvas(title='Spring Wave', width=1200, height=300, center = vector((N-1)*d/2, 0, 0)) 

ball =[]
for i in range(N):
    ball.append(sphere(radius=size, color=color.yellow, pos=vec(i*d, 0, 0), v=vec(0,0,0)))# 將sphere(radius=size, color=color.yellow, pos=vec(i*d, 0, 0), v=vec(0,0,0))放入list中

spring = []
for i in range(N-1):
    spring.append(helix(radius = size/2.0, thickness = d/15.0, pos=vec(i*d, 0, 0), axis=vec(d,0,0)))#將helix(radius = size/2.0, thickness = d/15.0, pos=vec(i*d, 0, 0), axis=vec(d,0,0))放入list中

A_pos = []    #呼叫一個空的list，隨後加入所有球的y座標資訊
for i in range(N):
    A_pos.append(ball[i].pos.y)

def SpringForce(r):    
    return - k*(mag(r)-0.5*d)*norm(r)

x = graph(title = "x-t")    #畫圖用，先設定圖表名稱即可
f = gdots(color = color.blue)

pre_max_index = 0    #記錄前一個迴圈中，介質位移最大的index
max_index = 0    #記錄這一個迴圈中，介質位移最大的index

t, dt = 0, 0.001       

while ball[N-2].pos.y < 0.1*A:    #當波前緣抵達倒數第二顆介質球時停止迴圈
    rate(500)
    t += dt
    
    if t <= pi/omega :
        ball[0].pos = vector( 0, A*sin(omega*t), 0)    
        #在球與球之間放入彈簧
    for i in range(N-1):
        spring[i].pos = ball[i].pos
        spring[i].axis = ball[i+1].pos-ball[i].pos
    
    #計算並模擬球的運動
    for i in range(1, N-1):      
        ball[i].v += (SpringForce(spring[i-1].axis)-SpringForce(spring[i].axis))/m*dt 
        ball[i].pos += ball[i].v*dt
        A_pos[i] = ball[i].pos.y    #更新y座標list資訊
    
    pre_max_index = max_index
    max_index = A_pos.index(max(A_pos)) #找出在A_pos的最大值並回傳其index
   
    if t > pi/omega:
        T = t - pi/omega
        if pre_max_index != max_index:    #當最大位移的index有所變化時在將該球的x座標畫上圖
            f.plot(T , ball[max_index].pos.x)  
