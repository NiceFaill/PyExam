from turtle import *

tracer(0)
k = 30
left(90)

for i in range(4):
    fd(14 * k)
    rt(90)
    
for i in range(5):
    fd(5 * k)
    rt(45)

penup()
pencolor("red")    
for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x * k, y * k)
        dot(5)
done()