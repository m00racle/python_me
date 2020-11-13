# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:22:36 2020

@author: m00racle
"""
def fizzbuzz(fizz, buzz, topNumber):
    """
    this is function that process the fizz buzz play which print the whole number but on certain numbers will print fizz, buzz, or fizzbuzz

    Parameters
    ----------
    fizz : TYPE positive int
        DESCRIPTION. the fizz factor 
    buzz : TYPE positive int
        DESCRIPTION. 
    topNumber : TYPE positive int > 0
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # start the number from 1
    number = 1
    
    # while the number is less than topNumber + 1 loop it
    while number < topNumber + 1:
        # switch to cases for the number (python does not have this )
        # let's try another approach; prepare a varoable for a string and always reset it into '' for each loop
        result = ''
        
        # if number % fizz >0 and number % buzz > 0 then just increment the number as string onto reault
        if number%fizz > 0 and number%buzz > 0 :
            result += str(number)
        # else : 
        else:
            #if the number%fizz == 0 then result += 'fizz'
            if number%fizz == 0 :
                result += 'fizz'
            #if the number%buzz == 0 then result += 'buzz'
            if number%buzz == 0:
                result += 'buzz'
        # print the result
        print(result)
        # increment the number by one to loop to the topNumber
        number += 1
    #the end of the def fizzbuzz(fizz, buzz, topNumber)