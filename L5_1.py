from vpython import *  #引用套件Vpython

G = 6.67*10**(-11)  #萬有引力常數
M = 6*10**24    #地球質量
m = 1000    #衛星質量
Re = 6.4*10**6  #地球半徑
r = 5*Re  #衛星軌道半徑
t = 0   
dt = 1
v0 = sqrt(G*M/r)   #衛星繞行速率   
cir = True

def F_g(x):                                 #定義萬有引力公式
    return -G*M*m/(mag(x)**3)*x

scene = canvas(width=600, height=600, center=vec(1.6*Re,0,0), background=vec(0.6,0.8,0.8)) #設定視窗
earth = sphere(pos=vec(0,0,0), radius=Re, texture=textures.earth) #放置物件地球
mater = sphere(pos=vec(r,0,0), v = vec (0,0.7*v0,0), a = vec(0,0,0),radius=0.1*Re,color=color.red, make_trail=True) #放置物件衛星

def semi(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]
    len = sqrt(x**2 + y**2 + z**2)/2
    return len

while cir:  #執行無窮迴圈
    rate(50000)
    
    mater.a = F_g(mater.pos-earth.pos)/m
    mater.v += mater.a*dt   
    mater.pos += mater.v*dt  

    if mater.v.y > 0 and (mater.v + dt*mater.a).y < 0:
        print(f"上端點: {mater.pos}")
        top = (mater.pos.x, mater.pos.y, mater.pos.z)
    if mater.v.x < 0 and (mater.v + dt*mater.a).x > 0:
        print(f"左端點: {mater.pos}")
        left = (mater.pos.x, mater.pos.y, mater.pos.z)
    if mater.v.y < 0 and (mater.v + dt*mater.a).y > 0:
        print(f"下端點: {mater.pos}")
        bottom = (mater.pos.x, mater.pos.y, mater.pos.z)
    if mater.v.x > 0 and (mater.v + dt*mater.a).x < 0:
        print(f"右端點: {mater.pos}")
        right = (mater.pos.x, mater.pos.y, mater.pos.z)
        semi_major = semi(left, right)
        semi_minor = semi(top, bottom)
        f = sqrt(semi_major**2 - semi_minor**2)
        print(f"The semi-major axis is: {semi_major}\nThe semi-minor axis is: {semi_minor}\nThe focal length is: {f}")
        cir = False
        
    t += dt
