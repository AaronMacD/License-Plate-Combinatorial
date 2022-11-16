# -*- coding: utf-8 -*-
"""
License Plate Counter
MTH 225
Aaron MacDougall
version 9/29/22
"""

def lettersPermutation(letters):
    #26 Letters in the Alphabet, used as our number of options.
    result = 0
    numLetters = len(letters)
    
    if numLetters == 1: # With 1 Letter, there are three different spots that letter can be.
        result = (1 * 26 * 26) + (26 * 1 * 26) + (26 * 26 * 1) #Written this way for clarity.
    if numLetters == 2: # With 2 letters, there are only two combinations
        result = (1 * 1 * 26) + (26 * 1 * 1)
    if numLetters == 3:#only one option
        result = 1 * 1 * 1
    
    return result
    

def numbersPermutation(numbers):
    #10 numbers to use, 0-9
    result = 0
    numNumbers = len(numbers)
    if numNumbers == 1:
        result = (1 * 10 * 10 * 10) + (10 * 1 * 10 * 10) + (10 * 10 * 1 * 10) + (10 * 10 * 10 * 1)
    if numNumbers == 2:
        result = (1 * 1 * 10 * 10) + (10 * 1 * 1 * 10) + (10 * 10 * 1 * 1)
    if numNumbers == 3:
        result = (1 * 1 * 1 * 10) + (10 * 1 * 1 * 1)
    if numNumbers == 4:
        result = (1 * 1 * 1 * 1)
    
    return result
    

def main():
    
    quit = False
    while quit == False:
        print("License Plates are typically formatted as LLL #### with L being a letter and # being a number.\n\nThis program will allow you to select letters and/or numbers for your license plate and give you the number of permutations containing those letters and/or numbers.\n")
        letters = input("Please enter a sequence of zero to three letters(LLL): ")
        numbers = input("Please enter a sequence of zero to four numbers (####): ")
        
        result = lettersPermutation(letters) * numbersPermutation(numbers)
        print("\n\nThe combination of letters and numbers you entered has " + str(result) + " total possible combination!\n")
        
        endResult = input("Do you wish to play again? (y/n)")
        if endResult == "n" or endResult == "N":
            quit = True
            
        
        
    
if __name__=='__main__':
    main()