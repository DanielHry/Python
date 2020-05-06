# -*- coding: utf-8 -*-
"""
Created on Wed May 6 2020

@author: Daniel Hryniewski

Count Words in a String - Counts the number of individual words in a string.
For added complexity read these strings in from a text file and generate a summary.
"""



def main():
    
    f = open('MyFile.txt')
    
    
    words = []
    characters = []
    
    
    for i in f:
        for y in i:
            if y == ' ' or y == '\n':
                a = ''.join(characters)
                if a != '':
                    words.append(a)
                    characters.clear()
            else:
                characters.append(y)
    
    print('Your txt file have:',len(words), 'words')



main()