class Solution(object):
    def spiralOrder(self, matrix):
        n=len(matrix)
        l=0
        r=len(matrix[0])-1
        t=0
        b=n-1
        result=[]
        while t<=b and l<=r:
            for i in range(l,r+1):
                result.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                result.append(matrix[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    result.append(matrix[b][i])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    result.append(matrix[i][l])
                l+=1
        return result
s1=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(s1.spiralOrder(matrix))