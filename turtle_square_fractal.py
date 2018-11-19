# Draw a Koch snowflake
import turtle

window = turtle.Screen()
turtle = turtle.Turtle()


window.tracer(1000)

def koch(a, order):
    if order > 0:
        for i in [a / 3, a, a, a / 3]:
            koch(i, order - 1)
            turtle.right(90)
        turtle.left(45)

    else:
        turtle.forward(a)


koch(100,5)
window.update()
window.exitonclick()
