#milestone_3

#imports
import random
import re

#creating the logic of hangman
#creating the random fruit generator
word_list = ["mango", "blueberry", "strawberry", "pineapple", "grape", "raspberry","bananna", "melon", "watermelon", "apple", "pear", "peach"]
word = random.choice(word_list)
print(word)


while len(word)>0:
    
    

    guess = input("We're playing Hangman. I'm thinking of a fruit, please guess a letter: ")
    if len(guess) == 1 and guess.isalpha() == True:
        print("you have guessed letter '"+guess +"'")
        if guess in word:
            print("nice, that letter is in the word")
            word=re.sub(str(guess),"",word)
        else:
            print("swing and a miss, try again my friend")
    else:
        print("Oops! That is not a valid input.")

print("Well done! you've guessed all the correct letters in my word. Maybe you should try the lottery next.")
