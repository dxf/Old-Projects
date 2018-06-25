#welcome message
import sys
import time

print('\n\t\t\t\t\t\t\t    Fruity Hangman!\n')
print('\n\t\t\t\t\t\t\tWill you guess the word?\n')
print('\n\tNOTE: If you\'ve guessed one letter, do NOT repeat the same letter, unless you actually think it\'s in the word.')
#words
words = ["grape","banana","orange","apple","grapefruit","pineapple","avocado","tomato","mango"]

import random
word = random.choice(words)
#turnwordintodashes
dashes = ''
lettercount = 0
remain = word
for letter in word:
    lettercount = lettercount + 1 
    dashes = dashes + "-"
print('Here\'s your word:',dashes)
#loopreallystartsxddd
lives = 10
while "-" in dashes and lives > 0:
    guess = input('\nTake a guess. What letter do you think will go into the word? ')
#check
    if guess in word:
            print('\nGG! That\'s one letter down. Try again!')
            lettercount = lettercount - 1
            print('\nYou have', lettercount, 'letters remaining.')
    if lettercount == 0:
        print('\n\t\t\t\tYou won! PogChamp! Quitting in 3 seconds.')
        time.sleep(3)
        sys.exit()
    if guess not in word:
        lives = lives - 1
        print('\nFeelsBadMan, you didn\'t get it right. Can I get a RIP in chat?', lives, 'lives remaining!')
    if lives == 0:
        print('\n\t\t\t\t\nSorry mate. You lost. Why not try again? Quitting in 3 seconds.')
        time.sleep(3)
        sys.exit()
    
