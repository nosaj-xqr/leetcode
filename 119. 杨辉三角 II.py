'''
递归思想得出结果
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        result=[0 for x in range(rowIndex+1)]
        last_row = self.getRow(rowIndex-1)
        result[0]=1
        result[rowIndex]=1
        for i in range(1,rowIndex):
            result[i]=last_row[i-1]+last_row[i]
        return result
