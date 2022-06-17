from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)
user_guess = screen.textinput("Make Your Bet", "Which turtle will win the race? Enter your color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for n in range(0, 6):
    tim = Turtle("turtle")
    tim.color(colors[n])
    tim.penup()
    tim.goto(-230, y_positions[n])
    turtles.append(tim)

tocontinue = True
while tocontinue:
    for n in range(0, 6):
        turtles[n].forward(random.randint(0,25))
        if turtles[n].xcor() >= 250:
            tocontinue = False;
            turtlewon = n
            break

if user_guess == colors[n]:
    print(f"You won! The {colors[n]} turtle won!")
else:
    print(f"You lost! The {colors[n]} turtle won!")


screen.exitonclick()