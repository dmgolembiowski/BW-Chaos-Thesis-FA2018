#!/usr/bin/env python3
import decimal
from decimal import getcontext
import sys
import numpy as np


"""
# Yes, that's really one million decimal places
getcontext().prec = 1000000
"""
"""
Actually, that was utterly unmanageable.
Let's go smaller.
"""
getcontext().prec = 100000
d = decimal.Decimal

class DataPoints:
    def __init__(self, X0, r, termCount):
        self.X0 = X0
        self.r = r
        self.termCount = termCount
        # self.limit = limit
        """self.Data = range... actually creates a list"""
        self.Data = [self.r, self.X0]

    def graphIt(self):
    # Yeah, not sure how to do this yet...
        pass

    def generateTerms(self):
        Output = self.X0
        for i in range(self.termCount):
            Output = Output*(self.r)*(1 - Output)
            self.Data.append([self.r, Output])
            print('self.Data = ',Output)
            print()

    def exportData(self):
        pass

print('The logistic chaos equation is Xn+1 = R*Xn*(1-Xn).')
print('The default decimal accuracy is set for one-hundred thousand decimal places.')
print('If you would like greater degrees of accuracy, you can increase the program\'s')
print('number of decimal places at the -getcontext().prec- statement.')

goAgain = True
testCaseCounter = 0

while goAgain == True:
    rValue = input('Enter the value of R:   ')
    rValue = float(rValue)
    xNaught = input('Enter the value of X0:   ')
    xNaught = float(xNaught)
    print('How many pseudoaccurate terms would you like to generate?')
    term_Count = input()
    term_Count = int(term_Count)

    # Create new instances of the DataPoints class
    # for retaining data to export and analyze
    testCase = DataPoints(xNaught, rValue, term_Count)
    DataPoints.generateTerms(testCase)
    testCaseCounter += 1

    wannaGoAgain = input('Wanna test another set?'  )
    if wannaGoAgain == 'n':
        sys.exit()
