import random

print("Welcome to to the Eight ball magic game, it is not a ripoff be sure of that")
Playerchoice = input("What is your name madam or sir: \n")
print(f"Hello {Playerchoice} , welcome to not a ripoff of 8 ball magic.")
Playerquestion = input("So, did you need a answer from my inllectual Eight ball in the virtual world of the computers. \n")
print(f"{Playerchoice} ask: {Playerquestion}")

random_number = random.randint(1, 12)
if(random_number == 1):
    print("yes-definetely.")
elif(random_number == 2):
    print("it is true that you will be able to make it there.")
elif(random_number == 3):
    print("there is no chance thats gonna happen,sorry.")
elif(random_number == 4):
    print("There is a high chance but if you follow a certain path")
elif(random_number == 5):
    print("My intelectual computer analysis tells me thats not going to happen")
elif(random_number == 6):
    print("Yes, that is going to happen in the near future")
elif(random_number == 7):
    print("im very doubtful that what you said to me is going to happen")
elif(random_number == 8):
    print("I actually don't know about that one")
else:
    print("There is a virus, hacking me (sarcasm)")