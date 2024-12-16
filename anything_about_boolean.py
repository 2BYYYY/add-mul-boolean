import turtle as t

def draw_table(rows, cols, cell_width, cell_height, boolean_value_1):
    t.pensize(5)
    start_x = -cols * cell_width // 2
    start_y = rows * cell_height // 2

    # Draw horizontal lines
    for r in range(rows + 1):
        t.penup()
        t.goto(start_x, start_y - r * cell_height)  # Start of each horizontal line
        t.pendown()
        t.forward(cols * cell_width)  # Draw horizontal line

    # Draw vertical lines
    for c in range(cols + 1):
        t.penup()
        t.goto(start_x + c * cell_width, start_y)  # Start of each vertical line
        t.pendown()
        t.setheading(-90)  # Face downward
        t.forward(rows * cell_height)  # Draw vertical line

    # Write '1' in the center of each cell and print coordinates
    running = 0
    for r in range(0,4):
        for c in range(rows):
            running +=1
            
            # Calculate center coordinates
            center_x = start_x + (r * cell_width) + (cell_width // 2)
            center_y = start_y - (c * cell_height) - (cell_height // 2)

            # Write '1' in each cell at the center coordinates
            t.penup()
            t.goto(center_x, center_y - 10)  # Adjust slightly for vertical alignment
            if r == 0:
                if running <= 2:
                    if boolean_value_1 == 1:
                        t.write('1', align="center", font=("Arial", 16, "bold"))
                    else:
                        t.write('0', align="center", font=("Arial", 16, "bold"))
                elif running > 2:
                    if boolean_value_1 == 1:
                        t.write('0', align="center", font=("Arial", 16, "bold"))
                    else:
                        t.write('1', align="center", font=("Arial", 16, "bold"))
                        
            elif r == 1:
                if running < 9:
                    if running % 2:
                        if boolean_value_1 == 1:
                            t.write('1', align="center", font=("Arial", 16, "bold"))
                        else:
                            t.write('0', align="center", font=("Arial", 16, "bold"))
                    else:
                        if boolean_value_1 == 1:
                            t.write('0', align="center", font=("Arial", 16, "bold"))
                        else:
                            t.write('1', align="center", font=("Arial", 16, "bold"))
            elif r == 2:
                if (boolean_value_1 == 0 and running == 9):
                    t.write('0', align="center", font=("Arial", 16, "bold"))
                elif boolean_value_1 == 0:
                    t.write('1', align="center", font=("Arial", 16, "bold"))
                if (boolean_value_1 == 1 and running == 12):
                    t.write('0', align="center", font=("Arial", 16, "bold"))
                elif boolean_value_1 == 1:
                    t.write('1', align="center", font=("Arial", 16, "bold"))

            elif r == 3:
                if (boolean_value_1 == 0 and running == 16):
                    t.write('1', align="center", font=("Arial", 16, "bold"))
                elif boolean_value_1 == 0:
                    t.write('0', align="center", font=("Arial", 16, "bold"))
                elif (boolean_value_1 == 1 and running == 13):
                    t.write('1', align="center", font=("Arial", 16, "bold"))
                elif boolean_value_1 == 1:
                    t.write('0', align="center", font=("Arial", 16, "bold"))


            # Print the center coordinates of each cell
            # print(f"Cell ({r}, {c}) center: ({center_x}, {center_y})")
    t.goto(-350,150)
    t.write('Sum', align="center", font=("Arial", 35, "bold"))
    t.goto(350,150)
    t.write('Product', align="center", font=("Arial", 35, "bold"))
    t.goto(-150,100)
    t.write('x', align="center", font=("Arial", 35, "bold"))
    t.goto(-50,100)
    t.write('y', align="center", font=("Arial", 35, "bold"))
    t.goto(50,100)
    t.write('x+y', align="center", font=("Arial", 35, "bold"))
    t.goto(150,100)
    t.write('xy', align="center", font=("Arial", 35, "bold"))
    t.goto(350,-160)
    t.write('xy', align="center", font=("Arial", 35, "bold"))
    t.goto(-350,-160)
    t.write('x + y', align="center", font=("Arial", 35, "bold"))


def draw_number_one():
    # t.goto(-350, 50)  # Adjust the position to the left side of the table
    # t.goto(300, 50)  # Adjust the position to the right side of the table
    t.pencolor("yellow")
    t.pensize(10)
    t.pendown()
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(175)
    t.left(90)
    t.forward(90)
    t.left(45)
    t.forward(90)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(40)
    t.fillcolor("white")  # Set the fill color
    t.penup()

def draw_zero(bool_num):
    # t.goto(430, -70)  # Adjust the position to the right side of the table
    # t.goto(-480, 15)  # Adjust the position to the left side of the table
    t.pendown()
    t.circle(120)
    t.penup()
    if bool_num == 0:
        t.goto(-410, 15)  # Adjust the position to the right side of the table
        t.pendown()
        t.circle(50)
        t.penup()
    elif bool_num == 1:
        t.goto(400, -5)  # Adjust the position to the right side of the table
        t.pendown()
        t.circle(50)
        t.penup()
    else:
        t.goto(380, -20)  # Adjust the position to the right side of the table
        t.pendown()
        t.circle(50)
        t.penup()

def add_bool(bool_val, bool_val2):
    if bool_val == 0 and bool_val2 == 0:
        t.goto(-480, 15)
        draw_zero(0)
    else:
        t.goto(-350, 50)  # Adjust the position to the left side of the table
        draw_number_one()

def mul_bool(bool_val, bool_val2):
    if bool_val == 1 and bool_val2 == 1:
        t.goto(300, 50)  
        t.setheading(-90)
        draw_number_one()
    elif bool_val == 0 and bool_val2 == 0:
        t.setheading(60)
        t.goto(460, -40)  
        draw_zero(1)
    else:
        t.goto(430, -70)  
        draw_zero(2)