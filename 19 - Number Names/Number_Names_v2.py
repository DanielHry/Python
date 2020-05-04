# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 2020

@author: Daniel Hryniewski

Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own,
but you should support inputs up to at 10^100.
"""


def choice():
    n = input('Enter a integers or floating-point number between -10^100 and 10^100:\n')
    return n

def units(n):
    #function that returns the name of number between 1 and 9
    if n == '0':
        return ''
    elif n == '1':
        return 'one'
    elif n == '2':
        return 'two'
    elif n == '3':
        return 'three'
    elif n == '4':
        return 'four'
    elif n == '5':
        return 'five'
    elif n == '6':
        return 'six'
    elif n == '7':
        return 'seven'
    elif n == '8':
        return 'eight'
    elif n == '9':
        return 'nine'
    

def join(n):
    if n == '0':
        return ''
    else:
        return '-'
    
def tens(n):
    #function that returns the name of number between 1 and 99
    if n == '10':
        return 'ten'
    elif n == '11':
        return 'eleven'
    elif n == '12':
        return 'twelve'
    elif n == '13':
        return 'thirteen'
    elif n == '14':
        return 'fourteen'
    elif n == '15':
        return 'fifteen'
    elif n == '16':
        return 'sixteen'
    elif n == '17':
        return 'seventeen'
    elif n == '18':
        return 'eighteen'
    elif n == '19':
        return 'nineteen'
    
    elif n[0] == '2':
        t = 'twenty' + join(n[1]) + units(n[1])
        return t
    elif n[0] == '3':
        t = 'thirty' + join(n[1]) + units(n[1])
        return t
    elif n[0] == '4':
        t = 'forty' + join(n[1]) + units(n[1])
        return t
    elif n[0] == '5':
        t = 'fifty' + join(n[1]) + units(n[1])
        return t
    elif n[0] == '6':
        t = 'sixty' + join(n[1]) + units(n[1])
        return t
    elif n[0] == '7':
        t = 'seventy' + join(n[1]) + units(n[1])
        return t
    elif n[0] == '8':
        t = 'eighty' + join(n[1]) + units(n[1])
        return t
    elif n[0] == '9':
        t = 'ninety' + join(n[1]) + units(n[1])
        return t
    
    else:
        return units(n[1])
    
    
def serach(n):
    #function that returns the name of number between 1 and 999
    if n[0] == '0':
        result = tens(n[1:])
    else:
        result = units(n[0]) + ' ' + largnumber(n) + ' ' + tens(n[1:])
    return result


def largnumber(n):
    #function that returns the name of a number
    m = len(n)
    if m == 3:
        return 'hundred'
    elif m == 6:
        return 'thousand'
    elif m == 9:
        return 'million'
    elif m == 12:
        return 'billion'
    elif m == 15:
        return 'trillion'
    elif m == 18:
        return 'quadrillion'
    elif m == 21:
        return 'quintillion'
    elif m == 24:
        return 'sextillion'
    elif m == 27:
        return 'septillion'
    elif m == 30:
        return 'octillion'
    elif m == 33:
        return 'nonillion'
    elif m == 36:
        return 'decillion'
    elif m == 39:
        return 'undecillion'
    elif m == 42:
        return 'duodecillion'
    elif m == 45:
        return 'tredecillion'
    elif m == 48:
        return 'quattuordecillion'
    elif m == 51:
        return 'quindecillion'
    elif m == 54:
        return 'sexdecillion'
    elif m == 57:
        return 'septendecillion'
    elif m == 60:
        return 'octodecillion'
    elif m == 63:
        return 'novemdecillion'
    elif m == 66:
        return 'vigintillion'
    elif m == 69:
        return 'unvigintillion'
    elif m == 72:
        return 'duovigintillion'
    elif m == 75:
        return 'trevigintillion'
    elif m == 78:
        return 'quattuorvigintillion'
    elif m == 81:
        return 'quinvigintillion'
    elif m == 84:
        return 'sexvigintillion'
    elif m == 87:
        return 'septenvigintillion'
    elif m == 90:
        return 'octovigintillion'
    elif m == 93:
        return 'novemvigintillion'
    elif m == 96:
        return 'trigintillion'
    elif m == 99:
        return 'untrigintillion'
    elif m == 102:
        return 'duotrigintillion'


def listtransform(num):
    #function that transforms a string into a list
    mylist = []
    for i in num:
        mylist.append(i)
    return mylist

def aroundnum(t):
    #function that adds '0' to get a list of 3 numbers
    t.reverse()
    if len(t) % 3 == 2:
        t.append('0')
    elif len(t) % 3 == 1:
        t.append('0')
        t.append('0')
    t.reverse()
    return t

def namednum(n):
    #function returns the full name of the number and searches by 3 numbers for the names of the numbers
    listnmed = []
    t = listtransform(n)
    aroundnum(t)
    
    while len(t) > 0:
        firsttree = t[:3]
        j = ''.join(firsttree)
        listnmed.append(serach(j))
        
        if len(t) == 3:
            pass
        else:
            if t[0] == '0' and t[1] == '0' and t[2] == '0':
                pass
            else:
                listnmed.append(' ')
                listnmed.append(largnumber(t))
                listnmed.append(' ')
        
        del t[0:3]
    
    return ''.join(listnmed)
        

def integer(n, p):
    #function that defines whether it is a positive or negative integer
    if p[0] != '-' and p[0] != '0':
        return namednum(n)
    elif p[0] == '-' and p[1] != '0':
        p.pop(0)
        m = ''.join(p)
        return 'minus ' + namednum(m)
    else:
        return 'zero'
     
def floatnum(p):
    #function that returns all the names of the numbers after the decimal point
    p1 = p
    x = ''
    y = []
    z = []
    while x != '.':
        x = p1.pop()
        y.append(x)
    y.pop()
    y.reverse()
    for i in y:
        z.append(units(i))
    z = ' '.join(z)
    return z


def main():
    
    n = choice()
    p = listtransform(n)

    if p.count('.') == 1:
        afterpoint = floatnum(p)
        n = ''.join(p)
        print(integer(n, p), 'point', afterpoint)
    else:
        print(integer(n, p))

if __name__ == '__main__':
    main()