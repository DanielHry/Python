# -*- coding: utf-8 -*-
"""
Created on Sun May 4 2020

@author: Daniel Hryniewski

Unit Converter (temp, length, volume, mass and more) - Converts various units between one another.
The user enters the type of unit being entered, the type of unit they want to convert to and then the value.
The program will then make the conversion.
"""

from main_class.classLength import Length
from main_class.classTemperature import Temperature
from main_class.classMass import Mass
from main_class.classTime import Time
from main_class.classVolume import Volume
from main_class.classSpeed import Speed
from main_class.classPressure import Pressure
from main_class.classFrequency import Frequency


class_length = Length()
class_mass = Mass()
class_temperature = Temperature()
class_time = Time()
class_volume = Volume()
class_speed = Speed()
class_pressure = Pressure()
class_frequency = Frequency()


def numchoice():
    while True:
        try:
            numchoice = int(input('>>> '))
            if numchoice == int(numchoice): break
        except:
            print('ERROR')

    return numchoice



def convertchoice():
    print('Choose unit to converter:')
    print('1 - Length\t\t5 - Volume\n2 - Mass\t\t6 - Speed\n3 - Temperature\t\t7 - Pressure\n4 - Time\t\t8 - Frequency')
    UnitList = ['Length','Mass','Temperature','Time','Volume','Speed','Pressure','Frequency']
    
    while True:
        choice = input('>>> ')
        print('------------------------')
        try:
            intChoice = int(choice)
            if 1 <= intChoice <= 8:
                print(f'You choice: {UnitList[intChoice-1]}')
                break
            else:
                print('Your choice must be between 1 and 8')            
        except:
            print('Your choice must be between 1 and 8')
    return choice



def convertresult(class_choice):
    
    numtoconvert = numchoice()
    unit = class_choice.units(numtoconvert)
    print('------------------------')
    c = class_choice.calcul(numtoconvert, unit[0], unit[1])
    
    return str(numtoconvert) + unit[2] + ' = ' + str(c) + unit[3]



def classchoice(num):
    print('print your number: ')
    if num == '1':
        return convertresult(class_length)
    elif num == '2':
        return convertresult(class_mass)
    elif num == '3':
        return convertresult(class_temperature)
    elif num == '4':
        return convertresult(class_time)
    elif num == '5':
        return convertresult(class_volume)
    elif num == '6':
        return convertresult(class_speed)
    elif num == '7':
        return convertresult(class_pressure)
    elif num == '8':
        return convertresult(class_frequency)
    
    return result



def main():
    
    print(classchoice(convertchoice()))



if __name__ == '__main__':
    main()