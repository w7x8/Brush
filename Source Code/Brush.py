import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.title("Brush")
screen.bgcolor("snow")
screen.setup(width=800, height=800)

brush = Turtle("arrow")
brush.speed(-1)
brush.width(3)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']


def stamp():
    brush.stamp()


def up():
    brush.seth(90)
    brush.forward(100)


def down():
    brush.seth(270)
    brush.forward(100)


def left():
    brush.seth(180)
    brush.forward(100)


def right():
    brush.seth(0)
    brush.forward(100)


def dragging(x, y):
    brush.ondrag(None)
    brush.setheading(brush.towards(x, y))
    brush.goto(x, y)
    brush.ondrag(dragging)


def clickright(x, y):
    brush.clear()


def middleclick(x, y):
    brush.color(random.choice(colors))


def clickleftscreen(x, y):
    brush.penup()
    brush.setpos(x, y)
    brush.pendown()


def main():
    turtle.listen()

    brush.ondrag(dragging)

    turtle.onscreenclick(clickright, 3)
    turtle.onscreenclick(middleclick, 2)

    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.onkey(stamp, 's')
    turtle.onscreenclick(clickleftscreen, 1)

    screen.mainloop()


main()
