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


class Frequency():
    def __init__(self):
        pass
    
    
    def units(self, num):
        print('------------------------')
        print('Chose your frequency unit:')
        print('1 - Hertz [Hz]\t\t3 - Megahertz [MHz]\n2 - Kilohertz [KHz]\t4 - Gigahertz [GHz]')
        
        c = choice()
        
        if c == 1:
            print(f'{num} Hz convert to: ')
            symbol1 = ' Hz'
        elif c == 2:
            print(f'{num} KHz convert to: ')
            symbol1 = ' KHz'
        elif c == 3:
            print(f'{num} MHz convert to: ')
            symbol1 = ' MHz'
        elif c == 4:
            print(f'{num} GHz convert to: ')
            symbol1 = ' GHz'
            
        convert = choice()
        
        if convert == 1:
            symbol2 = ' Hz'
        elif convert == 2:
            symbol2 = ' KHz'
        elif convert == 3:
            symbol2 = ' MHz'
        elif convert == 4:
            symbol2 = ' GHz'
        
        return c, convert, symbol1, symbol2
    
    
    
    def calcul(self, num, unit1, unit2):
        
        if unit1 == 1:
            if unit2 == 1:
                result = num
            elif unit2 == 2:
                result = num / 1000
            elif unit2 == 3:
                result = num / 1000000
            elif unit2 == 4:
                result = num / 1000000000
                
        elif unit1 == 2:
            if unit2 == 1:
                result = num * 1000
            elif unit2 == 2:
                result = num
            elif unit2 == 3:
                result = num / 1000
            elif unit2 == 4:
                result = num / 1000000
                
        elif unit1 == 3:
            if unit2 == 1:
                result = num * 1000000
            elif unit2 == 2:
                result = num * 1000
            elif unit2 == 3:
                result = num
            elif unit2 == 4:
                result = num / 1000
            
        elif unit1 == 4:
            if unit2 == 1:
                result = num * 1000000000
            elif unit2 == 2:
                result = num * 1000000
            elif unit2 == 3:
                result = num * 1000
            elif unit2 == 4:
                result = num
        
        
        return result