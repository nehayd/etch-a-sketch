from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def turn_left():
    new_heding = tim.heading + 10
    tim.setheading(new_heding)

def turn_right():
    new_heding = tim.heading - 10
    tim.setheading(new_heding)

def move_counter_clockwise():
    tim.circle(100, -60)

def move_clockwise():
    tim.circle(100, 60)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
