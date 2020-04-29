print("Welcome! This is Brendan's test for conditional/boolean if-else statements and in the form of a guessing game")

Name = input("What is your name? ")
print("it's a pleasure to meet you.", Name)

answer = input ("Can I ask you a question? ")

if answer.lower() == "yes" or "okay" or "sure":
    print("Fantastic, lets proceed")

else: 
    print("well that's really unfortunate")

if answer.lower() == "yes" or "okay" or "sure":
    foodname = ("ramen")
    foodname = input ("What is my favourite food? ")

if foodname == ("ramen"):
    print("Yep! So Amazing! Great guess by the way")

else:
    print("Yuck, that's not it")

print("Anyway, thanks for playing")

