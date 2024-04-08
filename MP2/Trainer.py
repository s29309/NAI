class Trainer:
    
    def __init__(self, data, perceptron, n):
        self.data = data
        self.perceptron = perceptron
        self.n = n
    
    def train_perceptron(self):
        for i in range(self.n):
            for vector in self.data:
                self.perceptron.learn(vector[:-1], vector[-1])
            
            
        




