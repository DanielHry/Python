# -*- coding: utf-8 -*-
"""
Created on Tue May 6 2020

@author: Daniel Hryniewski

Sorting - Implement two types of sorting algorithms: Merge sort and bubble sort.
"""
from random import randint



def randomlist():
    r = randint(5,30)
    randlist = []
    for i in range(1, r+1):
        n = randint(1,100)
        randlist.append(n)
    return randlist



def fusion(l1, l2):
    l0 = []
    while l1 != [] and l2 != []:
        
        if l1 != None and l2 != None:
            if l1[0] > l2[0]:
                l0.append(l2[0])
                l2.pop(0)
            else:
                l0.append(l1[0])
                l1.pop(0)
        elif l1 == None:
            l0.append(l2[0])
            l2.pop(0)
        elif l2 == None:
            l0.append(l1[0])
            l1.pop(0)
            
    if l1 != None:
        l0 = l0 + l1
    if l2 != None:
        l0 = l0 + l2

    return l0


def mergesort(l):

    n = len(l)
    if n <= 1:
        return l
    
    left = l[:(round(n/2))]
    right = l[(round(n/2)):]
    
    lsorted = mergesort(left)
    rsorted = mergesort(right)

    return fusion(lsorted, rsorted)



def bubblesort(l):
    s = True
    while s == True:
        s = False
        for i in range(0, len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                s = True
    return l
    



def main():
    mylist = randomlist()
    print('My random list:')
    print(mylist)
    print('\nBubble sort:')
    print(bubblesort(mylist))
    print('\nMerge sort:')
    print(mergesort(mylist))
    
    
    
if __name__ == '__main__':
    main()    