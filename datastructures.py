#!/usr/bin/env python3
import numpy as np
from collections import deque
import hashlib

class Chaos():
    def __init__(self, rLowerBd, rUpperBd, option):
        """
        The essential bifurcation diagram properties
        """
        self.rLowerBd = rLowerBd
        self.rUpperBd = rUpperBd
        self.steps = 500
        self.terms = 50000
        self.xArray = np.ones([self.terms, self.steps])
        self.tailSize = 10
        self.rStep = (rUpperBd - rLowerBd) / self.steps
        self.option = {
            1:"Chaos.logistc",
            2:"Chaos.other"}

    def __str__(self):
        return f"""Constellation(
            rLowerBd = {self.rLowerBd}, 
            rUpperBd = {self.rUpperBd}, 
            steps = {self.steps},
            terms = {self.steps}, 
            xArray = {self.steps}, 
            tailSize = {self.tailSize}, 
            rStep = {self.rStep})"""

    def logistic(self, rLowerBd, rUpperBd):
        pass
    
    def other(self,rLowerBd, rUpperBd):
        pass

class Orbit(Chaos):
    def __init__(self, rLowerBd, rUpperBd, limits):
        super().__init__()
        self.rLowerBd = rLowerBd
        self.rUpperBd = rUpperBd
        self.rRange = range(self.rLowerBd, self.rUpperBd,self.rStep)
        self.limits = {}
        # WTS limits = 

    def __str__(self):
        return """Orbit(Birfurcation) is the data structure holding
        set of Xn+1 values that correspond to stable limits (orbits)
        for some particular value of R on the horizontal axis.
        To store limit/orbit values for some R value, you could use
        NAME.limits[rValue] = [value1, value2, ...]
        For many cases it will be possible to simply type:
        INSTANCE_NAME.limits[3.4459] if there is not an identical 
        key.
        """

def toBigInt(r):
    rString = str(r).split('.')
    
    decimal_places = float(10 ** (0 - len(rString[1])))
    r = [int(rString[0] + rString[1]), decimal_places]

    rBytes = (int(rString[0] + rString[1])).to_bytes(256, byteorder='big')
    rBytes = hashlib.sha256(rBytes)
    rBytes = rBytes.hexdigest()
    return rBytes

def rKeys(R):
    RString = str(R).split('.')
    decimal_places = float(10 ** (0 - len(RString[1])))
    R = [int(RString[0] + RString[1]), decimal_places]
    return R