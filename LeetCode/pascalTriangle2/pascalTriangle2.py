class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        bigArray = [[1]]
        for i in range(rowIndex):
            tmp = [0] + bigArray[-1] + [0]
            tmp2 = []
            for j in range(len(bigArray[-1])+1):
                tmp2.append(tmp[j]+tmp[j+1])
            bigArray.append(tmp2)
        return bigArray[rowIndex]