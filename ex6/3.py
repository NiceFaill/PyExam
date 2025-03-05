from turtle import *

tracer(0)
k = 30
left(90)

for i in range(4):
    forward(14 * k)
    right(90)
    forward(120 * k)
    left(90)

for x in range(-15, 15):
    for y in range(0, 15):
        goto(x * k, y * k)
        dot(5)
done()