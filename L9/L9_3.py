from vpython import *  #引用視覺畫套件Vpython

k = 9*10**9   
size = 0.1  
N = 36  #電力線數量
Q1_charge = 10**(-5) #Q1電量 
Q1_position = vec(0, 0, 0) #Q1位置
Q2_charge = -10**(-5)
Q2_position = vec(2, 0, 0)
t = 0 ; dt = 0.001

scene = canvas(title='line of electric force', height=600, width=1200, range=3.5,auto_scale=False, background=vec(0.3,0.4,0.4), center = vec(1,0,0))
Q1 = sphere(pos = Q1_position , radius = size , color = color.blue)
Q2 = sphere(pos=Q2_position, radius=size, color=color.red)

#畫出每個質點球, 每個球的名稱為field_ballp[i] 
field_ballp=[]
field_balln=[]

for i in range(N):
    field_ballp.append(sphere(pos=vec(size*cos(2*pi*i/N), size*sin(2*pi*i/N),0) + Q1_position, radius=0.01, color=color.yellow, make_trail=True, v=vec(0,0,0)))
    field_balln.append(sphere(pos=Q2_position+vec(size*cos(2*pi*i/N), size*sin(2*pi*i/N),0), radius=0.01, color=color.yellow, make_trail=True, v=vec(0,0,0)))

def Force_Ep(r, q):  #定義靜電力，請將庫倫定律寫於此，r為與場源距離，q為電荷帶電量
    return k*Q1_charge*q*norm(r)/(mag(r)**2)

def Force_En(r, q):
    return k*Q2_charge*q*norm(r)/(mag(r)**2)

while True:
    rate(1000)        
    for i in range(len(field_ballp)):
        field_ballp[i].v = norm(Force_Ep(field_ballp[i].pos-Q1_position, Q1_charge) + Force_En(field_ballp[i].pos-Q2_position, Q1_charge))   #設定小球移動方向為單位正電荷的受力方向
        field_ballp[i].pos += field_ballp[i].v*dt
        field_balln[i].v = norm(Force_En(field_balln[i].pos-Q2_position, Q2_charge) + Force_Ep(field_balln[i].pos-Q1_position, Q2_charge))
        field_balln[i].pos += field_balln[i].v*dt