import random
import os
import numpy

def main():
    labels = []
    data = []
    path = "E:\\PJATK\\NAI\\MP\\MP3\\Data"

    a = float(input("stala uczenia: "))
    n = int(input("liczba epok: "))

    perceptron = Perceptron(a)
    labels = label_reader(path)
    data = reader(path, labels)
    perceptron.train(data, n, len(labels))
    loop = 0
    
    while loop == 0:
        input_text = input("(1 by wyjsc) poprosze tekst do klasyfikacji: ")
        if input_text == "1":
            loop = 1
        else:
            str = input_text.replace('\n', '').lower()
            str = ''.join(c for c in str if c.isalpha())
        
            print(str)
        
            print(f'moim zdaniem tekst jest w jezyku {labels[perceptron.classify(str)]}m...')
        

def reader(path, labels):
    
    data = []
    
    for folder in os.listdir(path):
        

        for item in os.listdir(f"{path}/{folder}"):
            
            print(folder)

            file_path = os.path.join(path,folder, item)
            with open(file_path, 'r') as file:
                str = file.read().replace('\n', '').lower()
                str = ''.join(c for c in str if (ord('a') <= ord(c)<=ord('z')))
                
                print(str)

                language = labels.index(folder)
                data.append((str, language))
                
    return data
        


def label_reader(path):
    
    return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]


        

    




    
        
class Perceptron:
    
    def __init__(self, a):
        
        self.a = a
        self.w = None
        self.t = None


    def normalize(self, str):
        
        char_count = numpy.zeros(26)

        for c in str:
            char_count[ord(c) - ord('a')] += 1
        normal = char_count / numpy.linalg.norm(char_count)
        
        return normal


    def train(self, data, n, lang_n):

        self.w = numpy.array([[random.uniform(0, 1)] * 26 for _ in range(lang_n)])
        self.t = numpy.array([random.uniform(0,1) for _ in range(lang_n)])
        
        for i in range(n):
            for str, d in data:
                inputs = numpy.array(list(self.normalize(str)))
                out = numpy.dot(self.w, inputs)-self.t
                y = numpy.zeros(lang_n)
                y[out > 0] = 1
                error = numpy.zeros(lang_n)
                error[d] = 1
                error -= y
                self.w += numpy.outer(error, inputs)*self.a
                self.t -= error*self.a 
                
    def classify(self, str):

        inputs = numpy.array(list(self.normalize(str)))
        dot = numpy.dot(self.w, inputs)-self.t
        
        return numpy.argmax(dot)













if __name__ == '__main__':
    main()

