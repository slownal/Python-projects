print("Welcome to my Quiz!")

playing=input("Do you want to play? ")

if playing.lower()!='yes':
    quit()

print("Okay! Lets play.")
score=0
answer = input('What does CPU stand for? ').lower()
if answer =="central processing unit":
    print('Correct!')
    score+=1
else : print("Incorrect!")

answer1 = input('What does GPU stand for? ').lower()
if answer1 =="graphic processing unit":
    print('Correct!')
    score+=1
else : print("Incorrect!")

answer2 = input('What does RAM stand for? ').lower()
if answer2 =="random access unit":
    print('Correct!')
    score+=1
else : print("Incorrect!")

answer3 = input('What does PSU stand for? ').lower()
if answer3 =="power supply":
    print('Correct!')
    score+=1
else : print("Incorrect!")

print("yout got" + str(score) + "questions correct!")
print("yout got" + str((score/4)*100) + " %.")


