from vpython import *

scene = canvas(title="Mirage", width=800, height=600, x=0, y=0, center=vec(1, 0, 0), background=vec(0, 0.6, 0.6))
interface = box(pos=vec(1, 0, 0), size=vec(15, 0.1, 0.5), color=color.blue)
light = sphere (pos = vec(-5,3,0),v = vec(sin(60*pi/180),-cos(60*pi/180),0), radius = 0.01,color = color.white, make_trail = True)    #用球的軌跡代表光束
object = arrow(pos=vec(-5, 0, 0), axis = vec(0,light.pos.y,0), color=color.red,shaftwidth = 0.1)

t = 0
dt = 0.001

k = 0.1      #折射率的變化率
m = 1000     #切1000層
n = []       #先叫出空的list，待會填入各層的折射率
delta_y = light.pos.y/m     #每層的厚度

d = 3*k/m
for i in range(m):
    n.append(1 + d*i)   #切1000層，由下而上的各層折射率

first_time = 0  
   
while t < 25:
    rate (3/dt)
    t += dt
    light.pos += light.v*dt    #光的直進性
            
    if light.v.y < 0 and light.pos.y // delta_y != (light.pos.y + light.v.y*dt) // delta_y :    #光線下行時通過各介面的判斷
        i = int (light.pos.y // delta_y)    #判斷光線現在位於哪層
        
        if first_time == 0:                 #判斷第一次的折射
            theta_i = 60*pi/180         #第一次折射的入射角    
            theta_r = asin(sin(theta_i)*n[i]/n[i-1])    #利用折射定律配合反三角函數求出折射角
            light.v = vec(sin(theta_r), -cos(theta_r), 0)    #改變光線行進方向
            first_time = 1
            
        else:
            theta_i = acos(abs(light.v.y))    #每一次入射角為上一次的折射角

            if sin(theta_i)*n[i] > n[i-1]:      #全反射條件
                light.v.y = -light.v.y  #發生全反射時，光線前進方向如何調整?               
            else:
                theta_r = asin(sin(theta_i)*n[i]/n[i-1])        #利用折射定律配合反三角函數求出折射角
                light.v = vec(sin(theta_r), -cos(theta_r), 0)   #改變光線行進方向
                
    elif light.v.y > 0 and light.pos.y // delta_y != (light.pos.y + light.v.y*dt) // delta_y :     #光線上行時通過各介面的判斷
        i = int (light.pos.y // delta_y)    #判斷光線現在位於哪層
        
        theta_i = acos(light.v.y)   #每一次入射角為上一次的折射角
        theta_r = asin(sin(theta_i)*n[i]/n[i+1])    #利用折射定律配合反三角函數求出折射角
        light.v = light.v = vec(sin(theta_r), cos(theta_r), 0) #改變光線行進方向
        
    t += dt