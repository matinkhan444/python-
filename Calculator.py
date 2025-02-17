from turtle import *

number=int(input('Enter Your number:'))
symbol=input('Enter Your symbol:')
number2=int(input('Enter Your number2:'))
person=[number,symbol,number2]
if (symbol=='+'):
    print('rusult:',number+number2)
elif(symbol=='-'):
    print('rusult:',number-number2)
elif(symbol=='*'):
    print('rusult:',number*number2)
elif(symbol=='/'):
    print('rusult:',number/number2)
else:
    print('Do not found result')


     
