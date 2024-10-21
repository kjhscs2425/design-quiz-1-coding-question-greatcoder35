import turtle
from turtle import *

length = 20 #side length of base octagon
for i in range (5):
    for _ in range(8):
        forward(length*(i+1))
        right(45)
    penup()
    left(90)
    forward(length)
    right(90)
    backward(length/2)
    pendown()

exitonclick()