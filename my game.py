import random

tries = 0

print ("Welcome to the word game!")
print ("\nI'm going to think of a word and you have to guess it!")
print ("\nGuess which letters are in the word, then you have to guess the whole thing!")
print ("\nGood luck!")

WORDS = ('/Users/Engr. OYEJOBI/Documents/Python Scripts/words.txt')

word = random.choice(WORDS)

correct = word
length = len(word)
length = str(length)

guess = input("The word is " + length + " letters long. Guess a letter!: ")

while tries < 5:
    for guess in word:
        if guess not in word:
            print ("Sorry, try again.")
        else:
            print ("Good job! Guess another!")

    if tries == 5:
        final = input ("Try to guess the word!: ")

        if final == correct:
            print ("Amazing! My word was ", word, "!")

        else:
            print ("Sorry. My word was ", word, ". Better luck next time!")

input("\n\nPress enter to exit")
            
