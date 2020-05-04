# -*- coding: utf-8 -*-

def choice():
    while True:
        try:
            c = int(input('>>> '))
            if 1 <= c <= 5: break
            else: print('Your choice must be between 1 and 5')
        except:
            print('Your choice must be between 1 and 5')
    return c


class Mass():
    def __init__(self):
        pass
    
    
    def units(self, num):
        print('------------------------')
        print('Chose your mass unit:')
        print('1 - Tonne [t]\t\t4 - Miligram [mg]\n2 - Kilogram [kg]\t5 - Microgram [µg]\n3 - Gram [g]')
        
        c = choice()
        
        if c == 1:
            print(f'{num}t convert to: ')
            symbol1 = 't'
        elif c == 2:
            print(f'{num}kg convert to: ')
            symbol1 = 'kg'
        elif c == 3:
            print(f'{num}g convert to: ')
            symbol1 = 'g'
        elif c == 4:
            print(f'{num}mg convert to: ')
            symbol1 = 'mg'
        elif c == 5:
            print(f'{num}µg convert to: ')
            symbol1 = 'µg'
            
        convert = choice()
        
        if convert == 1:
            symbol2 = 't'
        elif convert == 2:
            symbol2 = 'kg'
        elif convert == 3:
            symbol2 = 'g'
        elif convert == 4:
            symbol2 = 'mg'
        elif convert == 5:
            symbol2 = 'µg'
        
        return c, convert, symbol1, symbol2
    
    
    
    def calcul(self, num, unit1, unit2):
        
        if unit1 == 1:
            if unit2 == 1:
                result = num
            elif unit2 == 2:
                result = num * 1000
            elif unit2 == 3:
                result = num * 1000000
            elif unit2 == 4:
                result = num * 1000000000
            elif unit2 == 5:
                result = num * 1000000000000
                
        elif unit1 == 2:
            if unit2 == 1:
                result = num / 1000
            elif unit2 == 2:
                result = num
            elif unit2 == 3:
                result = num * 1000
            elif unit2 == 4:
                result = num * 1000000
            elif unit2 == 5:
                result = num * 1000000000
                
        elif unit1 == 3:
            if unit2 == 1:
                result = num / 1000000
            elif unit2 == 2:
                result = num / 1000
            elif unit2 == 3:
                result = num
            elif unit2 == 4:
                result = num * 1000
            elif unit2 == 5:
                result = num * 1000000
            
        elif unit1 == 4:
            if unit2 == 1:
                result = num / 1000000000
            elif unit2 == 2:
                result = num / 1000000
            elif unit2 == 3:
                result = num / 1000
            elif unit2 == 4:
                result = num
            elif unit2 == 5:
                result = num * 1000

        elif unit1 == 5:
            if unit2 == 1:
                result = num / 1000000000000
            elif unit2 == 2:
                result = num / 1000000000
            elif unit2 == 3:
                result = num / 1000000
            elif unit2 == 4:
                result = num / 1000
            elif unit2 == 5:
                result = num
        
        
        return result