from random import choice
import pygame
from pygame import mixer
# import necessary modules
options = ['Rock','Paper','Scissors']
hardbass = 'RHB'
mq = 'MarioQuack'
h = 'Hyper'
paper = 'Paper'
rock = 'Rock'
clas = 'Classical'
scissors = 'Scissors'
# defining variables
songchoice = input('What song would you like to listen to? RHB (Russian Hard Bass), MarioQuack, Classical or Hyper? (CaSe SeNsItIvE): ')
# asking for song choice
if hardbass in songchoice:
    mixer.init()
    mixer.music.load('rhb.mp3')
    mixer.music.play(-1)
    print('Jam\'s on! Have fun! :)')
if mq in songchoice:
    mixer.init()
    mixer.music.load('mq.mp3')
    mixer.music.play(-1)
    print('Jam\'s on! Have fun! :)')
if h in songchoice:
    mixer.init()
    mixer.music.load('hyp.mp3')
    mixer.music.play(-1)
    print('Jam\'s on! Have fun! :)')
if clas in songchoice:
    mixer.init()
    mixer.music.load('nut.mp3')
    mixer.music.play(-1)
    print('Jam\'s on! Have fun! :)')
# plays music according to songchoice
while True:
    to_guess = choice(options)
    # defines computer's guess
    player1 = input('Rock, Paper or Scissors? (CaSe SeNsItIvE!): ')
    # asks for input from player
    if player1 in to_guess:
        print('Oops! You and the computer picked the same! Try Again!')
    # if the program and player choose the same, restart game
    else:
        if paper in player1:
            if scissors in to_guess:
                print('*chop chop* The computer\'s scissors destroy your paper. You lost.\n Thanks for playing! :)')
            if rock in to_guess:
                print('You won! *Paper crumples on computer\'s rock*\n Thanks for playing! :)')
        if rock in player1:
            if paper in to_guess:
                print('*paper crumples on your rock* You lost. Sorry!\n Thanks for playing! :)')
            if scissors in to_guess:
                print('*clang* Your rock destroys the computer\'s scissors. You win!\n Thanks for playing! :)')
        if scissors in player1:
            if paper in to_guess:
                print('*chop, chop* You cut up the computer\'s paper. You win!\n Thanks for playing! :)')
            if rock in to_guess:
                print('*clanging* The computer\'s rock bends your scissors to hell and back. You lose.\n Thanks for playing! :)')
# responses based on input and computer's choice
