'''
Homework #7
Part #2
This file contains the necessary functions to transpose a matrix by switching the rows and columns. 
'''
import sys

def transpose(matrix):
    '''
    This function transposes a matrix by switching the rows and columns of the matrix. This file takes a matrix as a list and returns the transpose of the matrix as a list. 
    This function has one input: matrix
    This function has one output: transMatrix
    '''
    i = 0
    transMatrix = []
    
    while i < len(matrix[1]):
        newMatrix = []
        for j in range(len(matrix)):
            newMatrix.append(matrix[j][i])
        transMatrix.append(newMatrix)
        i = i + 1
        
    return transMatrix


def main():

    #opens the file from the command line parameter
    fin = open(sys.argv[1],'r')
    
    matrix = [] #creates an empty list

    for line in fin:
        matrixList = line.split() #splits each line of the file into a list
        matrix.append(matrixList) #adds the list of each line to a list of all of the lines

    #calls the transpose function and assigns the returned list to a variable
    transMatrix = transpose(matrix)

    #opens a new file from the command line parameter to write inside of
    fout = open(sys.argv[2], 'w')
    
    i = 0
    while i < len(transMatrix):
        newString = ''

        #for each sublist of transMatrix, a string is created containing the values of the sublist
        for j in range(len(transMatrix[0])): 
            newString = newString + transMatrix[i][j] + '\t'
        i = i + 1
        fout.write(newString + '\n')  #writes the string of the sublist in the new file

    fin.close() #closes the file being read
    fout.close() #closes the file being written in

main()
