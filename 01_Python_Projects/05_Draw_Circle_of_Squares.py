# Project name: Draw Circle of Squares
# Course: Udacity Full Stack Nanodegree

# -----------------------------------

import turtle

def draw_square(some_turtle):
    for x in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)    

def draw_art():
    # Draw window
    window = turtle.Screen()
    window.bgcolor("gold")
    # Create turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)
    # Draw
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_art()


