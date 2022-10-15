from vpython import *

G = 6.67*10**(-11)  #萬有引力常數
M = 2*10**30    #太陽質量
me = 6*10**24   #地球質量
mm = 6.4*10**23    #火星質量
Rs = 7*10**8  #太陽半徑
re = 5*Rs   #地球軌道半徑
rm = 7*Rs   #火星軌道半徑
v0_e = 0.7*sqrt(G*M/re)     #地球繞行速率
v0_m = 0.7*sqrt(G*M/rm)     #火星繞行速率  
dt = 1
theore = G*M/(4*(pi**2))

bg = canvas(width=800, height=800, center=vec(re/2, 0, 0), background=vector(0.605, 0.789, 0.789))
sun = sphere(pos=vec(0, 0, 0), radius=Rs, color=color.yellow) #放置物件太陽
earth = sphere(pos=vec(re, 0, 0), v=vec(0, v0_e, 0), a=vec(0, 0, 0), radius=Rs/10, texture=textures.earth, make_trail=True)
mars = sphere(pos=vec(rm, 0, 0), v=vec(0, v0_m, 0), a=vec(0, 0, 0), radius=Rs/8, color=color.red, make_trail=True)

def F_g(m, x):
    return -G*M*m/(mag(x)**3)*x

def semi(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    z = a[2] - b[2]
    len = sqrt(x**2 + y**2 + z**2)/2
    return len

def value(a, t):
    return a**3/t**2

print(f"theoretical value for a^3/T^2 = {theore}")

earth_l = []
earth_r = []
earth_t = 0
mars_l = []
mars_r = []
mars_t = 0

while True:
    rate(5000)  

    earth.a = F_g(me, earth.pos - sun.pos)/me
    mars.a = F_g(mm, mars.pos - sun.pos)/mm
    earth.v += earth.a*dt
    mars.v += mars.a*dt
    earth.pos += earth.v*dt
    mars.pos += mars.v*dt

    if earth.v.x < 0 and (earth.v + earth.a*dt).x > 0:
        earth_l = [earth.pos.x, earth.pos.y, earth.pos.z]
    if earth.v.x > 0 and (earth.v + earth.a*dt).x < 0:
        earth_r = [earth.pos.x, earth.pos.y, earth.pos.z]
        print(f"a^3/T^2 for Earth = {value(semi(earth_l, earth_r), earth_t)}")
        earth_t = 0
    if mars.v.x < 0 and (mars.v + mars.a*dt).x > 0:
        mars_l = [mars.pos.x, mars.pos.y, mars.pos.z]
    if mars.v.x > 0 and (mars.v + mars.a*dt).x < 0:
        mars_r = [mars.pos.x, mars.pos.y, mars.pos.z]
        print(f"a^3/T^2 for Mars = {value(semi(mars_l, mars_r), mars_t)}")
        mars_t = 0
    
    earth_t += dt
    mars_t += dt