import re

'''A class that consists of functions to validate data inserted into the system, e.g. if the name is meant to be entered    
    'hasLetters' function is going to be used to make sure that there are no numbers or others signs in it'''
class errorHandling:


    def onlyNumbers(self,input):
        '''Makes sure that the input only consists of numbers'''
        return bool(re.search(r'\d', input))    #returns bool e.g. if TRUE, only numbers

    def hasLetters(self, inputString):
        '''Makes sure that the input only consists of letters'''
        return bool(re.search(r"^[a-zA-Z]+$", inputString)) #returns bool, if TRUE, only letters

    def isDate(self, inputString):
        '''Makes sure that the input is in a correct DATE format'''
        return bool(re.search(r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$", inputString)) #returns bool, if TRUE, correct format

    def isPrice(self, inputString):
        '''Makes sure that the input is in a correct PRICE format'''
        return bool(re.search(r'\d+(?:[.]\d{2})?$', inputString))   #return bools, if TRUE, correct format



