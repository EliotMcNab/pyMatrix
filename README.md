matrixHandler
=============

A small module which adds a Matrix class to be used as a new data type.
Use this to represent and manipulate matrixes in Python

The code is made for Python3

Installation
------------

Fast Install : 

::

    pip install pymatrix

Manual install TBA

::

    placeHolder

Install the package :

::

    python setup.py install

Example
-------

..code::python

    from pymatrix import matrix

    # creates a 2x3 matrix based on a list
    matrix1 = Matrice([[1, 2],[3, 4],[5, 6]])

    # creates another 3x2 matrix
    matrix2 = Matrice([[10, 9, 8], [7, 6, 5]])

    # multiples both matrixes
    multMatrix = matrix1 * matrix2

    # displays the result
    print(multMatrix)

Output:

[14, 12]
[28, 24]
[42, 36]