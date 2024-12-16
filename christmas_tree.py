import turtle as t
import random
import math

def draw_triangle(size):
    t.fillcolor("green")
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
        t.dot(10, "yellow")
    t.end_fill()


def draw_tree():
    base_size = 40
    trunk_height = 50
    trunk_color = "brown"

        # Draw trunk
    t.penup()
    t.goto(-20, -350)
    t.pendown()
    t.color(trunk_color)
    t.fillcolor(trunk_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(trunk_height)
        t.right(90)
    t.end_fill()

    t.pencolor("white")
    t.bgcolor("#071330")
    t.penup()
    t.goto((-base_size * 5 / 2)+18, -350)
    t.pendown()

    # Draw tree
    for level in range(1, 5):
        draw_triangle(base_size *(5 - level))
        t.penup()
        t.goto((0 - base_size *
                    (5 - level) / 2)+18,
                    -350 + (level * base_size)
                    + ((level * base_size) * 0.5))
        t.pendown()

    t.penup()
    t.color("yellow")
    t.goto((0 - base_size - 5) + 23,
                -325 + (5 * base_size))
    t.begin_fill()
    t.pendown()

    for i in range(5):
        t.forward(40)
        t.right(144)

    t.end_fill()
    t.setheading(-90)
    t.penup()

def draw_triangle(size):
    t.fillcolor("green")
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
        t.dot(10, "yellow")
    t.end_fill()


def draw_tree():
    base_size = 40
    trunk_height = 50
    trunk_color = "brown"

        # Draw trunk
    t.penup()
    t.goto(-20, -350)
    t.pendown()
    t.color(trunk_color)
    t.fillcolor(trunk_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(trunk_height)
        t.right(90)
    t.end_fill()

    t.pencolor("white")
    t.bgcolor("#071330")
    t.penup()
    t.goto((-base_size * 5 / 2)+18, -350)
    t.pendown()

    # Draw tree
    for level in range(1, 5):
        draw_triangle(base_size *(5 - level))
        t.penup()
        t.goto((0 - base_size *
                    (5 - level) / 2)+18,
                    -350 + (level * base_size)
                    + ((level * base_size) * 0.5))
        t.pendown()

    t.penup()
    t.color("yellow")
    t.goto((0 - base_size - 5) + 23,
                -325 + (5 * base_size))
    t.begin_fill()
    t.pendown()

    for i in range(5):
        t.forward(40)
        t.right(144)

    t.end_fill()
    t.setheading(-90)
    t.penup()

# Function to draw a star
def draw_star(x, y, size, color):
    t.goto(x, y)
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def create_random_stars():
    colors = ["white", "yellow", "lightblue", "pink"]
    star_positions = []  # List to keep track of drawn star positions

    for _ in range(15):
        while True:
            y_left = random.randint(-400, -150)  # Random x-coordinate
            x_left = random.randint(-700, -100)  # Random y-coordinate
            size = random.randint(10, 30)  # Random size
            color = random.choice(colors)  # Random color
            
            # Check distance from all previously drawn stars
            too_close_left = any(math.sqrt((x_left - px) ** 2 + (y_left - py) ** 2) < 50 for px, py in star_positions)

            if not too_close_left:  # If no other star is too close, draw the star
                draw_star(x_left, y_left, size, color)
                star_positions.append((x_left, y_left))  # Add this star's position
                print([x_left, y_left])  # Optional: Debugging to see star positions
                break  # Exit the loop and move to the next star
    for _ in range(15):
        while True:
            y_right = random.randint(-400, -150)  # Random x-coordinate
            x_right = random.randint(100, 700)  # Random y-coordinate
            size = random.randint(10, 30)  # Random size
            color = random.choice(colors)  # Random color
            
            # Check distance from all previously drawn stars
            too_close_right = any(math.sqrt((x_right - px) ** 2 + (y_right - py) ** 2) < 50 for px, py in star_positions)

            if not too_close_right:
                draw_star(x_right, y_right, size, color)
                star_positions.append((x_right, y_right))  
                print([x_right, y_right])  
                break 