from turtle import *

speed(30)

# We want to paint a House.

width(7)
color("purple")

# Step 1: draw a square.

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# The end of making a square.

# Now we need to draw a door.

forward(70)
color("yellow")
left(90)
forward(120)  # The height of the door.
right(90)
forward(60)
right(90)
forward(120)

# Now we need a roof for the House.

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# Now lets add windows

color("brown")
penup()
goto(0,120)
begin_fill()
right(240)
forward(10)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

penup()
goto(190,120)
pendown()
begin_fill()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()

exitonclick()

# This is a comment!