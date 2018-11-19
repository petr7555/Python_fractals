# Draw a Koch snowflake
import turtle

window = turtle.Screen()
turtle = turtle.Turtle()

def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a / 3, order - 1)
            turtle.left(t)
    else:
        turtle.forward(a)

# Choose colours and size
turtle.color("sky blue", "white")
window.bgcolor("black")
size = 400
order = 5

# Ensure snowflake is centred
turtle.penup()
turtle.backward(size/1.732)
turtle.left(30)
turtle.pendown()

# Make it fast
window.tracer(100)
turtle.hideturtle()

turtle.begin_fill()

# Three Koch curves
for i in range(3):
    koch(size, order)
    turtle.right(120)

turtle.end_fill()

# Make the last parts appear
window.update()
window.exitonclick()
