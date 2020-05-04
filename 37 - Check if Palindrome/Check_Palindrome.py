# -*- coding: utf-8 -*-
"""
Created on Fri May  1 2020

@author: Daniel Hryniewski

Check if Palindrome - Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”
"""


def main():
    
    string = input('Enter your string: ')
    if string == string[::-1]:
        print('Yes, your string is Palindrome')
    else:
        print('No, your string is not Palindrome' )
    
main()