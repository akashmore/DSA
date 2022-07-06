class solution:
    def solve(self,matrix):
        left,right = 0,len(matrix)-1
        while left < right:
            for i in range(right-left):
                top,bottom = left,right
                temp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = temp
            left+=1
            right-=1
        return matrix
                
if __name__ == '__main__':
    obj = solution()
    result = obj.solve([[1,2,3],[4,5,6],[7,8,9]])
    print(result)