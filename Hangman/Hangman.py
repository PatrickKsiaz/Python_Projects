# Start
# Generate a random word
# Generate as many blanks as letters in word
# Ask the user to guess a letter
# Is the guessed letter in the word?

#Yes --> Replace the blank with the letter --> Are all the blansk filled? Yes

#No --> Lose a life --> Have they run out of lives? 

word_list = ["ardvark", "baboon", "camel"]

#ToDo-1 - Randomly choose a word form the word_list and assign it to a variable called chosen_word. Then print it.
import random
chosen_word = random.choice(word_list)
print(chosen_word)


#ToDo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercases.
guess = input("Guess a letter: ").lower()
print(guess)


#ToDo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right if it is", "Wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")








