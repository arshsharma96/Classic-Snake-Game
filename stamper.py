# importing the graphics modules
import turtle

# define program constants
WIDTH = 500
HEIGHT = 500

# creating the window for drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Stamping")
screen.bgcolor("cyan")

# creating a turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("red")
stamper.shapesize(
    50 / 20)  # 20 is default size of square shape in turtle so 50 / 20 is 50 pixels as this leads to pixel controlling
stamper.stamp()
stamper.penup()  # so the stamp does not make a mark when moving
stamper.shapesize(10 / 20)
stamper.goto(100, 100)
stamper.stamp()

# to end all turtle programs
turtle.done()


"""
Uses of Turtle Graphics Stamp
1. Board Games
2. 2D Games such as Snake / Tron clones
3. Exploring mazes
4. Pixel Art
"""
