import turtle

# Click Counter Function

def clicked (x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}" , align="center" , font=("Courier New" , 32, "normal"))
                                                           
# Set Up Turtle Screen

wn = turtle.Screen()
wn.title("Click Counter")
wn.bgcolor("black")

# Register the Shape (attach custom image location directory)

wn.register_shape("xxx/bark.gif")

# Create Dog Turtle (attach custom image location directory)

dog = turtle.Turtle()
dog.shape("xxx/bark.gif")
dog.speed(0)

# Initialize the Click Counter

clicks = 0

# Create Pen for Displaying the Click Counter

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, -200)
pen.write(f"Clicks: {clicks}" , align="center" , font=("Courier New" , 32, "normal"))

# Set Up the click Event Handler

dog.onclick(clicked)

# Start the Turtle Main Loop

wn.mainloop()
