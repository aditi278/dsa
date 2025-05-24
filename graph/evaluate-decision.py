class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        arr = [0]*len(queries)
        m = {}
        for i in range(len(equations)):
            x = equations[i][0]
            y = equations[i][1]
            if x not in m:
                m[x] = {}
            if y not in m:
                m[y] = {}
            m[x][y] = values[i]
            m[y][x] = 1/values[i]

        def getVal(x, y, m, visited=None):
            if visited is None:
                visited = set()
            visited.add(x)
            if y in m[x]:
                return m[x][y]
            
            for key, val in m[x].items():
                if key in visited:
                    continue
                sol = getVal(key, y, m, visited)
                if sol != -1.0:
                    m[x][y] = sol * val
                    return val * sol
            return -1.0
            

        for i in range(len(queries)):
            x = queries[i][0]
            y = queries[i][1]
            if x not in m or y not in m:
                arr[i] = -1.0
            elif x == y:
                arr[i] = 1.0
            else:
                arr[i] = getVal(x, y, m)
        return arr
        