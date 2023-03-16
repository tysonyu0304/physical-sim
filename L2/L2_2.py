from vpython import *

t = 0
x = 0
x_max = 0
max_t = 0
max_v = 0
v = 0
dt = 0.001

scene = canvas(width = 600, height = 400, center = vec(2.5, 0, 0), background = vec(0, 0, 0))

gd1 = graph(title = "x-t plot", width = 600, height = 400, xtitle = "t", ytilte = "x")
f1 = gcurve(color = color.blue)
gd2 = graph(title = "v-t plot", width = 600, height = 400, xtitle = "t", ytitle = "v")
f2 = gcurve(color = color.green)
gd3 = graph(title = "a-t plot", width = 600, height = 400, xtitle = "t", ytitle = "a")
f3 = gcurve(color = color.red)

while t < 6:
    rate(1/dt)
    if t < 2:
        a = 5
    elif t >= 2:
        a = -5
    t = t + dt
    v += a * dt
    x += v * dt
    if x_max < x:
        x_max = x
        max_t = t
        max_v = v
    f1.plot(pos = (t, x))
    f2.plot(pos = (t, v))
    f3.plot(pos = (t, a))
print("好遠")
print("t = {:.2f}".format(max_t))
print("x = {:.2f}".format(x_max))
print("v = {:.2f}".format(max_v))