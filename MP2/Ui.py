from Perceptron import Perceptron
from Trainer import Trainer


class UI:


    def get_vector_input(self):

        try:
            vector_str = input("(0 - wyjscie) poprosze vector do klasyfikacji: ")
            vector = [float(x) for x in vector_str.split(";")]
            return vector
        except ValueError:
            print("nie dziala...")
            return []

    def read_file(self, file_path):
        result = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    strings = line.strip().split(';')
                    values = [float(x) for x in strings[:-1]]
                    values.append(strings[-1])
                    result.append(values)
            #print(result)
            return result
        except FileNotFoundError:
            print(f"nie ma pliku...")
            return []

    def compute_vector(self, vector):
        result = self.perceptron.compute(vector)
        if result == 1:
            print("wektor nalezy do grupy 1")
        else:
            print("wektor nalezy do grupy 2")



    def run(self):
        train_set = []
        test_set = []
        vector = []

        print("dzien dobry")
        while train_set == []:
            train_set_path = input("train set path: ")
            train_set=self.read_file(train_set_path)

        while test_set == []:
            test_set_path = input("test set path: ")
            test_set=self.read_file(test_set_path)

        self.perceptron = Perceptron(test_set, 0.5)
        trainer = Trainer(train_set, self.perceptron, 6)
        
        trainer.train_perceptron()
        self.perceptron.compute_all()


        vector = self.get_vector_input()
        while vector!=[0]:
            self.compute_vector(vector)
            vector = self.get_vector_input()
            




if __name__ == "__main__":
    ui = UI()
    ui.run()
