# importing the graphics modules
import turtle

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 400  # in Milliseconds

# global variables

# determines how much snake moves in each direction
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

snake_direction = "up"


def go_up():
    global snake_direction

    # condition to stop pressing the opposite key
    if snake_direction != "down":
        snake_direction = "up"


def go_down():
    global snake_direction

    # condition to stop pressing the opposite key
    if snake_direction != "up":
        snake_direction = "down"


def go_left():
    global snake_direction

    # condition to stop pressing the opposite key
    if snake_direction != "right":
        snake_direction = "left"


def go_right():
    global snake_direction

    # condition to stop pressing the opposite key
    if snake_direction != "left":
        snake_direction = "right"


def move_snake():
    stamper.clearstamps()  # clears existing stamps

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # add new head to snake body
    snake.append(new_head)

    # remove the tail of the snake body
    snake.pop(0)

    # Draw snake for the first time
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    # Refresh screen
    screen.update()

    # Rinse and repeat
    turtle.ontimer(move_snake, DELAY)


# creating the window for drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # disables automatic automation

# Event handlers
screen.listen()

# action to be taken on pressing the key
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# creating a turtle
stamper = turtle.Turtle()
stamper.shape("square")
stamper.penup()  # so the stamp does not make a mark when moving

# create snake as a list of coordinates pairs
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# Draw snake for the first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# Set animation in motion state
move_snake()

# Finish nicely
turtle.done()
