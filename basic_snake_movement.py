# importing the graphics modules
import turtle
import random

WIDTH = 500
HEIGHT = 500
DELAY = 400  # in Milliseconds this controls the speed of the snake
FOOD_SIZE = 10  # the size of the food

# global variables

# determines how much snake moves in each direction
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

snake_direction = "up"


# moves the snake upwards
def go_up():
    global snake_direction

    # condition to stop pressing the opposite key
    if snake_direction != "down":
        snake_direction = "up"


# moves snake downwards
def go_down():
    global snake_direction

    # condition to stop pressing the opposite key
    if snake_direction != "up":
        snake_direction = "down"


# moves snake left
def go_left():
    global snake_direction

    # condition to stop pressing the opposite key
    if snake_direction != "right":
        snake_direction = "left"


# moves snake right
def go_right():
    global snake_direction

    # condition to stop pressing the opposite key
    if snake_direction != "left":
        snake_direction = "right"


# implements pythagoras theorem
# it is to check the closest pixels when snake eats the food
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x2) ** 2) ** 0.5
    return distance


# detect food collisions
def food_collision():
    global food_pos
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True

    return False


# to create the random food positions
def get_random_food_pos():
    x = random.randint(- WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return x, y


# main method for the snake movement
def move_snake():
    stamper.clearstamps()  # clears existing stamps

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    # this enables if snake touches the wall or itself the game ends
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 or new_head[1] < - HEIGHT / 2 or \
            new_head[1] > HEIGHT / 2:
        turtle.bye()  # closing the program
    else:
        # add new head to snake body
        snake.append(new_head)

        # check for food collisions
        if not food_collision():
            # remove the tail of the snake body
            snake.pop(0)  # keep the snake length same unless fed

        # Draw snake for the first time
        for segmentIntMvSnake in snake:
            stamper.goto(segmentIntMvSnake[0], segmentIntMvSnake[1])
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

# food
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOOD_SIZE / 10)
food.color("blue")
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)

# Set animation in motion state
move_snake()

# Finish nicely
turtle.done()
