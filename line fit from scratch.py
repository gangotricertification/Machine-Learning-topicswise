import numpy as np
import matplotlib.pyplot as plt
import random
import sys


x=[]
y=[]

#--------------------------choose random 30 points in limit of -100 to 100-----------------------------------
for i in range(30):
    x.append(random.randint(-100,100))

for j in range(30):
    y.append(random.randint(-100,100))

             
x1=np.reshape(x,(-1,1))
y1=np.reshape(y,(-1,1))



#--------------------compbine both x and y to make coordinate set -----------------------------------------
pair=np.concatenate((x1,y1),axis=1)


count=0
sum2=sys.maxsize

#-------------------to find best two coordinates to make best fit line-------------------------------------
for i in range(30):
    for j in range(i,30):
        new=[]
        p1=pair[i]
        p2=pair[j]
        for k in range(30):
            p3=pair[k]
            d=np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1)
            if(d<0):
                d= -1*d
            new.append(d)
        sum1=sum(new)
        if(sum1<sum2):
            sum2=sum1
            pair1=p1
            pair2=p2
#--------------------best two coordinates-------------------------
print(pair1)
print(pair2)
print("----------gangotricertification@gmail.com---------------")
#------------------find slope and intercept to draw lines--------------
q1,w1=pair1
q2,w2=pair2
m=(w2-w1)/(q2-q1)
x2,y2=pair1
c = y2-m*x2

x3=np.linspace(-100,100,100)
y3 = m*x3 + c

plt.plot(x3,y3,linestyle='--')
plt.grid()

plt.scatter(x,y)

plt.show()

                
                
                        
