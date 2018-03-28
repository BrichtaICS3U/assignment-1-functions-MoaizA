# Assignment 1
# ICS3U
# <Moaiz Ahmad>
# March 28, 2018

###### uncomment this when you are ready to work on it
def CtoF (C):
    F=(1.8)*C+32
    return F

###### uncomment this when you are ready to work on it
def FtoC (F):
    C = (0.55556)*(F-32)
    return C

ans = True
while ans == True:
    print('Enter 1 for celsius to fahrenheit or 2 for fahrenheit to celsius and them enter your number')
    choice = int(input())
    temperature = int(input())
    if choice == 1:
        if temperature <= -273.15:
            print('please enter a value greater')
        else:
            temperature = CtoF(temperature)
            print(round(temperature))  
    elif choice == 2:
        if temperature <= -459.67:
            print('please enter a value greater')
        else:
            temperature = FtoC(temperature)
            print(round(temperature))
    elif choice != 1 or choice != 2:
        print('please enter 1 or 2')
    print('New Conversion? Y/N')
    answ = str(input())
    if answ == str('Y'):
        print('Ok')
    elif answ == str('N'):
        print('Well then')
        ans = False
    
