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


class Pressure():
    def __init__(self):
        pass
    
    
    def units(self, num):
        print('------------------------')
        print('Chose your pressure unit:')
        print('1 - Atmosphere [atm]\t4 - Psi [psi]\n2 - Bar [bar]\t\t5 - Torr [torr]\n3 - Pascal [Pa]')
        
        c = choice()
        
        if c == 1:
            print(f'{num} atm convert to: ')
            symbol1 = ' atm'
        elif c == 2:
            print(f'{num} bar convert to: ')
            symbol1 = ' bar'
        elif c == 3:
            print(f'{num} Pa convert to: ')
            symbol1 = ' Pa'
        elif c == 4:
            print(f'{num} psi convert to: ')
            symbol1 = ' psi'
        elif c == 5:
            print(f'{num}µg convert to: ')
            symbol1 = ' torr'
            
        convert = choice()
        
        if convert == 1:
            symbol2 = ' atm'
        elif convert == 2:
            symbol2 = ' bar'
        elif convert == 3:
            symbol2 = ' Pa'
        elif convert == 4:
            symbol2 = ' psi'
        elif convert == 5:
            symbol2 = ' torr'
        
        return c, convert, symbol1, symbol2
    
    
    
    def calcul(self, num, unit1, unit2):
        
        if unit1 == 1:
            if unit2 == 1:
                result = num
            elif unit2 == 2:
                result = num * 1.013
            elif unit2 == 3:
                result = num * 101325
            elif unit2 == 4:
                result = num * 14.696
            elif unit2 == 5:
                result = num * 760
                
        elif unit1 == 2:
            if unit2 == 1:
                result = num / 1.013
            elif unit2 == 2:
                result = num
            elif unit2 == 3:
                result = num * 100000
            elif unit2 == 4:
                result = num * 14.504
            elif unit2 == 5:
                result = num * 750
                
        elif unit1 == 3:
            if unit2 == 1:
                result = num / 101325
            elif unit2 == 2:
                result = num / 100000
            elif unit2 == 3:
                result = num
            elif unit2 == 4:
                result = num / 6895
            elif unit2 == 5:
                result = num / 133
            
        elif unit1 == 4:
            if unit2 == 1:
                result = num / 14.696
            elif unit2 == 2:
                result = num / 14.504
            elif unit2 == 3:
                result = num * 6895
            elif unit2 == 4:
                result = num
            elif unit2 == 5:
                result = num * 51.715

        elif unit1 == 5:
            if unit2 == 1:
                result = num / 760
            elif unit2 == 2:
                result = num / 750
            elif unit2 == 3:
                result = num * 133.322
            elif unit2 == 4:
                result = num / 51.715
            elif unit2 == 5:
                result = num
        
        
        return result
