import random

class Matrix():

    def __init__(self, matrix = []):
        """initialises Matrix class"""

        self.__matrix = matrix

    @property
    def matrix(self):
        """allows acess to a matrix
            ex : aMatrix.matrix"""
        return self.__matrix

    @matrix.setter
    def matrix(self, value):
        """helps to change the value of a matrix
            ex : aMatrix.matrix = [...]"""
        if(type(value) == list):
            self.__matrix = value
        else:
            raise ValueError("Can only affect a Matrix to another Matrix")

    def __len__(self):
        """returns matrix's width
            ex : len(aMatrix)"""
        return len(self.matrix)

    def __repr__(self):
        """displays matrice when variable is called
            ex: aMatrice"""

        strMatrix = ""
        for y in range(len(self)-1):
            strMatrix += str(self[y]) + "\n"
        strMatrix += str(self[-1])
        return strMatrix

    def __str__(self):
        """determines how a matrix is displayed
            ex : print(aMatrix)"""
        strMatrix = "\n"
        for y in range(len(self)-1):
            strMatrix += str(self[y]) + "\n"
        strMatrix += str(self[-1])
        return strMatrix

    def __getitem__(self, key):
        """returns the value of elements within a matrix
            ex : aMatrix[y][x]"""
        return self.matrix[key]

    def __setitem__(self, index, value):
        """alows to easily modify elements within a matrix
            ex : aMatrix[y][x] = a"""
        self.matrix[index] = value

    def __eq__(self, other):
        """returns True if two matrices are equal
            ex : aMatrix1 == aMatrix2"""
        if(len(self) == len(other) and len(self[0]) == len(self[0])):
            for y in range(len(self)):
                for x in range(len(self[0])):
                    if(self[y][x] != other[y][x]):
                        return False
            return True

        return False      

    def __ne__(self, other):
        """returns True if a matrix isn't equal to another parameter
            ex : aMatrix1 != a"""
        if(len(self) == len(other) and len(self[0]) == len(self[0])):
            for y in range(len(self)):
                for x in range(len(self[0])):
                    if(self[y][x] != other[y][x]):
                        return True
            return False

        return True   

    def __add__(self, other):
        """returns the sum of two matrixes
            ex : aMatrix1 + aMatrix2"""
        
        try:
            if(len(self) == len(other) and len(self[0]) == len(other[0])):
                sumMatrix = Matrix([[self[y][x] + other[y][x] for x in range(len(self[0]))]for y in range(len(self))]) 
                return sumMatrix

            raise ValueError("Matrixs must have equal size")

        except AttributeError:
            raise ValueError("can only add Matrixs together")

    def __iadd__ (self, other):
        """increments a matrixe
            ex : aMatrix1 += aMatrix2"""
        return self + other

    def __sub__(self, other):
        """returns the difference between two matrixes
            ex : aMatrix1 - aMatrix2""" 
        
        try:
            if(len(self) == len(other) and len(self[0]) == len(self[0])):
                differenceMatrix = Matrix([[self[y][x] - other[y][x] for x in range(len(self[0]))]for y in range(len(self))])
                
                return differenceMatrix

            raise ValueError("Matrixs must have equal size")

        except AttributeError:
            raise ValueError("can only substract Matrixs together")

    def __isub__(self, other):
        """decrements a matrix
            ex : aMatrix1 -= aMatrix2"""
        return self - other

    def __neg__(self):
        """returns a matrix's opposite
            ex : - aMatrix"""
        opposeMatrix = Matrix([[-self[y][x] for x in range(len(self.matrix[0]))]for y in range(len(self.matrix))])
        
        return opposeMatrix

    def __mul__(self, other):
        """multiplies a matrice by another matrice, and int or a float
            ex : aMatrix1 * aMatrix2
            ex : aMatrix * 2
            ex : aMatrix * 1.2
        /!\\ multiplying a matrix by a float will lead to aproximative results"""

        try: 
            if(type(other) == int or type(other) == float):
                multMatrix = Matrix([[self[y][x] * other for x in range(len(self[0]))]for y in range(len(self))])

            elif(len(self.matrix[0]) == len(other.matrix)):
                multMatrix = Matrix([[sum([self[y][x] * other[x][i] for x in range(len(self[0]))]) for i in range(len(other[0]))]for y in range(len(self))])

            return multMatrix

        except AttributeError:
            raise ValueError("matrix can only be multipled by other matrix, int or float")
        else:
            raise ValueError("Matrixs must have valid sizes")

    def __imul__(self, other):
        """assigns the value of a multiplication to a matrix
            ex : aMatrix1 *= aMatrix2
            ex : aMatrix * 2
            ex : aMatrix * 1.2
        /!\\ multiplying a matrix by a float will lead to aproximative results"""
        return self * other