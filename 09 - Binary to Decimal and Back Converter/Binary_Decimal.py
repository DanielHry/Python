# -*- coding: utf-8 -*-
"""
Created on Tue May 5 2020

@author: Daniel Hryniewski

Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
"""

def bintodec(num):
    result = bin(num)
    return result[2:]

def dectobin(num):
    result = int(str(num), 2)
    return result

def choice():
    while True:
        try:
            a = int(input('>>> '))
            if a == int(a): break
        except:
            print('ERROR - print a numbers') 
    return a

def convert():
    print('1 - Convert Binary to Decimal\n2 - Convert Decimal to Binary')
    
    while True:
        c = choice()
        if c == 1 or c == 2: break
        else: print('ERROR - Choice 1 or 2')
    
    print('Print your number:')
    
    while True:
        num = choice()
        if c == 1:
            result = bintodec(num)
            break
        else:
            try:
                result = dectobin(num)
                break
            except:
                print('ERROR - Your number is not binary!')
    
    print(result)
    
convert()