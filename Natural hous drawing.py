from turtle import *
speed(20)

# all color variavall
S=("sky blue")
G=("Green")
Y=("yellow")
R=("red")
W=("white")
P=("pink")
B=("black")
BE=("blue")
BN=("brown")

# set up the screen
bgcolor(S)
penup()
goto(-650, -60)
pendown()
color(G)
begin_fill()
for i in range(4):
    if(i==1 or i==3):
        forward(260)
    else:
         forward(1300)
    right(90)
end_fill()

# Draw the sun
penup()
goto(-550, 150)
pendown()
color(Y)
begin_fill()
circle(50)
end_fill()

# Draw sun rays
pensize(4)
for i in range(12):
    penup()
    goto(-550,200)
    pendown()
    forward(70)
    backward(70)
    right(30)

# Draw the cloud
penup()
goto(-400,200)
pendown()
color(W)
begin_fill()
circle(30)
end_fill()

penup()
goto(-370,220)
pendown()
begin_fill()
circle(30)
end_fill()

penup()
goto(-340,200)
pendown()
begin_fill()
circle(30)
end_fill()

# Draw the house
pensize(1)
penup()
goto(-120,-60)
pendown()
color(B)
begin_fill()
for i in range(4):
    if (i==1 or i==3):
        forward(20)
    else:
        forward(440)
    left(90)
end_fill()

penup()
goto(-100, -40)
pendown()
color(B,BE)
begin_fill()
for i in range(4):
    if (i==1 or i==3):
        forward(200)
    else:
        forward(400)
    left(90)
end_fill()

penup()
goto(0,-40)
pendown()
left(90)
forward(200)

# Draw door
penup()
goto(175,-40)
pendown()
fillcolor(P)
begin_fill()
for i in range(4):
    if(i==1 or i==3):
        forward(50)
    else:
        forward(100)
    left(90)   
end_fill()

# windo
penup()
goto(90,20)
pendown()
fillcolor(P)
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

penup()
goto(260,20)
pendown()
fillcolor(P)
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

penup()
goto(-25,20)
pendown()
fillcolor(P)
begin_fill()
for i in range(4):
    forward(50)
    left(90)
end_fill()

# Draw the roof
penup()
goto(-100,160)
pendown()
right(90)
color(B,R)
begin_fill()
for i in range(4):
    if(i==1):
        left(120)
        forward(100)
    if(i==2):
        left(60)
        forward(300)
    if(i==3):
        left(60)
        forward(100)
    if(i==0):
        forward(400)
end_fill()
penup()
goto(0,160)
pendown()
right(120)
forward(100)

# Draw flag
penup()
goto(-130,160)
pendown()
left(60)
color(G)
begin_fill()
for i in range(4):
    if(i==1 or i==3):
        forward(140/2)
    else:
        forward(140)
    right(90)
end_fill()

penup()
goto(-200,215)
pendown()
color(R)
begin_fill()
circle(20)
end_fill()

penup()
goto(-130,230)
pendown()
pensize(10)
color(BN)
left(90)
forward(270)
color(B)
begin_fill()
pensize(1)
left(90)
for i in range(5):
    if(i==2):
        forward(40)
    else:
        forward(20)
    right(90)
end_fill()

# Draw the tree trunk
penup()
goto(400,-60)
pendown()
color(BN)
begin_fill()
for i in range(4):
    left(90)
    forward(50)
end_fill()
# Draw the tree leaves  
penup()
goto(350,-10)
pendown()
color(G)
begin_fill()
left(90)
for i in range(3):
    forward(150)
    left(120)
end_fill()
penup()
goto(360,40)
pendown()
begin_fill()
for i in range(3):
    forward(130)
    left(120)
end_fill()
penup()
goto(370,90)
pendown()
begin_fill()
for i in range(3):
    forward(110)
    left(120)
end_fill()

# Draw my Name
penup()
goto(-420,-40)
pendown()
color(B)
write("Made By The Name of Hacker (Matin Khan)","14pt bold")

#
hideturtle()


   