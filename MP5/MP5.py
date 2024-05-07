from ast import Not
import csv
import math
import random
from turtle import update

class Perceptron:
    
    def read_file(this, filename):
        data = []
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                vector = [float(val) for val in row]
                data.append(vector)
        return data


    def kmeans(this, data, k):
        centroids = []
        while len(centroids)<k:
            random_point = random.choice(data)
            if not centroids.__contains__(random_point):
                centroids.append(random_point)
        groups = [[] for _ in range(k)]
        
        loop = True
        while loop:
            groups = [[] for _ in range(k)]
            for point in data:
                distances = [this.calculate_distance(point, centroid) for centroid in centroids]
                group_index = distances.index(min(distances))
                groups[group_index].append(point)

            
            new_centroids = this.update_centroids(groups, centroids)
            if new_centroids == centroids:
                loop = False

            e = 0
            for group, centroid in zip(groups, centroids):
                e += sum(this.calculate_distance(point, centroid) for point in group)

            index = 1
            for group in groups:
                print(f'grupa {index}: {len(group)} wektorow')
                index += 1
                for point in group:
                    print(point)
            print(f'suma kwadratow odleglosci: {e} \n')

            centroids = new_centroids            

    def calculate_distance(this, p1, p2):
        distance = 0
        for i in range(len(p1)):
            distance += (p1[i] - p2[i]) ** 2
        return distance
    
    def update_centroids(this, groups, prev_centroids):
        centroids = []
        for group in groups:
            if group:
                centroid = tuple(sum(point[i] for point in group) / len(group) for i in range(len(group[0])))
                centroids.append(centroid)
            else:
                centroids.append(centroids[groups.index(group)])
        return centroids
        

def main():
    perceptron = Perceptron()
    data = perceptron.read_file('test.csv')
    k = int(input("poprosze k: "))
    perceptron.kmeans(data, k)

    
if __name__ == "__main__":
    main()