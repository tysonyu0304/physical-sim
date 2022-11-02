from vpython import *
import random
import os

dt = 0.01 #時間間隔 0.01 秒
run = False
reset = False
end = False
mtrail = True
speed = 2.0

class ball():
    def __init__(self):
        self.size = 0.1
        self.m = 2
        self.side = 4.0
        self.thk = 0.3
        self.s2 = 2*self.side - self.thk
        self.s3 = 2*self.side + self.thk
        self.num = 5
        self.ball = []
        self.colors = [color.yellow, color.green, color.black, color.orange]
        self.start()
    
    def start(self):
        self.scene = canvas(width=800, height=800, center = vec(0,0,0), background=vec(0.6,0.8,0.8)) #設定畫面
        self.b_slide = slider(pos=self.scene.title_anchor, min=0, max=500, step=1, value=0, length=600, right=15, bind=self.b_slider)
        self.b_text = wtext(pos=self.scene.title_anchor, text="ball numbers: 0")
        self.b_n_apply = button(text="apply", pos=self.scene.title_anchor, bind=self.apply)
        self.v_slide = slider(pos=self.scene.title_anchor, min=0.1, max=5.0, step=0.1, value=2.0, length=400, right=15, bind=self.v_slider)
        self.v_apply = button(pos=self.scene.title_anchor, text="apply", bind=self.apply_v)
        self.v_text = wtext(pos=self.scene.title_anchor, text="ball speed: 2.0")
        self.wall_R = box(pos=vector(self.side, 0, 0), size=vector(self.thk, self.s2, self.s3),  color=color.white)
        self.wall_L = box(pos=vector(-self.side, 0, 0), size=vector(self.thk, self.s2, self.s3),  color=color.white)
        self.wall_B = box(pos=vector(0, -self.side, 0), size=vector(self.s3, self.thk, self.s3),  color=color.white)
        self.wall_T = box(pos=vector(0, self.side, 0), size=vector(self.s3, self.thk, self.s3),  color=color.white)
        self.wall_BK = box(pos=vector(0, 0, -self.side), size=vector(self.s2, self.s2, self.thk), color=color.gray(0.7))
        self.b_run = button(text="run", pos=self.scene.caption_anchor, bind=self.run_stop)
        self.b_reset = button(text="reset", pos=self.scene.caption_anchor, bind=self.reset)
        self.b_end = button(text="end", pos=self.scene.caption_anchor, bind=self.end)
        self.trail = wtext(pos=self.scene.caption_anchor, text="Make Trail")
        self.b_mtrail = button(text="No!", pos=self.scene.caption_anchor, bind=self.mtrail)

    def init(self):
        global reset
        self.num = 0
        self.ball = []
        self.scene.visible = False
        self.b_slide.delete()
        self.b_n_apply.delete()
        self.b_text.text = ""
        self.trail.text = ""
        self.v_text = ""
        self.b_text.delete()
        self.trail.delete()
        self.b_mtrail.delete()
        self.b_run.delete()
        self.b_reset.delete()
        self.b_end.delete()
        self.scene.delete()
        self.v_slide.delete()
        self.v_apply.delete()
        self.start()
        reset = False

    def pos_ganerater(self):
        x = random.uniform(-((self.s2/2 - self.thk - self.size)), ((self.s2/2 - self.thk - self.size)))
        y = random.uniform(-((self.s2/2 - self.thk - self.size)), ((self.s2/2 - self.thk - self.size)))
        z = random.uniform(-((self.s2/2 - self.thk - self.size)), ((self.s2/2 - self.thk - self.size)))
        return vec(x, y, z)

    def v_ganerater(self):
        x = random.uniform(-2, 2)
        y = random.uniform(-2, 2)
        z = random.uniform(-2, 2)
        v = vec(x, y, z)
        return v/mag(v)

    def ball_ganerater(self):
        for i in range(self.num):
            self.ball.append(sphere(pos=self.pos_ganerater(), v=self.v_ganerater()*speed, radius=self.size, color=self.colors[random.randint(0,3)], make_trail=mtrail, retain=100)) #畫好多球

    def collision(self, v1, v2, x1, x2):
        v1_f = v1 - (2*self.m/(self.m + self.m))*((dot(v1 - v2, x1 - x2))/(mag(x1 - x2)**2))*(x1 - x2)   #請嘗試將碰撞公式填入其中
        v2_f = v2 - (2*self.m/(self.m + self.m))*((dot(v2 - v1, x2 - x1))/(mag(x2 - x1)**2))*(x2 - x1)
        return (v1_f, v2_f)

    def btb_collision(self):
        for i in range(len(self.ball)):
            for j in range(i+1, len(self.ball)-1):
                #若兩球球心距離小於兩倍球半徑，則代入碰撞公式改變速度
                if mag(self.ball[i].pos - self.ball[j].pos) < 2*self.size :
                    self.ball[i].v, self.ball[j].v = self.collision(self.ball[i].v, self.ball[j].v, self.ball[i].pos, self.ball[j].pos)
                    print("Hit!")
                
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

    def run_stop(self, b_run):
        global run
        if run == False:
            b_run.text = "stop"
        elif run == True:
            b_run.text = "run"
        run = not run
    
    def reset(self):
        global reset
        reset = not reset

    def end(self):
        global end
        end = True

    def b_slider(self):
        self.b_text.text = f"ball numbers: {self.b_slide.value}"

    def apply(self):
        for i in self.ball:
            i.clear_trail()
            i.visible = False
        self.ball = []
        self.num = self.b_slide.value
        self.ball_ganerater()
        self.b_run.text = "stop"
        global run
        run = True
    
    def mtrail(self):
        global mtrail
        if mtrail == True:
            mtrail = False
            for i in self.ball:
                i.make_trail = False
                i.clear_trail()
            self.b_mtrail.text = "Yes!"
        elif mtrail == False:
            mtrail = True
            for i in self.ball:
                i.make_trail = True
            self.b_mtrail.text = "No!"

    def v_slider(self):
        self.v_text.text = f"ball speed: {self.v_slide.value}"

    def apply_v(self):
        global speed
        for i in self.ball:
            i.v = i.v/speed*self.v_slide.value
        speed = self.v_slide.value
        

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
os._exit(0)