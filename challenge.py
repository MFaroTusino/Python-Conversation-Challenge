import re
print("Welcome! This is Brendan's test for conditional/boolean if-else statements and in the form of a guessing game")

Name = input("What is your name? ")
print("it's a pleasure to meet you,", Name)

keywordFound = False
keywordlist = ("yes", "okay", "sure")
favouriteThings=[]
countOfFavourites=0
countOfSharedFavourites=0
question1 = input("Can I ask you a question? ")
question1 = question1.lower()
question1 = re.sub(r'[^\w\s]','',question1)
input_words=question1.split()
for word in input_words:
    if word in keywordlist:
        keywordFound = True
        print("Word: ",word)

if(keywordFound):
    print("YAY!")
else:
    print ("Okay - maybe next time")
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

question2 = input("Can I get to know you a little better? ")
question2 = question2.lower()
question2 = re.sub(r'[^\w\s]','',question2)
input_words=question2.split()
for word in input_words:
    if word in keywordlist:
        keywordFound = True
        print("Word: ",word)

if(keywordFound):
    print("YAY!")
else:
    print ("Okay - maybe next time")
    quit()
    
faveColour = input("What is your favourite colour? ")
if faveColour.lower().strip() == "purple":
    print("Okay, this is freaky! My favourite colour is Purple too")
    countOfSharedFavourites = countOfSharedFavourites + 1
    countOfFavourites = countOfFavourites + 1
else:
    print(faveColour,", hey. That's a nice colour. My choice is Purple")
favouriteThings.append(faveColour)
countOfFavourites = countOfFavourites + 1

if countOfSharedFavourites > 1:
    print("So it seems like now I know",countOfFavourites, "of your favourite things, and we have", countOfSharedFavourites, "favourite things in common!")
    print("That's so cool!")
else:
    print("So it seems like now I know",countOfFavourites, "of your favourite things")
#print("Your favourite colour is,", faveColour, "and your favourite food is,", favouriteFood)
print("Look at this, we're learning about each other so quickly")
