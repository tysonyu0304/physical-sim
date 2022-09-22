from vpython import *

height = 0
v = 20
t = 0
g = -9.8
dt = 0.001
max30 = 0
max60 = 0
t30 = 0
t60 = 0

sence = canvas(width=600, height=400, x=0, y=0, background=color.black)
floor = box(pos=vec(5, 0, 0), length=60, height=0.01, width=10, texture=textures.wood)
ball30 = sphere(pos=vec(0, 0, 0), vc=vec(v*cos(30*pi/180), v*sin(30*pi/180), 0), radius=0.5,
                color=color.blue, make_trail=True, trail_type="curve", interval=1)
ball60 = sphere(pos=vec(0, 0, 0), vc=vec(v*cos(60*pi/180), v*sin(60*pi/180), 0), radius=0.5,
                color=color.green, make_trail=True, trail_type="curve", interval=1)

while ball30.pos.y >= 0 or ball60.pos.y >= 0:
    rate(1/dt)
    if ball30.pos.y >= 0:
        ball30.pos += ball30.vc*dt
        t30 += dt
    if ball60.pos.y >= 0:
        ball60.pos += ball60.vc*dt
        t60 += dt
    ball30.vc.y += g*dt
    ball60.vc.y += g*dt
    if max30 < ball30.pos.y:
        max30 = ball30.pos.y
    if max60 < ball60.pos.y:
        max60 = ball60.pos.y
    t += dt

print("30度的飛行時間", t30)
print("30度的最大高度", max30)
print("30度的水平射程", ball30.pos.x)
print("60度的飛行時間", t60)
print("60度的最大高度", max60)
print("60度的水平射程", ball60.pos.x)