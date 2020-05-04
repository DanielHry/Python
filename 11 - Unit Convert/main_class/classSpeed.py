# -*- coding: utf-8 -*-

def choice():
    while True:
        try:
            c = int(input('>>> '))
            if 1 <= c <= 4: break
            else: print('Your choice must be between 1 and 4')
        except:
            print('Your choice must be between 1 and 4')
    return c


class Speed():
    def __init__(self):
        pass
    
    
    def units(self, num):
        print('------------------------')
        print('Chose your speed unit:')
        print('1 - Kilometre/hour [km/h]\t3 - Mille/hour [mille/h]\n2 - Metre/second [m/s]\t\t4 - Foot/second [foot/s]')
        
        c = choice()
        
        if c == 1:
            print(f'{num} km/h convert to: ')
            symbol1 = ' km/h'
        elif c == 2:
            print(f'{num} m/s convert to: ')
            symbol1 = ' m/s'
        elif c == 3:
            print(f'{num} mille/h convert to: ')
            symbol1 = ' mille/h'
        elif c == 4:
            print(f'{num} foot/s convert to: ')
            symbol1 = ' foot/s'
            
        convert = choice()
        
        if convert == 1:
            symbol2 = ' km/h'
        elif convert == 2:
            symbol2 = ' m/s'
        elif convert == 3:
            symbol2 = ' mille/h'
        elif convert == 4:
            symbol2 = ' foot/s'
        
        return c, convert, symbol1, symbol2
    
    
    
    def calcul(self, num, unit1, unit2):
        
        if unit1 == 1:
            if unit2 == 1:
                result = num
            elif unit2 == 2:
                result = num / 3.6
            elif unit2 == 3:
                result = num / 1.609
            elif unit2 == 4:
                result = num / 1.097
                
        elif unit1 == 2:
            if unit2 == 1:
                result = num * 3.6
            elif unit2 == 2:
                result = num
            elif unit2 == 3:
                result = num * 2.237
            elif unit2 == 4:
                result = num * 3.281
                
        elif unit1 == 3:
            if unit2 == 1:
                result = num * 1.609
            elif unit2 == 2:
                result = num / 2.237
            elif unit2 == 3:
                result = num
            elif unit2 == 4:
                result = num * 1.467
            
        elif unit1 == 4:
            if unit2 == 1:
                result = num * 1.097
            elif unit2 == 2:
                result = num / 3.281
            elif unit2 == 3:
                result = num / 1.467
            elif unit2 == 4:
                result = num
        
        
        return result