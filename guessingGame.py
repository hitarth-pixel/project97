import random 
number=[1,2,3,4,5,6,7,8,9,10]
chances=5
print("guess the number from 1 to 10")

while(chances>0):
#while(chances>=1):
#while(chances<=5 && chance>0):
    numberType=int(input("enter your number "))
    randomChoice=random.choice(number)
    if(numberType<1):
        print("choose no. from 1-10")
        numberType=int(input("enter your number "))
    elif(numberType>10):
            print("choose no. from 1-10")
            numberType=int(input("enter your number "))
    else:
        if(randomChoice==numberType):
            print("you win")
            break
        
        elif(chances>0):
            #print("Oh the number is wrong try again")
            if(randomChoice<numberType):
                print("oh you choose bigger no. Try to choose smaller no.")
            else:
                print("oh you choose smaller no. Try to choose bigger no.")
            chances=chances-1
        else:
                print("you lose")
            

