print("welcome to my com quiz")

playing=input("do you want to play?" )
score=0
if playing !="yes":
    quit()
print("ok lets play ;")
answer = input("what does cu stands for")
if answer=="control unit":
    print("correct")
    score+=1
else:
    print("try again")

answer = input("what does www stands for")
if answer=="world wide web":
    print("correct")
    score +=1
else:
    print("try again")

answer = input("what does air stands for")
if answer=="all india radio":
    print("correct")
    score +=1
else:
    print("try again")
    print("you got" +str(score) + "questions correct!")
    print("you got" +str((score / 3)*100 )+ "%.")