# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 2020

@author: Daniel Hryniewski

Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""

def range_choise():
    i = 0
    while True:
        try:
            while i < 1:
                choise = int(input('Which Fibonacci number do you want: '))
                if choise > 0 and choise < 300:
                    i += 1
                elif choise >= 300 :
                    print("Enter a lower number.")
                else:
                    print("Enter a positive integer.")
        except:
            print("Enter a positive integer.")
        else:
            break
    return choise

def calcul(num):
    list_fibo = [1]
    f0 = 0
    f1 = 1
    for i in range(num-1):
        fn = f1 + f0
        f0 = f1
        f1 = fn
        list_fibo.append(fn)
    return list_fibo


def main():
    integer = calcul(range_choise())
    list_str = [str(integer) for integer in integer]
    print(", ".join(list_str))      
    

if __name__ == '__main__':
    main()