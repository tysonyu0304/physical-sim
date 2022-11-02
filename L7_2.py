from vpython import *

n1 = 1.33    #水的折射率
n2 = 1.00    #空氣的折射率

scene = canvas(title="Full Reflection", width=800, height=600, x=0, y=0, center=vec(1.5, 1.5, 0), background=vec(0, 0.6, 0.6))
interface = box(pos=vec(1, 0, 0), size=vec(10, 0.1, 0.5), color=color.blue)
light = []      #叫出一個空的list，之後放入各道光的初始資訊
theta_i = []    #叫出一個空的list，之後放入各道光的入射角資訊
theta_r = []    #叫出一個空的list，之後放入各道光的折射角資訊
switch = []     #叫出一個空的list，之後放入各道光的界面判斷資訊

for i in range(7):    #利用迴圈配合append語法將模擬光的球丟入list中，在此模擬7道光線
    light.append(sphere(pos=vec(-4, -3, 0), radius = 0.01,v = vec(sin((10+10*i)*pi/180),cos((10+10*i)*pi/180),0),color = color.white, make_trail = True))
    switch.append(0)

t = 0
dt = 0.001

while t < 10:
    rate (3/dt)
    t += dt
    for i in range(7):
        light[i].pos += light[i].v*dt   #每道光的直進性
 
        if light[i].pos.y > 0 and switch[i] == 0:    #第i道光線抵達界面                
            switch[i] = 1              
            theta_i.append((10 + 10*i)*pi/180)    #將入射角資訊放入theta_i的list中
            if sin(theta_i[i])*n1 >= n2:     #全反射條件
                light[i].v.y = -light[i].v.y    #改變光線行進方向
            else :    #折射定律
                theta_r.append(asin(sin(theta_i[i])*n1))    #利用折射定律配合反三角函數求出各個折射角並放入theta_r的list中
                light[i].v = vec(sin(theta_r[i]), cos(theta_r[i]), 0)    #改變光線行進方向