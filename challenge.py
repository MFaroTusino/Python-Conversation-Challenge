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

foodname = input ("What is your favourite food? ")
if foodname.lower() == "ramen":
    print("No way! My favourite food is Ramen too!")
else:
    print("Oh -", foodname,"! That's tasty. My favourite is Ramen")

print("Anyway, thanks for playing")

