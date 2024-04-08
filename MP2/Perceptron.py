

class Perceptron:
    
    values = [[]]
    data = [[]]
    labels = []
    w = []
    a = 0
    first_label = ""
    wrong_label1 = 0
    wrong_label2 = 0
    bias = 0.5
    

    def __init__(self, data, a):
        self.data = data
        self.values = [l[:-1] for l in data]
        self.labels = [l[-1] for l in data]
        self.a = a
        self.w = [1]*(len(self.values[0]))
        self.first_label = data[0][-1]
    
    def compute(self, vector):
        y = -self.bias
        for i in range(len(self.w)):
            y+=self.w[i]*vector[i]
        if y>=0:
            return 1
        return 0
    

    def compute_all(self):
        for vector in self.data:
            y = self.compute(vector[:-1])
            
            if vector[-1] == self.first_label:
                label = 1
            else:
                label = 0
            
            print(vector)
            print(self.w)
            print(y)
            print(label)
            print()

            if y != label:
                print("zle!!")
                if label == 1:
                    self.wrong_label1+=1
                else:
                    self.wrong_label2+=1
           
        wrong=self.wrong_label1+self.wrong_label2
        total=len(self.data)
        right=total-wrong
        right1 = total/2 - self.wrong_label1
        right2 = total/2 - self.wrong_label2

        print(f"Celnosc: {right/total*100}%")
        print(f"Celnosc grupy 1: {right1/total*200}%")
        print(f"Celnosc grupy 2: {right2/total*200}%")

                



    def learn(self, vector, label):
        if label == self.first_label:
            y = 1
        else:
            y = 0
        result = self.compute(vector)
        error = y-result
        for i in range(len(self.w)):
            self.w[i] += self.a*error*vector[i]
        self.bias -= error*self.a
                
                
            
        
        
