#2-layer BDN simulator - specify number of inputs and hidden layer neurons
import itertools

class BDN(object):
    def __init__(self,hidden,output):
        self.hidden = hidden
        self.output = output
    def process(self,inputs):
        return '\n'.join([str(i)+str(self.output.isfired(self.hidden.fire(i))) for i in inputs])

class hiddenlayer(object):
    def __init__(self,hs):
        self.hiddens = []
        for h in hs:
            self.hiddens.append(neuron(h[0],h[1]))
    def __str__(self):
        return "hidden layer neurons:"+','.join([str(neuron) for neuron in self.hiddens])
    def fire(self, inp):
        return [n.isfired(inp) for n in self.hiddens]

class neuron(object):
    def __init__(self,weights,threshold):
        self.weights = weights
        self.threshold = threshold
    def isfired(self,inputs):
        return int(sum([a*b for a,b in zip(inputs,self.weights)]) > self.threshold)
    def __str__(self):
        return str(self.weights) + str(self.threshold)


n_inputs = 3 #this value is not used anywhere.

BDN1 = BDN(hiddenlayer([[(-1,-1,-1),-0.5],[(1,1,-1),1.5],[(1,-1,1),1.5],[(-1,1,1),1.5]]),neuron((1,1,1,1),0.5)) #each neuron is a list consisting of a tuple of weights and a threshold value
BDN2 = BDN(hiddenlayer([[(-1,-1,-1),-0.5],[(1,1,1),1.5],[(1,1,1),2.5]]),neuron((1,1,-2),0.5))
#print hiddens

inputs = map(list,itertools.product([0,1],repeat=3))
print BDN1.process(inputs)
print ""
print BDN2.process(inputs)