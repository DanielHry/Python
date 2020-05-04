# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 2020

@author: Daniel Hryniewski

Number Names - Show how to spell out a number in English. You can use a preexisting implementation or roll your own,
but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type,
if that's less). Optional: Support for inputs other than positive integers (like zero, negative integers, and floating-point numbers).
"""
def choice():
    n = input('Enter a integers or floating-point number between -10 000 000 and 10 000 000:\n')
    return n

def units(n):
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
    

def aroundtwenty(n):    
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

    
def tens(n):
    if n == '2':
        return 'twenty'
    elif n == '3':
        return 'thirty'
    elif n == '4':
        return 'forty'
    elif n == '5':
        return 'fifty'
    elif n == '6':
        return 'sixty'
    elif n == '7':
        return 'seventy'
    elif n == '8':
        return 'eighty'
    elif n == '9':
        return 'ninety'
    

def listtransform(num):
    mylist = []
    for i in num:
        mylist.append(i)
    return mylist


def length1(n):
    return units(n)


def length2(n):
    u = int(n)
    t = listtransform(n)
    if t[0] == '0':
        return length1(t[1])
    else:
        if u < 20:
            return aroundtwenty(n)
        elif t[1] == '0':
            return tens(t[0])
        else:
            result = tens(t[0]) + '-' + length1(t[1])
            return result
        
    
def length3(n):
    u = int(n)
    t = listtransform(n)
    if t[0] == '0':
        return length2(''.join(t[1:]))
    else:
        if u == 100:
            return 'hundred'
        else:
            result = length1(t[0]) + ' hundred ' + length2(''.join(t[1:]))
            return result
        
def length4(n):
    u = int(n)
    t = listtransform(n)
    if t[0] == '0':
        return length3(''.join(t[1:]))
    else:
        if u == 1000:
            return 'thousand'
        else:
            result = length1(t[0]) + ' thousand ' + length3(''.join(t[1:]))
            return result

def length5(n):
    u = int(n)
    t = listtransform(n)
    if t[0] == '0':
        return length4(''.join(t[1:]))
    else:
        if u == 10000:
            return 'ten thousand'
        else:
            result = length2(''.join(t[:2])) + ' thousand ' + length3(''.join(t[2:]))
            return result
        
def length6(n):
    u = int(n)
    t = listtransform(n)
    if t[0] == '0':
        return length5(''.join(t[1:]))
    else:
        if u == 100000:
            return 'hundred thousand'
        else:
            result = length3(''.join(t[:3])) + ' thousand ' + length3(''.join(t[3:]))
            return result

def length7(n):
    u = int(n)
    t = listtransform(n)
    if t[0] == '0':
        return length5(''.join(t[1:]))
    else:
        if u == 1000000:
            return 'million'
        else:
            result = length1(t[0]) + ' million ' + length3(''.join(t[1:4])) + ' thousand ' + length3(''.join(t[4:]))
            return result

def findlength(n):
    if len(n) == 1:
        return length1(n)
    elif len(n) == 2:
        return length2(n)
    elif len(n) == 3:
        return length3(n)
    elif len(n) == 4:
        return length4(n)
    elif len(n) == 5:
        return length5(n)
    elif len(n) == 6:
        return length6(n)
    elif len(n) == 7:
        return length7(n)
    elif len(n) == 8:
        return 'ten million'
    else:
        return 'your number is not between -10 000 000 and 10 000 000'

def integer(n, p):
    if p[0] != '-' and p[0] != '0':
        return findlength(n)
    elif p[0] == '-' and p[1] != '0':
        p.pop(0)
        m = ''.join(p)
        return 'minus ' + findlength(m)
    else:
        return 'zero'
     
def floatnum(p):
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
        z.append(length1(i))
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