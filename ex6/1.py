from turtle import *

tracer(0)
left(90)
k = 30

pencolor("red")

for i in range(7):
    forward(10 * k)
    right(120)
pu()
pencolor("black")
for x in range(-10, 15):
    for y in range(0, 20):
        goto(x * k, y * k)
        dot(5)

done()