__author__ = 'JH'


import numpy

A = numpy.array([[1, 2, 3], [1, 2, 1]])
B = numpy.array([[2, 1, 3], [-1, 0, 5]])

B = B.transpose()
C = numpy.dot(A, B)
print(C)



