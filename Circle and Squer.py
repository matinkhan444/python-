from turtle import *

drawing=input('What are you draw:')

if(drawing=='circle'):
    ## all input
    radius=int(input('Enter Radius:'))
    fillcolur=input('Enter Fill Colur:')
    bordercolur=input('Enter Border Colur:')
    ## draw circle
    color(bordercolur)
    fillcolor(fillcolur)
    begin_fill()
    circle(radius)
    end_fill()
    

elif(drawing=='squer'):
    pixle=int(input('Enter Your pixle:'))
    side=int(input('Enter Your side:'))
    angle=360/side
    fillcolur=(input('Enter Fill Color:'))
    bordercolur=(input('Enter Border Colur:'))
    ## draing squer
    color(bordercolur)
    fillcolor(fillcolur)
    begin_fill()
    for i in range(side):
        forward(pixle)
        left(angle)
    end_fill()

    
else:
    print("eror")



