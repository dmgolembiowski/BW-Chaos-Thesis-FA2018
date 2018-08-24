import math

class LogisticChaos:

    def __init__(self, xZero, rValue):
        self.xZero = xZero
        self.rValue = rValue

    def calcTerms(self):
        userInput = input('Enter the number of terms you want to generate: ')
        numTerms = int(userInput)

        sum = 0.00
        n = 0
        for n in range(0, numTerms):
            print("(", self.xZero, ",", self.xZero*self.rValue*(1.0 - self.xZero),",", sum,")")
            self.xZero = self.xZero*self.rValue*(1.0 - self.xZero)
            sum += self.xZero
            n += 1
        return

goAgain = True

while goAgain == True:
    print('For the discrete chaos equation, Xn+1 = r*Xn(1-Xn), please provide values for the following:')
    userInput = input('The initial X value, X0: ')
    xNaught = float(userInput)
    userInput = input('The value of r: ')
    r = float(userInput)
    equation = LogisticChaos(xNaught,r)
    equation.calcTerms()
    userInput = input('Generate another set of values? [Y/n]')
    if userInput.strip() == 'n':
        break
