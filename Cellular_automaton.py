# Cellular automaton

"""
Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

import matplotlib.pyplot as plt
import numpy as np

def rule(i,j,m,n):
	# Location of 8 neighbors of Cell
	neighbour = [(i-1,j+1),(i,j+1),(i+1,j+1),(i-1,j),(i+1,j),(i-1,j-1),(i,j-1),(i+1,j-1)]
	
	# Counting the number of living neighbor cells
	k=0
	for c in neighbour:
		x = c[0]
		y = c[1]
		if (i-1)>0 and (i+1)<m and (j-1)>0 and (j+1)<n:
			if results[x][y] == 1:
				k = k+1

	# If the living is equal to 3, the cell state becomes "living"			
	if k==3:
		results[i][j]=1 #1 stands for "living"
		return True

	# If the living is equal to 2, the cell state remains unchanged; Otherwise, the cell state becomes "dead"
	if k==2:
		return True
	else:
		results[i][j]=0 #0 means "dead"
		return False 

# Start Main Program
if __name__=='__main__':                  #explanation  https://realpython.com/if-name-main-python/
	
	#Python sets the global __name__ of a module equal to "__main__" 
	#if the Python interpreter runs your code in the top-level code environment
	#In an imported module, the value of __name__ is the module’s name as a string.
	
	plt.ion #Turn on interactive mode

	#Specify area size
	N=100

	#Specify the number of life seeds
	seed_num=1000

	#Specify Iterations
	iter_num=100

	x=np.arange(1,N+1,1)  #Generate the number of sequences with an interval of 1 between (1, N)
	y=np.arange(1,N+1,1)  #Generate the number of sequences with an interval of 1 between (1, N)

	m=len(x)
	n=len(y)
	X,Y=np.meshgrid(x,y)  #Generate grid coordinate matrix, N * N points

	#Cell status in initialization area
	results = np.zeros((m,n))

	#Seeds of life are sown, and the position of the seed is randomly generated
	for d in range(seed_num):
		i=np.random.randint(m)
		j=np.random.randint(n)
		results[i][j]=1

	#Generate initial state diagram
	plt.imshow(results)

	plt.pause(0.1)

	#Life iteration
	for t in range(iter_num):
		for i in range(m):
			for j in range(n):
				rule(i,j,m,n)

        #Clear drawing area
		#plt.cla() 

		plt.imshow(results)

		plt.pause(0.1)
