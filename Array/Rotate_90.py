class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in matrix:
            i.reverse()
        return matrix
s1=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(s1.rotate(matrix))
