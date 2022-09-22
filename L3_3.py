from vpython import *

scene = canvas(width=600 , height=600 , center=vec(10, 0, 0),
               background=vector(0.605, 0.789, 0.789))
scene.camera.pos = vec(-9, 0 ,0)
scene.range = 20

ball = sphere(radius=1, color=color.yellow, make_trail=True,
              trail_type="curve", interval=1)

dt = 0.001
t = 0
m = 1
F = vec(4, 0, 0)
ball.v = vec(0, 6.0, 0)
ball.a = vec(0, 0, 0)

while True:        
    rate(1/dt)
    t += dt
    
    ball.a = F/m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt

    F_vec = ball.v.rotate(angle = pi/2)  
    F = 4.0*F_vec/mag(F_vec)
    
    if ball.v.x >= 0 and ball.v.x + F.x/m < 0:    
        right = ball.pos.x
    if ball.v.x <= 0 and ball.v.x + F.x/m > 0:    
        left = ball.pos.x
        print ("theoretical radius = ", m*mag(ball.v)**2/mag(F))
        print ("simulated radius = " , abs(right - left)/2)    
