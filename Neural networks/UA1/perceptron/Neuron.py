from random import random

class  Neuron:
    
    def __init__(self,data,learningRate = 0.1):
        self._learning_rate = learningRate
        self._input,self._output = data
        #Randomise weights.
        self._weight =  map(lambda x: x*random(), [1] * len(self._input))
        #print self._weight
        self._y = None
        self._global_error = 0.0
        
        
    def train(self,data):    
        self._input,self._output = data
        #Calculate output.
        self._y = self._sign(self._sum()) 
        #Calculate error.
        if self._error() != 0:
            #Update weights.
            self._adjust_weight()
        #Convert error to absolute value.
        self._global_error += abs(self._error())
        
    def execute(self,input):
        self._input = input
        #Calculate output.
        self._y = self._sign(self._sum())
        return self._y
        
    
    def _sum(self):
        return sum(map(lambda x,y: x*y, self._input,self._weight))
    
    def _sign(self,output):
        if output < 0:
            y = -1
        else:
            y = 1
        return y
    
    def _error(self):
        return self._output - self._y    
    
    def _adjust_weight(self):
        self._weight = map(lambda x,y: x + (y*self._learning_rate*self._error()),self._weight,self._input)    
    
    def get_global_error(self):
        return self._global_error
    
    def reset_global_error(self):
        self._global_error = 0