# Task ID : 1
# The given task : Creating random 10x10 matrix and diagonal summation for this matrix.

import numpy as np
import random as rd

# This function include the random matrix generator with numpy and random library.
# First argument defines the size of matrix| for example if you want 3x3 -> randomnp(3,start,end).
# Second and third arguments is the range of random integers, both arguments included.

def rdmatrix(size,start,end):
    if type(size) == int and type(start) == int and type(end) == int:
        pid = 1 # The process number variable as integer.
        matrixtxt = "" # The variable that provides us to np.asmatrix's first argument as string.
        while pid<size*size+1:
            if not pid == size*size: # This if statements for text formatting in np.asmatrix function.
                if pid % size == 0:
                    matrixtxt+=str(rd.randint(start,end)) + "; " 
                else:
                    matrixtxt+=str(rd.randint(start,end)) + " " 
            else:
                matrixtxt+=str(rd.randint(start,end))
            pid+=1
        return np.array(np.asmatrix(matrixtxt))
    else:
        return print("TypeError: Please enter valid types.") # Type Check

# This function includes the matrix array's diagonal summation.
# Takes as first argument the np.ndarray type and returns the INTEGER type.

def diagsumMatrix(arr): 
    if type(arr) == np.ndarray: 
        diagonarr = arr.diagonal() # Basically uses the combination of diagonal and summation method.
        result = diagonarr.sum()
        return result
    else:
        return print("TypeError: Please enter a valid type.") # Type Check

# This function returns the array that includes the given matrix's integer elements which has diagonal location.
# Takes and returns 'np.ndarray' type.
def diag(arr):
    if type(arr) == np.ndarray:
        return arr.diagonal()
    else:
        return print("TypeError: Please enter a valid type.")

# Debug codes:
# myArray = rdmatrix(10,1,100)
# print(myArray)
# sum = diagsumMatrix(myArray)
# print(sum)
# print(diag(myArray))