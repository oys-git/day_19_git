from turtle import Turtle, Screen, colormode
import random
# import colorgram

geeny_screen = Screen()
geeny_screen.setup(width=500, height=400)
user_bet = geeny_screen.textinput(title="pick a turtle color", prompt=" ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-150, -100, -50, 0, 50, 100]

# class geeny_race:
for i in range(6):
    geeny_turtle = Turtle(shape="turtle")
    geeny_turtle.penup()
    geeny_turtle.goto(x=-230, y=y[i])
    geeny_turtle.color(color[i])
    
geeny_screen.exitonclick()
    




