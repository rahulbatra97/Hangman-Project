#imports
import random

#creating the random fruit generator
word_list = ["mangoes", "blueberries", "strawberries", "pineapples", "grapes"]
word = random.choice(word_list)
print(word)

#creating the guessing system
guess = input("Please guess a letter: ")
if len(guess) == 1:
    print("you have guessed letter '"+guess +"'")
else:
    print("Oops! That is not a valid input.")

