from vpython import *

n = [1.1, 1.2, 1.3, 1.4, 1.5 ]
scene = canvas(title="Dispersion", width=800, height=600, x=0, y=0, center=vec(1, 0, 0), background=vec(0, 0.6, 0.6))
interface = box(pos=vec(1, 0, 0), size=vec(10, 0.05, 0.5), color=color.blue)

light = []
for i in range(5):
    light.append(sphere(pos=vec(-2, 2, 0), radius = 0.01,v = vec(sin(60*pi/180),-cos(60*pi/180),0),color = color.white, make_trail = True))
    
theta_r = []    #叫出一個空的list，之後放入各道光的折射角資訊
switch = 0

t = 0
dt = 0.001

while light[0].pos.y >= -3:
    rate (2/dt)
    
    for i in range(5):
        light[i].pos += light[i].v*dt
    
    if light[0].pos.y < 0 and switch == 0:  #當光接觸到界面時，改變軌跡顏色
        switch = 1
        light[0].trail_color = color.red
        light[1].trail_color = color.yellow
        light[2].trail_color = color.green
        light[3].trail_color = color.blue
        light[4].trail_color = color.purple

        for i in range(len(light)):    #利用for迴圈將物件放入list中
            theta_i = 60*pi/180    #各色光的入射角皆為60度
            theta_r.append(asin(sin(theta_i)/n[i]))  #求出各色光折射角並放入list中
            light[i].v = vec(sin(theta_r[i]), -cos(theta_r[i]), 0)   #改變各色光的行進方向