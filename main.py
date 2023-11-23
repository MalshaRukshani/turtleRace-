import turtle
from turtle import Turtle,Screen
import random

is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title ="Make your bet", prompt="which turtle will win the race?Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle =[]


for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on== False
            winning_color = turtle.pencolor()
            if winning_color== user_bet:
                print("you are the winner")
            else:
                print(f"you are lose. The winner is {winning_color}")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()