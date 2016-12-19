# -*- coding: utf-8 -*-

import random

options = ['rock', 'paper', 'scissors']
user_pick = raw_input('Enter your input: ')


while True:
    if user_pick in options:    
        print "You picked %s!" % user_pick
        computer =random.choice(options)
        print "The computer picked %s!" % computer
        if user_pick == computer:
            print 'Tie! Try again!' 
            user_pick = raw_input('Enter your input: ')
            continue
        elif user_pick == 'rock':
            if computer == 'paper':
                print "You lose!"
                break
            if computer == 'scissors':
                print "You win!"
                break          
        elif user_pick == 'paper':
            if computer == 'rock':
                print 'You win!'
                break
            if computer == 'scissors':
                print 'You lose!'
                break
    else:
        print "Invalid input. Please try again. Available options are %s" % options
        user_pick = raw_input('Enter your input: ')
        continue

