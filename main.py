import turtle
from termcolor import colored


# Defining functions
def show_error(text):
    print(colored(text, 'red'))


# Initializing Window
window = turtle.Screen()
window.bgcolor("black")
pen = turtle.Turtle()
pen.color("white")
pen.right(270)
exit_program = False
print()

while not exit_program:
    command = input("-").lower().rstrip(" ")
    if command[:2] == "fd":
        pen.forward(int(command[2:]))
    elif command[:2] == "bk":
        pen.back(int(command[2:]))
    elif command[:2] == "rt":
        pen.right(int(command[2:]))
    elif command[:2] == "lt":
        pen.left(int(command[2:]))
    elif command == "ht":
        pen.hideturtle()
    elif command == "cs":
        pen.clear()
    elif command == "st":
        pen.showturtle()
    elif command == "home":
        pen.penup()
        pen.home()
        pen.pendown()
    elif command == "pu":
        pen.penup()
    elif command == "pd":
        pen.pendown()
    elif command == "bye":
        exit_program = True
    else:
        show_error("I do not understand.")
