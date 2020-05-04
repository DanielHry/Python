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


class Volume():
    def __init__(self):
        pass
    
    
    def units(self, num):
        print('------------------------')
        print('Chose your volume unit:')
        print('1 - Cubic Meter [m²]\t4 - Centilitre [cl]\n2 - Litre [l]\t\t5 - Mililitre [ml]\n3 - Decilitre [dl]')
        
        c = choice()
        
        if c == 1:
            print(f'{num}m² convert to: ')
            symbol1 = 'm²'
        elif c == 2:
            print(f'{num}l convert to: ')
            symbol1 = 'l'
        elif c == 3:
            print(f'{num}dl convert to: ')
            symbol1 = 'dl'
        elif c == 4:
            print(f'{num}cl convert to: ')
            symbol1 = 'cl'
        elif c == 5:
            print(f'{num}ml convert to: ')
            symbol1 = 'ml'
            
        convert = choice()
        
        if convert == 1:
            symbol2 = 'm²'
        elif convert == 2:
            symbol2 = 'l'
        elif convert == 3:
            symbol2 = 'dl'
        elif convert == 4:
            symbol2 = 'cl'
        elif convert == 5:
            symbol2 = 'ml'
        
        return c, convert, symbol1, symbol2
    
    
    
    def calcul(self, num, unit1, unit2):
        
        if unit1 == 1:
            if unit2 == 1:
                result = num
            elif unit2 == 2:
                result = num * 1000
            elif unit2 == 3:
                result = num * 10000
            elif unit2 == 4:
                result = num * 100000
            elif unit2 == 5:
                result = num * 1000000
                
        elif unit1 == 2:
            if unit2 == 1:
                result = num / 1000
            elif unit2 == 2:
                result = num
            elif unit2 == 3:
                result = num * 10
            elif unit2 == 4:
                result = num * 100
            elif unit2 == 5:
                result = num * 1000
                
        elif unit1 == 3:
            if unit2 == 1:
                result = num / 10000
            elif unit2 == 2:
                result = num / 10
            elif unit2 == 3:
                result = num
            elif unit2 == 4:
                result = num * 10
            elif unit2 == 5:
                result = num * 100
            
        elif unit1 == 4:
            if unit2 == 1:
                result = num / 100000
            elif unit2 == 2:
                result = num / 100
            elif unit2 == 3:
                result = num / 10
            elif unit2 == 4:
                result = num
            elif unit2 == 5:
                result = num * 10

        elif unit1 == 5:
            if unit2 == 1:
                result = num / 1000000
            elif unit2 == 2:
                result = num / 1000
            elif unit2 == 3:
                result = num / 100
            elif unit2 == 4:
                result = num / 10
            elif unit2 == 5:
                result = num
        
        
        return result
