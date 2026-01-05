from turtle import Turtle, Screen, colormode
import random
# import colorgram

geeny_turtle = Turtle()
geeny_screen = Screen()
# colormode(255)

def w_moving():

    geeny_turtle.forward(15)

def s_moving():

    geeny_turtle.backward(15)

def a_anticlockwise():
    x = random.randint(0, 361)

    geeny_turtle.left(x)

def d_clockwise():
    x = random.randint(0, 361)

    geeny_turtle.right(x)

def c_cleanup():

    geeny_turtle.reset()
# def func_listen():

def control():
    geeny_screen.listen()
    geeny_screen.onkey(key='w', fun=w_moving)
    geeny_screen.onkey(key='s', fun=s_moving)
    geeny_screen.onkey(key='a', fun=a_anticlockwise)
    geeny_screen.onkey(key='d', fun=d_clockwise)
    geeny_screen.onkey(key='c', fun=c_cleanup)
    geeny_screen.exitonclick()

control()