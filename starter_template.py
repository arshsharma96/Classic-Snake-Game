# importing the graphics modules
import turtle

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 20  # Milliseconds between screen updates


def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY) 


# creating the window for drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Program title")
screen.bgcolor("cyan")
screen.tracer(0)  # Turns off automatic animation

# creating a turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# set animation in motion state
move_turtle()

# to end all turtle programs
turtle.done()
