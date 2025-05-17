class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        n = len(matrix)
        m = len(matrix[0])
        i = row_start = 0
        row_end = n-1
        j = col_start = 0
        col_end = m-1
        traverse = "row-l-r"
        while len(arr) < m*n:
            arr.append(matrix[i][j])
            if traverse == "row-l-r":
                if j == col_end:
                    traverse = "col-u-d"
                    row_start+=1
                    i+=1
                else:
                    j+=1          
            elif traverse == "col-u-d":
                if i == row_end:
                    traverse = "row-r-l"
                    col_end-=1
                    j-=1
                else:
                    i+=1
            elif traverse == "row-r-l":
                if j == col_start:
                    traverse = "col-d-u"
                    row_end-=1
                    i-=1
                else:
                    j-=1
            elif traverse == "col-d-u":
                if i == row_start:
                    traverse = "row-l-r"
                    col_start += 1
                    j+=1
                else:
                    i-=1
        return arr
