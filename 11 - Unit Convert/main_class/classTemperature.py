# -*- coding: utf-8 -*-

def choice():
    while True:
        try:
            c = int(input('>>> '))
            if 1 <= c <= 3: break
            else: print('Your choice must be between 1 and 3')
        except:
            print('Your choice must be between 1 and 3')
    return c


class Temperature():
    def __init__(self):
        pass
    
    
    def units(self, num):
        print('------------------------')
        print('Chose your temperature unit:')
        print('1 - Celsius [°C]\n2 - Kelvin [K]\n3 - Fahrenheit [°F]')
        
        c = choice()
        
        if c == 1:
            print(f'{num}°C convert to: ')
            symbol1 = '°C'
        elif c == 2:
            print(f'{num}K convert to: ')
            symbol1 = 'K'
        elif c == 3:
            print(f'{num}°F convert to: ')
            symbol1 = '°F'
            
        convert = choice()
        
        if convert == 1:
            symbol2 = '°C'
        elif convert == 2:
            symbol2 = 'K'
        elif convert == 3:
            symbol2 = '°F'
        
        return c, convert, symbol1, symbol2
    
    
    
    def calcul(self, num, unit1, unit2):
        
        if unit1 == 1:
            if unit2 == 1:
                result = num
            elif unit2 == 2:
                result = num + 273.15
            elif unit2 == 3:
                result = (num * 9/5) + 32 
                
        elif unit1 == 2:
            if unit2 == 1:
                result = num - 273.15
            elif unit2 == 2:
                result = num
            elif unit2 == 3:
                result = (num - 173.15) * 9/5 + 32
                
        elif unit1 == 3:
            if unit2 == 1:
                result = (num - 32) * 5/9
            elif unit2 == 2:
                result = (num - 32) * 5/9 + 273.15
            elif unit2 == 3:
                result = num
        
        
        return result
        
