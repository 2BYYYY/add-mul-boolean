import turtle as t
import random

def draw_christmaslights():
    lights_distance = [350,150,-150,-350,-650]
    lights_size = [150,100,150,100,150]
    for dis,size in zip(lights_distance,lights_size):
        t.goto(dis, 400)
        t.pendown()
        t.setheading(-90)
        t.circle(size, 180)
        t.penup()

    color_balls = ["red", "green", "blue", "yellow"]

    x_balls = [-640, -330, -130, 170, 370, 310, 230, -180, -270, 420, 620, 120, -80, -380, -580, 520, 20, -480]  # x positions for the balls (adjust as needed)
    y_balls = [390, 390, 390, 390, 390, 310, 310, 310, 310, 290, 290, 290, 290, 290, 290, 250, 250, 250]  # y positions for the balls (along the arcs)

    # Loop to draw balls at specified locations
    for x, y in zip(x_balls, y_balls):
        t.goto(x, y)  # Position the turtle at the coordinates for each ball
        t.pendown()
        t.color(random.choice(color_balls))  # Set the fill color (can be any color, e.g., 'red', 'blue', 'green')
        t.begin_fill()  # Begin the fill
        t.circle(20)  # Draw a small circle for the ball with radius 10
        t.end_fill()  # End the fill
        t.penup()

    t.setheading(0)