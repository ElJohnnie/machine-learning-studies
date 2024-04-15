from Neuron import *

class Perceptron:
    def __init__(self,inputs,iterations=100):
        self._inputs = inputs
        self._refresh_inputs = list(inputs)
        self._iterations = iterations
        self._iteration = 0
        self._neuron = Neuron(self._get_rand_input())
        self._train()
    
    
    def _train(self):
        while self._iteration <= self._iterations:
            self._neuron.reset_global_error()
            self._refresh_inputs = list(self._inputs)
            for i in range(len(self._refresh_inputs)):
                self._neuron.train(self._get_rand_input())
                print("Iteration %d Error: %f" % (self._iteration, self._neuron.get_global_error()))
                self._iteration += 1
                if(self._neuron.get_global_error() == 0.0):
                    break
            
        
    def _get_rand_input(self):
        return self._refresh_inputs.pop()

    
    def execute(self,input):
        return self._neuron.execute(input)
        
        
    def arange(self,start,stop=None,step=None):
        if stop is None:
            stop = float(start)
            start = 0.0
        if step is None:
            step = 1.0
        cur = float(start)
        while cur <= stop:
            yield cur
            cur+=step