from turtle import *
tracer(0)
left(90)
k = 20

for i in range(4):
    fd(7 * k)
    rt(90)
    fd(7 * k)
    lt(90)
    fd(7 * k)
    lt(90)
    
penup()
pencolor("red")
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(5)
done()