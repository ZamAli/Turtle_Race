from turtle import Turtle, Screen
import random


my_screen = Screen()
my_screen.setup(500, 400, 0)
user_choice= my_screen.textinput("Turtle Race", "Who will win the race?Select your color: ")
colors = ["red", "blue", "green", "purple", "orange"]
tim_list = []
race_on = False
for k in range(5):
    tim = Turtle()
    tim.shape("turtle")
    tim.color(colors[k])
    tim.teleport(x=-230, y=k*30)
    tim_list.append(tim)

if user_choice:
    race_on = True

while race_on:
    for tim in tim_list:
        tim.penup()
        rand_distance = random.randint(0,10)
        tim.forward(rand_distance)
        x = tim.pos()
        if x[0] >= 230:
            if user_choice == tim.color()[0]:
                print (f"you won!! {user_choice} is first")
                race_on = False
            else:
                print(f"you lost!! {tim.color()[0]} is first")
                race_on = False
