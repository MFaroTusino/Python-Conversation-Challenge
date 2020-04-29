print("Welcome! This is Brendan's test for conditional/boolean if-else statements and in the form of a guessing game")

Name = input("What is your name? ")
print("it's a pleasure to meet you,", Name)

keywordlist = ("yes", "okay", "sure")
question1 = input("Can I ask you a question? ")
input_words=question1.lower().split()
for word in input_words:
    if word in keywordlist:
        print("Fantastic!")
    else: 
        print("No problem - maybe next time")
        quit()

foodname = ("ramen")
foodname = input ("What is my favourite food? ")

if foodname.strip().lower() == ("ramen"):
    print("Yep! So Amazing! Great guess by the way")

else:
    print("Yuck, that's not it")

print("Anyway, thanks for playing")

