# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 2020

@author: Daniel Hryniewski
"""

def choice():
    i = 0
    while True:
        try:
            while i < 1:
                number = int(input('Enter a number to find its prime factors:  '))
                if number > 0:
                    i += 1
                else:
                    print("Enter a positive integer.")
        except:
            print("Enter a positive integer.")
        else:
            break
    return number

def primes(num):
    primes = [2]
    x = 3
    while x <= num:
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)   
    return primes

def mainone(choice_num):
    my_num = choice_num
    list_primes = [1]
    z = 1
    num = 5000

    while z < choice_num:
        
        for i in primes(num):
            if my_num%i == 0:
                while my_num%i == 0:
                    my_num = my_num/i
                    list_primes.append(i)
                z = 1
                for n in list_primes:
                    z = z*n
        num = num + 5000
    list_primes.pop(0)
    
    return list_primes
    
def main():
    f = choice()
    list_pri = mainone(f)
    list_str = [str(list_pri) for list_pri in list_pri]
    
    if len(list_str) > 0:
        print(f,'='," * ".join(list_str))
    else:
        print('The number', f, 'does not have any prime factors.')


if __name__ == '__main__':
    main()