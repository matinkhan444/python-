from turtle import *

hideturtle()

pensize(5)

# Draw head

fillcolor('black')
begin_fill()
forward(120)
left(90)
forward(50)
left(90)
forward(120)
left(90)
forward(50)
end_fill()

# Draw eyes

penup()
goto(20,25)
pendown()
fillcolor('white')
begin_fill()
circle(10)
penup()
goto(80,25)
pendown()
circle(10)
end_fill()

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

fillcolor('yellow')
begin_fill()
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
end_fill()

# Draw right heand

fillcolor('black')
begin_fill()
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
left(90)
forward(20)
end_fill()

# Draw right heand circle/finger

penup()
goto(-80,-145)
pendown()
right(180)
circle(15)

# Draw left heand

penup()
goto(150,-30)
pendown()
fillcolor('black')
begin_fill()
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
end_fill()

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
fillcolor('black')
begin_fill()
forward(120)
left(90)
forward(60)
left(90)
forward(20)
left(90)
forward(30)
right(90)
forward(100)
end_fill()

# Draw left lag

fillcolor('black')
begin_fill()
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
end_fill()

# Draw left lag shoes

backward(100)
left(125)
fillcolor('brown')
begin_fill()
forward(35)
left(145)
forward(60)
left(90)
forward(20)
left(90)
forward(30)
end_fill()

# Draw right lag Shows

penup()
goto(-30,-240)
pendown()
fillcolor('brown')
begin_fill()
backward(60)
right(90)
forward(20)
left(90)
forward(30)
left(35)
forward(30)
end_fill()
