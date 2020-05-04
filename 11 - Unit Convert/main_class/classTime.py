# -*- coding: utf-8 -*-

def choice():
    while True:
        try:
            c = int(input('>>> '))
            if 1 <= c <= 8: break
            else: print('Your choice must be between 1 and 8')
        except:
            print('Your choice must be between 1 and 8')
    return c


class Time():
    def __init__(self):
        pass
    
    def units(self, num):
        print('------------------------')
        print('Chose your Time unit:')
        print('1 - Year\t5 - Hour\n2 - Month\t6 - Minute\n3 - Week\t7 - Second\n4 - Day\t\t8 - Milisecond')
        
        c = choice()
        
        if c == 1:
            print(f'{num} year convert to: ')
            symbol1 = ' year'
        elif c == 2:
            print(f'{num} month convert to: ')
            symbol1 = ' month'
        elif c == 3:
            print(f'{num} week convert to: ')
            symbol1 = ' week'
        elif c == 4:
            print(f'{num} day convert to: ')
            symbol1 = ' day'
        elif c == 5:
            print(f'{num} hour convert to: ')
            symbol1 = ' hour'
        elif c == 6:
            print(f'{num} minute convert to: ')
            symbol1 = ' minute'
        elif c == 7:
            print(f'{num} second convert to: ')
            symbol1 = ' second'
        elif c == 8:
            print(f'{num} milisecond convert to: ')
            symbol1 = ' milisecond'


            
        convert = choice()
        
        if convert == 1:
            symbol2 = ' year'
        elif convert == 2:
            symbol2 = ' month'
        elif convert == 3:
            symbol2 = ' week'
        elif convert == 4:
            symbol2 = ' day'
        elif convert == 5:
            symbol2 = ' hour'
        elif convert == 6:
            symbol2 = ' minute'
        elif convert == 7:
            symbol2 = ' second'
        elif convert == 8:
            symbol2 = ' milisecond'
        
        return c, convert, symbol1, symbol2
    
    def calcul(self, num, unit1, unit2):
        
        if unit1 == 1:
            if unit2 == 1:
                result = num
            elif unit2 == 2:
                result = num * 12
            elif unit2 == 3:
                result = num * 52.1429
            elif unit2 == 4:
                result = num * 365
            elif unit2 == 5:
                result = num * 8760
            elif unit2 == 6:
                result = num * 525600
            elif unit2 == 7:
                result = num * 31540000
            elif unit2 == 8:
                result = num * 31540000000
                
        elif unit1 == 2:
            if unit2 == 1:
                result = num / 12
            elif unit2 == 2:
                result = num
            elif unit2 == 3:
                result = num * 4.345
            elif unit2 == 4:
                result = num * 30.4167
            elif unit2 == 5:
                result = num * 730
            elif unit2 == 6:
                result = num * 43800
            elif unit2 == 7:
                result = num * 2628000
            elif unit2 == 8:
                result = num * 2628000000
                
        elif unit1 == 3:
            if unit2 == 1:
                result = num / 52.143
            elif unit2 == 2:
                result = num / 4.345
            elif unit2 == 3:
                result = num
            elif unit2 == 4:
                result = num * 7
            elif unit2 == 5:
                result = num * 168
            elif unit2 == 6:
                result = num * 10080
            elif unit2 == 7:
                result = num * 604800
            elif unit2 == 8:
                result = num * 608400000
                
        elif unit1 == 4:
            if unit2 == 1:
                result = num / 365
            elif unit2 == 2:
                result = num / 30.417
            elif unit2 == 3:
                result = num / 7
            elif unit2 == 4:
                result = num
            elif unit2 == 5:
                result = num * 24
            elif unit2 == 6:
                result = num * 1440
            elif unit2 == 7:
                result = num * 86400
            elif unit2 == 8:
                result = num * 86400000
        
        elif unit1 == 5:
            if unit2 == 1:
                result = num / 8760
            elif unit2 == 2:
                result = num / 730
            elif unit2 == 3:
                result = num / 168
            elif unit2 == 4:
                result = num / 24
            elif unit2 == 5:
                result = num
            elif unit2 == 6:
                result = num * 60
            elif unit2 == 7:
                result = num * 3600
            elif unit2 == 8:
                result = num * 36000000
    
        elif unit1 == 6:
            if unit2 == 1:
                result = num / 525600
            elif unit2 == 2:
                result = num / 43800
            elif unit2 == 3:
                result = num / 10080
            elif unit2 == 4:
                result = num / 1440
            elif unit2 == 5:
                result = num / 60
            elif unit2 == 6:
                result = num
            elif unit2 == 7:
                result = num * 60
            elif unit2 == 8:
                result = num * 60000
                
        elif unit1 == 7:
            if unit2 == 1:
                result = num / 31540000
            elif unit2 == 2:
                result = num / 2628000
            elif unit2 == 3:
                result = num / 604800
            elif unit2 == 4:
                result = num / 86400
            elif unit2 == 5:
                result = num / 3600
            elif unit2 == 6:
                result = num / 60
            elif unit2 == 7:
                result = num
            elif unit2 == 8:
                result = num * 1000
                
        elif unit1 == 8:
            if unit2 == 1:
                result = num / 31540000000
            elif unit2 == 2:
                result = num / 2628000000
            elif unit2 == 3:
                result = num / 604800000
            elif unit2 == 4:
                result = num / 86400000
            elif unit2 == 5:
                result = num / 3600000
            elif unit2 == 6:
                result = num / 60000
            elif unit2 == 7:
                result = num / 1000
            elif unit2 == 8:
                result = num
                

        
        return result