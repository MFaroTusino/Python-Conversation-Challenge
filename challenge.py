print("Welcome! This is Brendan's test for conditional/boolean if-else statements and in the form of a guessing game")

Name = input("What is your name? ")
print("it's a pleasure to meet you,", Name)

keywordlist = ("yes", "okay", "sure")
favouriteThings=[]
countOfFavourites=0
countOfSharedFavourites=0
question1 = input("Can I ask you a question? ")
input_words=question1.lower().split()
for word in input_words:
    if word in keywordlist:
        print("Fantastic!")
    else: 
        print("No problem - maybe next time")
        quit()

favouriteFood = input ("What is your favourite food? ")
if favouriteFood.lower() == "ramen":
    print("No way! My favourite food is Ramen too!")
    favouriteThings.append(favouriteFood)
    countOfSharedFavourites = countOfSharedFavourites +1
    countOfFavourites = countOfFavourites + 1
else:
    print("Oh -", favouriteFood,"! That's tasty. My favourite is Ramen")
    favouriteThings.append(countOfFavourites)
    countOfFavourites = countOfFavourites + 1

question2 = input("Can I get to know you you a little better? ")
input_words=question2.lower().split()
for word in input_words:
    if word in keywordlist:
        print("YAY!")
    else: 
        print("That's okay. Thanks for talking to me")
        quit()

faveColour = input("What is your favourite colour?")
if faveColour.lower().strip() == "purple":
    print("Okay, this is freaky! My favourite colour is Purple too")
    countOfSharedFavourites = countOfSharedFavourites + 1
    countOfFavourites = countOfFavourites + 1
else:
    print(faveColour,", hey. That's a nice colour. My choice is Purple")
favouriteThings.append(faveColour)
countOfFavourites = countOfFavourites + 1

print("So it seems like now I know",countOfFavourites, "of your favourite things, and we have", countOfSharedFavourites, "favourite things in common!")
print("That's so cool!")
#print("Your favourite colour is,", faveColour, "and your favourite food is,", favouriteFood)
print("Look at this, we're learning about each other so quickly")
