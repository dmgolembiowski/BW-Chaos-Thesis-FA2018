#!/usr/bin/env python3
import decimaldebian-c-1vcpu-2gb-nyc1-01 on pts/0 jobs:00 7 files 36K            Wed Sep 12 19:05from decimal import getcontext
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
		self.X0 = d(X0)
		self.r = d(r)
		self.termCount = termCount
		# self.limit = limit
		"""self.Data = range... actually creates a list"""
		self.Data = np.ndarray([int(1),self.X0], self.r) 

	def graphIt(self):
		# Yeah, not sure how to do this yet...
		pass

	def generateTerms(self):
		Output = self.X0
		for i in range(self.termCount):
			Output = Output*d(self.r)*(d(1) - Output)
			self.Data.append([i,str(Output)], self.r)
			print(self.Data)
			i += 1
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
	rValue = str(d(rValue))
	xNaught = input('Enter the value of X0:   ')
	xNaught = str(d(xNaught))
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
