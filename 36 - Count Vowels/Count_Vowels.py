# -*- coding: utf-8 -*-
"""
Created on Fri May 1 2020

@author: Daniel Hryniewski

Count Vowels - Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""

def countvowels(string):
    
    count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}
    
    for i in string:
        if i == 'a':
            count['a'] += 1
        elif i == 'e':
            count['e'] += 1
        elif i == 'i':
            count['i'] += 1
        elif i == 'o':
            count['o'] += 1
        elif i == 'u':
            count['u'] += 1
        elif i == 'y':
            count['y'] += 1
            
    return count
            
def printscore(count):
    sumvowels = 0
    for i in count:
        sumvowels = sumvowels + count[i]
        print(i + ' =', count[i])
        
    print(f'number of vowels: {sumvowels}')


def main():
    
    string = input('Enter your string: ')
    printscore(countvowels(string.lower()))
    
main()