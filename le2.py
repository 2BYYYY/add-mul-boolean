import turtle as t
from tkinter import Tk, Label, Entry, Button, Frame
import christmas_tree
import christmas_lights
import anything_about_boolean

#screen height and width
screen_x = 1300
screen_y = 800

def screen():
    # Set up the screen and t
    screen = t.Screen()
    screen.title("Discrete Structures")
    screen.bgcolor("black")  # Set background to black
    screen.setup(screen_x, screen_y)

    t.color("white")  # Set the drawing color to white
    t.speed(0)  # Slow down the drawing

    # Table parameters for a 4x4 table
    rows = 4
    cols = 4
    cell_width = 100
    cell_height = 50
    booleanValue = 1
    # Draw the table and write '1' in each cell
    anything_about_boolean.draw_table(rows, cols, cell_width, cell_height, booleanValue)
    christmas_lights.draw_christmaslights()
    christmas_tree.draw_tree()
    christmas_tree.create_random_stars()


# Function to reset the screen and button states
def reset_screen():
    # Reset turtle screen
    t.clearscreen()
    screen()

    # Reset button states
    calculate_button.config(state="normal")
    status_label.config(text="Screen reset. You can perform operations again.")

# Function to handle Add Bool operation
screen()

# Tkinter GUI setup
tk_screen = Tk()
tk_screen.title("5.3.2.5 Learning Evidence 2")
tk_screen.configure(bg="#1e1e1e")

# Header label
header = Label(
    tk_screen, text="Boolean Operations", font=("Arial", 18, "bold"), fg="#ffffff", bg="#1e1e1e"
)
header.grid(row=0, column=0, columnspan=2, pady=10)

# Input fields
Label(
    tk_screen, text="Boolean Value 1 (0 or 1):", font=("Arial", 12), fg="#ffffff", bg="#1e1e1e"
).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry1 = Entry(tk_screen, bg="#333333", fg="#ffffff", insertbackground="#ffffff", width=10)
entry1.grid(row=1, column=1, padx=10, pady=5, sticky="w")

Label(
    tk_screen, text="Boolean Value 2 (0 or 1):", font=("Arial", 12), fg="#ffffff", bg="#1e1e1e"
).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry2 = Entry(tk_screen, bg="#333333", fg="#ffffff", insertbackground="#ffffff", width=10)
entry2.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Buttons
button_frame = Frame(tk_screen, bg="#1e1e1e")
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

# Function to handle combined operations
def calculate_operations():
    try:
        bool_val1 = int(entry1.get())
        bool_val2 = int(entry2.get())
        if bool_val1 not in [0, 1] or bool_val2 not in [0, 1]:
            raise ValueError("Inputs must be 0 or 1")
        calculate_button.config(state="disabled")
        # Perform Add Bool operation
        anything_about_boolean.add_bool(bool_val1, bool_val2)
        
        # Perform Multiply Bool operation
        anything_about_boolean.mul_bool(bool_val1, bool_val2)
        
        # Update the status label
        status_label.config(text="Calculation complete. Results displayed.")
    except ValueError as e:
        status_label.config(text=f"Error: {e}")

# Replace the "Add Bool" and "Multiply Bool" buttons with a single "Calculate" button
calculate_button = Button(
    tk_screen,
    text="Calculate",
    command=calculate_operations,
    bg="#00adb5",
    fg="#ffffff",
    font=("Arial", 12, "bold"),
    activebackground="#02848f",
    activeforeground="#ffffff",
    width=15,
    bd=0,
    relief="flat",
)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)


reset_button = Button(
    tk_screen,
    text="Reset",
    command=reset_screen,
    bg="#f44336",
    fg="#ffffff",
    font=("Arial", 12, "bold"),
    activebackground="#d32f2f",
    activeforeground="#ffffff",
    width=15,
    bd=0,
    relief="flat",
)
reset_button.grid(row=4, column=0, columnspan=2, pady=10)

# Status label
status_label = Label(tk_screen, text="", font=("Arial", 10), fg="#ff5722", bg="#1e1e1e")
status_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start Tkinter loop
tk_screen.mainloop()
t.done()

if __name__ == "__main__":
    screen()