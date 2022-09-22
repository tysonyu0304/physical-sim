from vpython import *

o = vec(0, 0, 0)
dt = 0.001
v = -2
a = 3
t = 0

scene = canvas(width=600, height=400, center=vector(2.5,0,0), background=vector(0,0,0))

ball = sphere (pos = o, radius = 1, color = color.green, v = v)
a_x = arrow(pos = o, axis = vec(5, 0, 0), shaftwidth=0.02, color = color.green)
a_y = arrow(pos = o, axis = vec(0, 5, 0), shaftwidth=0.02, color = color.red)
a_z = arrow(pos = o, axis = vec(0, 0, 5), shaftwidth=0.02, color = color.blue)

gd1 = graph(title = "x-t plot", width = 600, height = 400, xtitle = "t", ytitle = "x")
f1 = gcurve(color = color.blue)
gd2 = graph(title = "v-t plot", width = 600, height = 400, xtitle = "t", ytitle = "v")
f2 = gcurve(color = color.green)
gd3 = graph(title = "a-t plot", width = 600, height = 400, xtitle = "t", ytitle = "a")
f3 = gcurve(color = color.red)

while t<5:
    rate(1/dt)
    if v < 0 and (v + dt * a) >= 0:
        print("欸 反了")
        print("t = {:.2f}".format(t))
        print("x = {:.2f}".format(ball.pos.x))
        print("v = {:.2f}".format(v))
    if t < 3 and (t + dt) >= 3:
        print("t = {:.2f} , position = {:.2f}".format(t, ball.pos.x))
    v += dt * a
    ball.pos.x += v * dt
    t += dt
    f1.plot(pos = (t, ball.pos.x))
    f2.plot(pos = (t, v))
    f3.plot(pos = (t, a))