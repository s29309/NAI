

class Perceptron:
    
    values = [[]]
    data = [[]]
    labels = []
    w = []
    a = 0
    unique_labels = []
    wrong_label1 = 0
    wrong_label2 = 0
    

    def __init__(self, data, a):
        self.data = data
        self.values = [l[:-1] for l in data]
        self.labels = [l[-1] for l in data]
        self.a = a
        self.w = [0]*(len(self.values[0]))
        self.find_unique_labels()
    
    def compute(self, vector):
        y = sum(w*x for w, x in zip(self.w, vector))
        if y>=0:
            return 1
        return -1
    

    def compute_all(self):
        for vector in self.data:
            y = self.compute(vector[:-1])
            label = self.translate_label(vector[-1])
            if y != label:
                
                print(vector)

                if label == 1:
                    self.wrong_label1+=1
                self.wrong_label2+=1
           
        if self.wrong_label1+self.wrong_label2<len(self.data):
            print(f"Celnosc: {float(len(self.data))/(float(len(self.data))-float((self.wrong_label1+self.wrong_label2)))}")
        else:
            print(f"Celnosc: 0..")
                



    def learn(self, vector, label):
        y = self.translate_label(label)
        result = self.compute(vector)
        if result != y:
            for i in range(len(self.w)):
                self.w[i] += self.a*(y-result)*vector[i]
                

    def find_unique_labels(self):
        for x in self.labels:
            if x not in self.unique_labels:
                self.unique_labels.append(x)
                
    def translate_label(self, label):
        if label == self.unique_labels[0]:
            return 1
        else:
            return -1
            
        
        
