import numpy as np
import matplotlib.pyplot as plt

Q1 = 1  #Q1的電荷量
k = 1   #庫倫常數
x1 = 0  #Q1的x座標
y1 = 0  #Q1的x座標

def V(x,y): #電位
    V1 = Q1*k/(x**2+y**2)**0.5 #請思考如何算出(x,y)處的電位
    return V1 

#利用linspace語法產生1D-array(陣列)
x = np.linspace(-50,50,50) 
y = np.linspace(-50,50,50)

#利用meshgrid語法產生2D-array，可簡單想成x-y平面上的網格
X,Y = np.meshgrid(x,y)

plt.figure(figsize=(8,8))     #設定圖表大小
equal_V = plt.contourf(X, Y, V(X, Y), levels = np.linspace(0,0.1,21))   #繪製等高線圖

plt.scatter(x1,y1,s=100,color = "red")  #加入Q1電荷位置
plt.annotate('Q1', (x1+1, y1+1))    #加入Q1的標籤    
plt.show() #輸出圖表結果