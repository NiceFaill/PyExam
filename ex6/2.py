from turtle import *

tracer(0)
k = 30
left(90)

pencolor("red")

for i in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)

penup()

forward(k)
right(90)
up(5)
left(90)

pendown()
for i in range(9):
    forward(53 * k)
    right(90)
    forward(73 * k)
    right(90)

penup()
