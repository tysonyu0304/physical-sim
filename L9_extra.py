from vpython import *

I = 1
dz = 0.01

def dB(r):   #必毆沙伐定律
    return 6*I*cross(vec(0,0,dz),r)/(mag(r)**3)    #調整常數的值，讓視窗顯示得較為好看

scene = canvas(width=1000, height=800, center=vec(0,0,0), background=vec(0.6,0.8,0.8))
current = cylinder(pos = vec(0,0,-30), axis = vec (0,0,60),radius = 0.1,color = color.green)    #一直導線
floor = box(pos=vec(0,0,-0.05),size=vec(35,35,0.1),color = vec(0.5,0.5,0.5))

arrowlist = []  #定義箭頭放置的List

for N1 in range(-5,6,1): #X軸
    for N2 in range(-5,6,1):#Y軸
        arrowlist.append(arrow(pos = vector(3*N1,3*N2,0), axis = vector(0,0,0), shaftwidth = 0.2, color = color.red))
        
for i in arrowlist:
    if mag(i.pos) > current.radius: #考慮導線外的區域
        z = current.pos.z
        while z < -current.pos.z :    #考慮整條導線
            #[    ] #這塊區域請寫上如何找出磁場大小
            pass
    else :
        i.axis = vec(0,0,0)