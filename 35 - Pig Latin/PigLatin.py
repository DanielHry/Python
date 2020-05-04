# -*- coding: utf-8 -*-
"""
Created on Fri May 1 2020

@author: Daniel Hryniewski

Pig Latin - Pig Latin is a game of alterations played on the English language game. Read Wikipedia for more information on rules.
"""

def piglatin(l):
    
    if l[0] == 'a' or l[0] == 'e' or l[0] == 'i' or l[0] == 'o' or l[0] == 'u' or l[0] == 'y':
        l = l + '-way'
    else:
        l = l[1:] + '-' + l[0] + 'ay'
    
    return l
        

def main():
    string = input('Enter your string: ')
    print(piglatin(string))
    
    
main()