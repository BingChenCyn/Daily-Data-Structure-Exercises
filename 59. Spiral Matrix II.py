from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        Matrix=[[0]*n for _ in range(n)]
        left,top,right,bottom=0,0,n-1,n-1
        count=1
        while count<=n*n:
            for j in range(left,right+1):
                Matrix[top][j]=count
                count+=1
            for i in range(top+1,bottom+1):
                Matrix[i][right]=count
                count+=1
            if left <= right and top <= bottom:
                for i in range(right-1,left-1,-1):
                    Matrix[bottom][i]=count
                    count+=1
                for j in range(bottom-1,top,-1):
                    Matrix[j][left]=count
                    count+=1
            top+=1
            left+=1
            right-=1
            bottom-=1
        return Matrix

S=Solution()
print(S.generateMatrix(4))