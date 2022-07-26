from turtle import Turtle, Screen
import random

screen = Screen()

# def move_forward():
#     tom.fd(100)
#
#
# def back_word():
#     tom.backward(100)
#
#
# def counter_clockwise():
#     tom.lt(10)
#
#
# def clockwise():
#     tom.rt(10)
#
#
# def clear_screen():
#     tom.clear()
#     tom.penup()
#     tom.home()
#     tom.pendown()
#
#
# def draw_circle():
#     tom.circle(100)
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=back_word)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="c", fun=clear_screen)
# screen.onkey(key="o", fun=draw_circle)

# whn a function(move_forward) is passed to another function tom.onkey(),we won't pass (), whn we pass () function will
# execute than and there.we want our fun to execute after we press space

# day -19 challenge
screen.setup(width=500, height=400)  # 500: width , 400 : height
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-90, -60, -30, 0, 30, 60]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # .goto(x,y) => tells the turtle to move to x,y coordinates
    # specified
    all_turtles.append(new_turtle)

# it's possible to create a different instance(objects) of turtle class of same name,until we have different states
# states are ntg but different values.

is_race_on = False

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 15)
        turtle.fd(rand_distance)

screen.exitonclick()
