# -*- coding: utf-8 -*-

def choice():
    while True:
        try:
            c = int(input('>>> '))
            if 1 <= c <= 9: break
            else: print('Your choice must be between 1 and 9')
        except:
            print('Your choice must be between 1 and 9')
    return c


class Length():
    def __init__(self):
        pass
    
    def units(self, num):
        print('------------------------')
        print('Chose your length unit:')
        print('1 - Kilometre [km]\t5 - Micrometre [µm]\t9 - Inch\n2 - Metre [m]\t\t6 - Mille\n3 - Centimetre [cm]\t7 - Yard\n4 - Millimetre [mm]\t8 - Foot')
        
        c = choice()
        
        if c == 1:
            print(f'{num}km convert to: ')
            symbol1 = 'km'
        elif c == 2:
            print(f'{num}m convert to: ')
            symbol1 = 'm'
        elif c == 3:
            print(f'{num}cm convert to: ')
            symbol1 = 'cm'
        elif c == 4:
            print(f'{num}mm convert to: ')
            symbol1 = 'mm'
        elif c == 5:
            print(f'{num}µm convert to: ')
            symbol1 = 'µm'
        elif c == 6:
            print(f'{num} mille convert to: ')
            symbol1 = ' mille'
        elif c == 7:
            print(f'{num} yard convert to: ')
            symbol1 = ' yard'
        elif c == 8:
            print(f'{num} foot convert to: ')
            symbol1 = ' foot'
        elif c == 9:
            print(f'{num} inch convert to: ')
            symbol1 = ' inch'

            
        convert = choice()
        
        if convert == 1:
            symbol2 = 'km'
        elif convert == 2:
            symbol2 = 'm'
        elif convert == 3:
            symbol2 = 'cm'
        elif convert == 4:
            symbol2 = 'mm'
        elif convert == 5:
            symbol2 = 'µm'
        elif convert == 6:
            symbol2 = ' mille'
        elif convert == 7:
            symbol2 = ' yard'
        elif convert == 8:
            symbol2 = ' foot'
        elif convert == 9:
            symbol2 = ' inch'
        
        return c, convert, symbol1, symbol2
    
    def calcul(self, num, unit1, unit2):
        
        if unit1 == 1:
            if unit2 == 1:
                result = num
            elif unit2 == 2:
                result = num * 1000
            elif unit2 == 3:
                result = num * 100000
            elif unit2 == 4:
                result = num * 1000000
            elif unit2 == 5:
                result = num * 1000000000
            elif unit2 == 6:
                result = num / 1.609
            elif unit2 == 7:
                result = num * 1094
            elif unit2 == 8:
                result = num * 3281
            elif unit2 == 9:
                result = num * 39370
                
        elif unit1 == 2:
            if unit2 == 1:
                result = num / 1000
            elif unit2 == 2:
                result = num
            elif unit2 == 3:
                result = num * 100
            elif unit2 == 4:
                result = num * 1000
            elif unit2 == 5:
                result = num * 1000000
            elif unit2 == 6:
                result = num / 1609
            elif unit2 == 7:
                result = num * 1.094
            elif unit2 == 8:
                result = num * 3.281
            elif unit2 == 9:
                result = num * 39.37
                
        elif unit1 == 3:
            if unit2 == 1:
                result = num / 100000
            elif unit2 == 2:
                result = num / 100
            elif unit2 == 3:
                result = num
            elif unit2 == 4:
                result = num * 10
            elif unit2 == 5:
                result = num * 10000
            elif unit2 == 6:
                result = num / 160934
            elif unit2 == 7:
                result = num / 91.44
            elif unit2 == 8:
                result = num / 30.48
            elif unit2 == 9:
                result = num / 2.54
                
        elif unit1 == 4:
            if unit2 == 1:
                result = num / 1000000
            elif unit2 == 2:
                result = num / 1000
            elif unit2 == 3:
                result = num / 10
            elif unit2 == 4:
                result = num
            elif unit2 == 5:
                result = num * 1000
            elif unit2 == 6:
                result = num / 1609340
            elif unit2 == 7:
                result = num / 914
            elif unit2 == 8:
                result = num / 305
            elif unit2 == 9:
                result = num / 25.4
        
        elif unit1 == 5:
            if unit2 == 1:
                result = num / 1000000000
            elif unit2 == 2:
                result = num / 1000000
            elif unit2 == 3:
                result = num / 10000
            elif unit2 == 4:
                result = num / 1000
            elif unit2 == 5:
                result = num
            elif unit2 == 6:
                result = num / 1609340000
            elif unit2 == 7:
                result = num / 914400
            elif unit2 == 8:
                result = num / 304800
            elif unit2 == 9:
                result = num / 25400
    
        elif unit1 == 6:
            if unit2 == 1:
                result = num * 1.609
            elif unit2 == 2:
                result = num * 1609
            elif unit2 == 3:
                result = num * 160934
            elif unit2 == 4:
                result = num * 1609340
            elif unit2 == 5:
                result = num * 1609340000
            elif unit2 == 6:
                result = num
            elif unit2 == 7:
                result = num * 1760
            elif unit2 == 8:
                result = num * 5280
            elif unit2 == 9:
                result = num * 63360
                
        elif unit1 == 7:
            if unit2 == 1:
                result = num / 1094
            elif unit2 == 2:
                result = num / 1.094
            elif unit2 == 3:
                result = num * 91.44
            elif unit2 == 4:
                result = num * 914
            elif unit2 == 5:
                result = num * 914400
            elif unit2 == 6:
                result = num / 1760
            elif unit2 == 7:
                result = num
            elif unit2 == 8:
                result = num * 3
            elif unit2 == 9:
                result = num * 36
                
        elif unit1 == 8:
            if unit2 == 1:
                result = num / 3281
            elif unit2 == 2:
                result = num / 3.281
            elif unit2 == 3:
                result = num * 30.48
            elif unit2 == 4:
                result = num * 305
            elif unit2 == 5:
                result = num * 304800
            elif unit2 == 6:
                result = num * 5280
            elif unit2 == 7:
                result = num / 3
            elif unit2 == 8:
                result = num
            elif unit2 == 9:
                result = num * 12
                
        elif unit1 == 9:
            if unit2 == 1:
                result = num / 39370
            elif unit2 == 2:
                result = num / 39.37
            elif unit2 == 3:
                result = num * 2.54
            elif unit2 == 4:
                result = num * 25.4
            elif unit2 == 5:
                result = num * 25400
            elif unit2 == 6:
                result = num / 63360
            elif unit2 == 7:
                result = num / 36
            elif unit2 == 8:
                result = num / 12
            elif unit2 == 9:
                result = num

        
        return result