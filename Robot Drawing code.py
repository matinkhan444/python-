from turtle import *

hideturtle()
speed(100)
pensize(5)

# Draw head

forward(120)
left(90)
forward(50)
left(90)
forward(120)
left(90)
forward(50)

# Draw eyes

penup()
goto(20,25)
pendown()
circle(10)
penup()
goto(80,25)
pendown()
circle(10)

# Draw neck or throat

penup()
goto(50,0)
pendown()
forward(30)
left(90)
forward(20)
left(90)
forward(30)

# Draw body

penup()
goto(60,-30)
pendown()
right(90)
forward(90)
right(90)
forward(90)
right(90)
forward(180)
right(90)
forward(90)
right(90)
forward(90)

# Draw right heand

right(180)
forward(140)
left(90)
forward(100)
left(90)
forward(30)
left(90)
forward(80)
right(90)
forward(20)

# Draw right heand circle/finger

penup()
goto(-80,-145)
pendown()
right(90)
circle(15)

# Draw left heand

penup()
goto(150,-30)
pendown()
left(90)
forward(50)
right(90)
forward(100)
right(90)
forward(30)
right(90)
forward(80)
left(90)
forward(20)

# Draw left heand circle/finger

penup()
goto(170,-145)
pendown()
left(90)
circle(15)

# Draw right lag

penup()
goto(-30,-120)
pendown()
forward(120)
left(90)
forward(60)
left(90)
forward(20)
left(90)
forward(30)
right(90)
forward(100)

# Draw left lag

right(90)
forward(120)
right(90)
forward(120)
left(90)
forward(60)
left(90)
forward(20)
left(90)
forward(30)
right(90)
forward(100)

# Draw left lag shoes

backward(100)
left(125)
forward(30)

# Draw right lag Shows

penup()
goto(-30,-240)
pendown()
backward(33)
