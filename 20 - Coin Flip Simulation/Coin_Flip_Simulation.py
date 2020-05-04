# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 2020

@author: Daniel Hryniewski

Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides.
The code should record the outcomes and count the number of tails and heads.
"""

import random


def choice():
    i = 0
    while True:
        try:
            while i < 1:
                number = int(input('Enter how many time do you want play: '))
                if number > 0:
                    i += 1
                else:
                    print("Enter a positive integer.")
        except:
            print("Enter a positive integer.")
        else:
            break
    return number



def flip(num):
    
    n = 0
    tails = 0
    heads = 0
    
    while n < num :
        
        f = random.random()
        
        if f < 0.5:
            tails += 1
        else :
            heads += 1
        n += 1
    
    return tails, heads



def main():
    result = flip(choice())
    print('tails:', result[0])
    print('heads:', result[1])
    


if __name__ == '__main__':
    main()