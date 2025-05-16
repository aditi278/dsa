class Solution:
    def searchRow(self, row, target, start, end):
        if end < start:
            return False
        mid = start + (end - start)//2
        if row[mid] == target:
            return True
        if row[mid] > target:
            return self.searchRow(row, target, start, mid-1)
        else:
            return self.searchRow(row, target, mid+1, end)
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
                
        if n == 1:
            return self.searchRow(matrix[0], target, 0, m-1)
        def searchCol(start, end):
            if end < start:
                return False
             
            mid = start + (end - start)//2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                return searchCol(start, mid - 1)
            elif mid+1 == n or (mid+1<n and matrix[mid][0]<target and matrix[mid+1][0] > target):
                return self.searchRow(matrix[mid], target, 0, m-1)
            else:
                return searchCol(mid+1, end)
        return searchCol(0, n-1)