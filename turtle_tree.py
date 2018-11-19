import turtle
t=turtle.Turtle()
def f(w):
    if w>=1:
        s=t.pensize()
        t.pensize(w)
        t.fd(w*9)
        t.rt(20)
        f(w*.75)
        t.lt(40)
        f(w*.75)
        t.right(20)
        t.bk(w*9)
        t.pensize(w)
t.speed(9)
f(9)
t.ht()
input()