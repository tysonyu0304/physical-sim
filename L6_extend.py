from vpython import *
import random

dt = 0.01 #時間間隔 0.01 秒
run = False
reset = False
end = False

class ball():
    def __init__(self):
        self.size = 0.1
        self.m1 = 2
        self.m2 = 2
        self.side = 4.0
        self.thk = 0.3
        self.s2 = 2*self.side - self.thk
        self.s3 = 2*self.side + self.thk
        self.num = 5
        self.ball = []
        self.hit_t = 0
        self.start()
    
    def start(self):
        self.scene = canvas(width=800, height=800, center = vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定畫面
        #畫牆壁
        self.wall_R = box (pos=vector(self.side, 0, 0), size=vector(self.thk, self.s2, self.s3),  color = color.red)
        self.wall_L = box (pos=vector(-self.side, 0, 0), size=vector(self.thk, self.s2, self.s3),  color = color.red)
        self.wall_B = box (pos=vector(0, -self.side, 0), size=vector(self.s3, self.thk, self.s3),  color = color.blue)
        self.wall_T = box (pos=vector(0, self.side, 0), size=vector(self.s3, self.thk, self.s3),  color = color.blue)
        self.wall_BK = box(pos=vector(0, 0, -self.side), size=vector(self.s2, self.s2, self.thk), color = color.gray(0.7))
        self.num = int(input("請輸入球數:"))
        self.ball_ganerater()
        self.b1 = button(text="stop", pos=self.scene.caption_anchor, bind=self.run_stop)
        self.b2 = button(text="reset", pos=self.scene.caption_anchor, bind=self.reset)
        self.b3 = button(text="end", pos=self.scene.caption_anchor, bind=self.end)
        global run
        run = True

    def init(self):
        global reset
        self.num = 0
        self.ball = []
        self.scene.visible = False
        self.b1.delete()
        self.b2.delete()
        self.b3.delete()
        self.scene.delete()
        self.start()
        reset = False

    def pos_ganerater(self):
        x = random.uniform(-self.s2/2, self.s2/2)
        y = random.uniform(-self.s2/2, self.s2/2)
        z = random.uniform(-self.s2/2, self.s2/2)
        return vec(x, y, z)

    def v_ganerater(self):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        z = random.uniform(-2, 2)
        return vec(x, y, z)

    def ball_ganerater(self):
        for i in range(self.num):
            self.ball.append(sphere(pos=self.pos_ganerater(), v=self.v_ganerater(), radius=self.size, color=color.yellow, make_trail=True, retain=100)) #畫好多球

    def collision(self, v1, v2, x1, x2):
        v1_f = v1 - (2*self.m2/(self.m1 + self.m2))*((dot(v1 - v2, x1 - x2))/(mag(x1 - x2)**2))*(x1 - x2)   #請嘗試將碰撞公式填入其中
        v2_f = v2 - (2*self.m1/(self.m1 + self.m2))*((dot(v2 - v1, x2 - x1))/(mag(x2 - x1)**2))*(x2 - x1)
        return (v1_f, v2_f)

    def btb_collision(self):
        for i in range(len(self.ball)):
            for j in range(i+1, len(self.ball)):
                #若兩球球心距離小於兩倍球半徑，則代入碰撞公式改變速度
                if mag(self.ball[i].pos - self.ball[i+1].pos) < 2*self.size :
                    self.ball[i].v, self.ball[i+1].v = self.collision(self.ball[i].v, self.ball[i+1].v, self.ball[i].pos, self.ball[i+1].pos)
                    self.hit_t += 1
                    print(f"hit! {self.hit_t} times")
                
    def btw_collision(self):
        for i in self.ball:
            if abs(i.pos.x - (self.side - self.thk)) <= self.size or abs(i.pos.x + (self.side - self.thk)) <= self.size:    #請思考如何判斷球1撞擊左右兩牆
                i.v.x = -i.v.x
            if abs(i.pos.y - (self.side - self.thk)) <= self.size or abs(i.pos.y + (self.side - self.thk)) <= self.size:    #請思考如何判斷球1撞擊上下兩牆
                i.v.y = -i.v.y
            if abs(i.pos.z - (self.side - self.thk)) <= self.size or abs(i.pos.z + (self.side - self.thk)) <= self.size:    #請思考如何判斷球1撞擊前後兩牆
                i.v.z = -i.v.z

    def update(self):
        for i in self.ball:
            i.pos = i.pos + i.v*dt

    def run_stop(self, b1):
        global run
        if run == False:
            b1.text = "stop"
        elif run == True:
            b1.text = "run"
        run = not run
    
    def reset(self):
        global reset
        reset = not reset

    def end(self):
        global end
        end = True

    def changeSize(self):
        for i in self.ball:
            i.radius = self.size

Ball = ball()

while not end:
    rate(1/dt)
    if run:
        Ball.update()
        Ball.btb_collision()
        Ball.btw_collision()
    if reset:
        Ball.init()

print("end")