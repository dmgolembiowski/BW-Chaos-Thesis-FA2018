#!/usr/bin/env python3
import math
import re
import sympy

# x is a sympy symbol that gets used as a variable
# for recursively defining functions
# x = sympy.symbols('x')

class DataPoints:
    def __init__(self, eq_Number, X0, r, t_Count):
        self.eq_Number = eq_Number
        self.X0 = X0
        self.r = r
        self.t_Count = t_Count
        self.function_Is = '0'
        self.Data = [self.r, self.X0]

    def function_Checker(self):
        eq_Num = self.eq_Number
        if eq_Num == '1':
            self.function_Is = 'logistic'
        elif eq_Num == '2':
            self.function_Is = 'quadratic'
        elif eq_Num == '3':
            self.function_Is = 'sine'
        elif eq_Num == '4':
            self.function_Is = 'cubic'
        else:
            RuntimeError
        # Call the correct function by name from Class instance
        getattr(self, self.function_Is)()
        
    def logistic(self):
        n = 0
        UniqueList = []
        x0 = self.X0
        while n < self.t_Count + 1:
            self.X0 = self.r * self.X0 * (1 - self.X0)
            if n >= self.t_Count - 32:
                if round(self.X0,3) not in UniqueList:
                    UniqueList.append(round(self.X0,3))
            n += 1
        number_Of_Limits = len(UniqueList)
        print('Logistic Equation')
        print('R =', self.r, 'and X0 =', x0)
        print('Number of Limits is = ',number_Of_Limits)
        print('Distinct Converging Limits are: ', UniqueList)

    def quadratic(self):
        n = 0
        UniqueList = []
        x0 = self.X0
        while n < self.t_Count + 1:
            self.X0 = self.r * (1 - self.X0**2)
            if (self.t_Count - 31) < n < (self.t_Count + 1):
                if round(self.X0,3) not in UniqueList:
                    UniqueList.append(round(self.X0,3))
            n += 1
        number_Of_Limits = len(UniqueList)
        print('Quadratic Function')
        print('R =', self.r, 'and X0 =', x0)
        print('Number of Limits is = ',number_Of_Limits)
        print('Distinct Converging Limits are: ', UniqueList)

    def sine(self):
        sin = math.sin
        pi = math.pi
        n = 0
        UniqueList = []
        x0 = self.X0
        while n < self.t_Count:
            self.X0 = self.r * sin(pi * self.X0)
            if (self.t_Count - 31) <= n < self.t_Count:
                if round(self.X0, 3) not in UniqueList:
                    UniqueList.append(round(self.X0,3))
            n += 1
        number_Of_Limits = len(UniqueList)
        print('Sine Function')
        print('R =', self.r, 'and X0 =', x0)
        print('Number of Limits is: ', number_Of_Limits)
        print('Distinct Converging Limits are: ', UniqueList)

    def cubic(self):
        n = 0
        UniqueList = []
        x0 = self.X0
        while n < self.t_Count:
            self.X0 = (self.r * self.X0) - (self.X0**3)
            if n >= self.t_Count - 32:
                #print('Term = ', n,'and Xn+1 = ',self.X0)
                if round(self.X0, 3) not in UniqueList:
                    UniqueList.append(round(self.X0,3))
            n += 1
        number_Of_Limits = len(UniqueList)
        print('Cubic Function')
        print('R =', self.r, 'and X0 =', x0)
        print('Number of Limits is = ',number_Of_Limits)
        print('Distinct Converging Limits are: ', UniqueList)

def funcRecursion(expression):
    pass

print("For (1)Logistic, (2)Quadratic, (3)Sine, (4)Cubic Chaos EQs,")
userInput = input("Enter Equation_Number,x_Naught,r_Value,term_Count: ")
userInput = re.split(r'[;,\s]\s*',userInput)
# re.split(r'[,;\s]\s*', userInput)
print(userInput)
Equation_Number = userInput[0]
x_Naught = float(userInput[1])
r_Value = float(userInput[2])
term_Count = int(userInput[3])


testData = DataPoints(Equation_Number, x_Naught, r_Value,term_Count)
DataPoints.function_Checker(testData)
