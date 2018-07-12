import numpy as np
from deepNeuralLib import *
from dataLib import *
import matplotlib.pyplot as plt

def main():
	file = 'Mark1 Data/Technology Sector/Technology Sector.test.5.txt'
	sectorName = file.split('/')[1]

	df = readData(file, ';')

	xNorm, x, y = prepareData(df, 10)

	n_hidden_layers = 4
	hidden_size = [180, 60, 20, 6]
	out_classes = 1

	learning_rate = 0.01
	epochs = 1000

	deepNN = DeepNeuralNetwork(x.shape[1], hidden_size, out_classes, n_hidden_layers, 3)

	error = deepNN.train(xNorm, y, learning_rate, epochs, 1)

	yAprox = deepNN.feedForward(xNorm)

	print(accuracyVector(y, yAprox))

	print("SQD ERROR:")
	
	plt.plot([i for i in range(len(error))], error, color='b', linestyle='-')
	plt.show()


	f = open("test1.txt", "w")

	for i in range(len(y)):
		f.write(str(y[i])+"->"+str(yAprox[i])+"\n")

	f.close()



if __name__ == '__main__':
	main()

