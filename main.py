import numpy as np
import turtle as tt
import random
import math

def put_dot(x, y):
    tt.penup()
    tt.setpos(x, y)
    tt.pendown()
    tt.dot(5)


tt.hideturtle()

orgPoints = np.array([[0, 250], [150, 0], [-150, 0]])
P = np.array([[0, 250], [150, 0], [-150, 0]])



def make_tri(orgPoints, P,speed = 1, iterations=1000):
    tt.speed(1)
    for x, y in orgPoints:
        put_dot(x, y)
    for i in range(iterations):
        # if(i > math.exp(speed)):
        #     speed+=1
        #     tt.speed(speed) 
        if i == 20:
            tt.speed(0)
        chOrgPoint = random.choice(orgPoints)
        chPoint = random.choice(P)
        x = (chOrgPoint[0] + chPoint[0]) / 2
        y = (chOrgPoint[1] + chPoint[1]) / 2
        put_dot(x, y)
        row = np.array([x, y])
        P = np.append(P, [row], axis=0);


# print(make_tri(orgPoints, P))
make_tri(orgPoints, P, iterations=10000)

# put_dot(0,250)  # Original First Dot
# put_dot(150, 0)
# put_dot(-150,0)
print(tt.position())
tt.done()
