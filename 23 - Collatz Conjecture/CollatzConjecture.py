# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 2020

@author: Daniel Hryniewski

Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""

def choice():
    i = 0
    while True:
        try:
            while i < 1:
                number = int(input('Enter a number: '))
                if number > 0:
                    i += 1
                else:
                    print("Enter a positive integer.")
        except:
            print("Enter a positive integer.")
        else:
            break
    return number


def calcul(n):
    
    listCollatz = []
    listCollatz.append(n)
    
    while n > 1:
        
        if n == 1:
            break
        elif n % 2 == 0:
            n = n / 2
            listCollatz.append(round(n))
        else :
            n = n * 3 + 1
            listCollatz.append(round(n))
            
    return listCollatz


def main():
    n = choice()
    result = calcul(n)
    list_str = [str(result) for result in result]
    print(f"Starting with {n}, one gets the sequence:", ", ".join(list_str))
    print("Number of steps: ", len(list_str) - 1)


if __name__ == '__main__':
    main()