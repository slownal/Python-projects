import random
maxrange=eval(input('Type a Number: '))
if maxrange.isdigit():
    maxrange=int(maxrange)

    if maxrange<=0:
        print('Please type a number larger than 0 next time. ')
        quit()
else:
    print('Please type a number next time.')
    quit()

rnum=random.randint(0, maxrange)
while True:
    userguess=input("Make a guess: ")
    if userguess.isdigit():
        userguess=int(userguess)
    else:
        print('Please type a number next time.')
        continue
   
    if userguess==rnum:
        print("You Got it! ")
    else:
        print("You got it wrong! ")