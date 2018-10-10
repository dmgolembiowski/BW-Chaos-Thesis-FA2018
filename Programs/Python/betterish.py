#!/usr/bin/env python3
"""
import decimal
from decimal import getcontext
import sys
import numpy as np
"""
import sys

"""
# Yes, that's really one million decimal places
getcontext().prec = 1000000
"""
"""
Actually, that was utterly unmanageable.
Let's go smaller.
"""
"""
getcontext().prec = 100000
d = decimal.Decimal
"""
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
        uniqueList = []
        Output = self.X0
        for i in range(self.termCount):
            Output = (self.r)*(1 - Output**2)
            self.Data.append([self.r, Output])
            if i in range(self.termCount - 31, self.termCount):
                print('term = ', i, '|', 'self.Data = ', Output)
                if i in [9976, 9984, 9992, 10000]:
                    print('')
                    if i == 9984:
                        print('_________________________')
                if round(Output,5) not in uniqueList:
                    uniqueList.append(round(Output,5))
        counter = len(uniqueList)
        print('unique list = ', sorted(uniqueList))
        print('counter = ', counter)
    
    def genLogTerms(self):
        UniqueList = []
        Output = self.X0
        for i in range(self.termCount):
            Output = (self.r)*Output*(1 - Output)
            self.Data.append([self.r, Output])
            if i in range(self.termCount - 31, self.termCount):
                print('term = ', i, '|', 'self.Data = ', Output)
                if i in [9976, 9984, 9992, 10000]:
                    print('')
                if i == 9984:
                    print('_________________________')
                if round(Output,5) not in UniqueList:
                    UniqueList.append(round(Output,5))
        counter = len(UniqueList)
        print('unique list = ', sorted(UniqueList))
        print('counter = ', counter)    

    def exportData(self):
        pass

print('The logistic chaos equation is Xn+1 = R*(1-Xn^2).')
print('The default decimal accuracy is set for one-hundred thousand decimal places.')
print('If you would like greater degrees of accuracy, you can increase the program\'s')
print('number of decimal places at the -getcontext().prec- statement.')

goAgain = True
tryHarder = False
testCaseCounter = 0

while goAgain == True:
    rValue = input('Enter the value of R:   ')
    rValue = float(rValue)
    """
    if rValue > 1.44:
        tryHarder = True
    while tryHarder == True:
        print("That's too big. Try something between 0 and 1.4399...")
        uI = input("Enter a defined value of r: ")
        rValue = float(uI)
        if rValue in range(float(0), 1.4399):
            tryHarder = False
    
    xNaught = input('Enter the value of X0:   ')
    xNaught = float(xNaught)
    print('How many pseudoaccurate terms would you like to generate?')
    term_Count = input()
    term_Count = int(term_Count)
    """
    # Create new instances of the DataPoints class
    # for retaining data to export and analyze
    #testCase = DataPoints(xNaught, rValue, term_Count)
    testCase = DataPoints(0.5, rValue, 10000)
    DataPoints.genLogTerms(testCase)
    #testCaseCounter += 1

    wannaGoAgain = input('Wanna test another set?'  )
    if wannaGoAgain == 'n':
        sys.exit()
