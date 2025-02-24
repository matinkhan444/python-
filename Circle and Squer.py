from turtle import *

print('1.circle')
print('2.squer')
drawing=int(input('What are you draw:'))

if(drawing==1):
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
    

elif(drawing==2):
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
    print("eorr")

