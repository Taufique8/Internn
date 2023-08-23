print("welcom to my Quiz Game: ")
playing = input("Do you want to playing Game :) ")
if playing.lower() != 'yes':
    quit()
a = str("Okay!,Let`s play the game")
print(a)

print("************************")

score = 0
answer = input("""Who Developed Python Programming language:
a) Wick van rossum
b) Rasmus lerdorf
c) Guido van rossum
d) Niene stom
""")
if answer.lower() == 'c':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("************************")

answer = input("""Whic Type Of Programming does Python Support :
a) Object Oriented Programming 
b) Structured programming
c) Functional programming
d) All of the mentioned
""")
if answer.lower() == 'a':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("************************")

answer = input("""Which of the following is the correct extension of python file? 
a) .python
b) .pl
c) .py
d) .p
""")
if answer.lower() == 'c':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("************************")

answer = input("""Is python code compiled or interpreted? 
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted
""")
if answer.lower() == 'a':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("************************")

print("You got" +" " + str(score) +" " + "Questions Correct!")
result = ("You score 100 out of" +" " + str((score / 4)*100) +"%")
print(result)
if result =='100%':
    print("outstanding Performance")
elif result =='75%':
    print("Well done!")
elif result == '50%':
    print("Good, But Try Best!")

               

