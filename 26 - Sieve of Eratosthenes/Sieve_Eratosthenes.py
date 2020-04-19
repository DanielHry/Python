# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 2020

@author: Daniel Hryniewski
"""


num = int(input('number: '))

listprims = [2,3,5,7]

for i in range(2, num+1):
    if i % 2 == 0:
        pass
    elif i % 3 == 0:
        pass
    elif i % 5 == 0:
        pass
    elif i % 7 == 0:
        pass
    else:
        listprims.append(i)
        
print(len(listprims))