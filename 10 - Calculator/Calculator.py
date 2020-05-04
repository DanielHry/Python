# -*- coding: utf-8 -*-
"""
Created on Fri May 2 2020

@author: Daniel Hryniewski

Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
"""
    


def listtransform(num):
    #function that transforms a string into a list
    mylist = []
    for i in num:
        mylist.append(i)
    return mylist



def isolation(equation):
    #function that separates numbers and symbols
    equation = equation + '+'
    lequation = listtransform(equation)
    listsymbol = []
    numlist = []
    count = 0
    mynum = ''
    
    for i in lequation:
        if i == '+' or i == '-' or i == '*' or i == '/':
            numlist.append(int(mynum))
            listsymbol.append(i)
            count += 1
            mynum = ''
        else:
            mynum = mynum + equation[count]
            count += 1
            
    listsymbol.pop()
    return listsymbol, numlist
    


def calcul(listsymbol, numlist):
    #function that does the calculation
    while '*' in listsymbol or '/' in listsymbol:
        num1 = 0
        if '*' in listsymbol and '/' in listsymbol:
            
            if listsymbol.index('*') < listsymbol.index('/'):
                num1 = numlist[listsymbol.index('*')] * numlist[listsymbol.index('*') + 1]
                numlist[listsymbol.index('*')] = num1
                numlist.pop(listsymbol.index('*') + 1)
                listsymbol.pop(listsymbol.index('*'))
                
            elif listsymbol.index('/') < listsymbol.index('*'):
                num1 = numlist[listsymbol.index('/')] / numlist[listsymbol.index('/') + 1]
                numlist[listsymbol.index('/')] = num1
                numlist.pop(listsymbol.index('/') + 1)
                listsymbol.pop(listsymbol.index('/'))
                
        elif '*' in listsymbol or '/' in listsymbol:
            
            if '*' in listsymbol:
                num1 = numlist[listsymbol.index('*')] * numlist[listsymbol.index('*') + 1]
                numlist[listsymbol.index('*')] = num1
                numlist.pop(listsymbol.index('*') + 1)
                listsymbol.pop(listsymbol.index('*'))
                
            elif '/' in listsymbol:
                num1 = numlist[listsymbol.index('/')] / numlist[listsymbol.index('/') + 1]
                numlist[listsymbol.index('/')] = num1
                numlist.pop(listsymbol.index('/') + 1)
                listsymbol.pop(listsymbol.index('/'))
        
        else:
            break
    
    while '+' in listsymbol or '-' in listsymbol:
        
        if '+' in listsymbol and '-' in listsymbol:
            
            if listsymbol.index('+') < listsymbol.index('-'):
                num1 = numlist[listsymbol.index('+')] + numlist[listsymbol.index('+') + 1]
                numlist[listsymbol.index('+')] = num1
                numlist.pop(listsymbol.index('+') + 1)
                listsymbol.pop(listsymbol.index('+'))
                
            elif listsymbol.index('-') < listsymbol.index('+'):
                num1 = numlist[listsymbol.index('-')] - numlist[listsymbol.index('-') + 1]
                numlist[listsymbol.index('-')] = num1
                numlist.pop(listsymbol.index('-') + 1)
                listsymbol.pop(listsymbol.index('-'))
                
        elif '+' in listsymbol or '-' in listsymbol:
            
            if '+' in listsymbol:
                num1 = numlist[listsymbol.index('+')] + numlist[listsymbol.index('+') + 1]
                numlist[listsymbol.index('+')] = num1
                numlist.pop(listsymbol.index('+') + 1)
                listsymbol.pop(listsymbol.index('+'))
                
            elif '-' in listsymbol:
                num1 = numlist[listsymbol.index('-')] - numlist[listsymbol.index('-') + 1]
                numlist[listsymbol.index('-')] = num1
                numlist.pop(listsymbol.index('-') + 1)
                listsymbol.pop(listsymbol.index('-'))
                
        else:
            break    
    
    return numlist[0]



def main():
    print('You can use:\n+ : Add \n- : Sub \n* : Multyply \n/ : Divide \nq : Quit')
    print('For exmple print 3+5*4-20/5')
    
    while True:
        equation = input('Print your calcul: ')
        
        if equation == 'q':
            break
        else:
            try:
                result = isolation(equation)
                print(calcul(result[0], result[1]))
            except:
                print('ERROR')
    
if __name__ == '__main__':
    main()