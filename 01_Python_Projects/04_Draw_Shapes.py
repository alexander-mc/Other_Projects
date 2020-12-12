# Project name: Draw Shapes
# Course: Udacity Full Stack Nanodegree

# -----------------------------------

import turtle

window = turtle.Screen()
window.bgcolor("gold")

brad = turtle.Turtle()
brad.shape("square")
brad.color("blue")
brad.speed(5)

chris = turtle.Turtle()
chris.shape("triangle")
chris.color("red")

andre = turtle.Turtle()
andre.shape("turtle")
andre.color("green")

def draw_circle():
    andre.circle(100)

def draw_square():
    for x in range(4):
        brad.forward(200)
        brad.right(90)

def draw_triangle():
    for x in range(3):
        chris.right(120)
        chris.forward(200)
    
draw_square()
draw_circle()
draw_triangle()
window.exitonclick()
