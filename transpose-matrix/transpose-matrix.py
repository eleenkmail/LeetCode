import numpy

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(matrix)
        cols = len(matrix[0])
        

        result = numpy.zeros([cols, rows], dtype='int')
        for i in range(rows):
            
            for j in range(cols):

                result[j][i] = matrix[i][j]
                

        return result

        