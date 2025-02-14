from turtle import *

total=360 
sides=4 
angle=total/sides 
pixel=200 
R=("red")
W=("white")
B=("black")
B2=("brown")
S=("skyblue")


speed(10)
Screen().bgcolor(S)
color(R)
fillcolor(R) 
begin_fill() 
for i in range(sides):
    print(i)
    if(i==1 or i==3):
        forward(pixel/4)
    else:
        forward(pixel)
    left(angle) 
end_fill()


penup() 
goto(0,50) 
pendown()
color(W)
fillcolor(W) 
begin_fill() 
for i in range(sides):
    print(i)
    if(i==1 or i==3):
        forward(pixel/4)
    else:
        forward(pixel)
    left(angle) 
end_fill()


penup() 
goto(0,100) 
pendown()
color(R)
fillcolor(R) 
begin_fill() 
for i in range(sides):
    print(i)
    if(i==1 or i==3):
        forward(pixel/4)
    else:
        forward(pixel)
    left(angle) 
end_fill()

color(B)
penup()
goto(0,150)
pendown()
pensize(10)
right(angle)
forward(pixel+100)


fillcolor(B)
begin_fill()
pixel2=50
left(angle)
for i in range(5):
    print(i)
    if(i==2):
        forward(pixel2)
    else:
        forward(pixel2/2)
    right(angle)
end_fill()

hideturtle()


