class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {}
        for x in prerequisites:
            a = x[0]
            b = x[1]
            if a == b:
                return False
            if a in m:
                tmp = m[a]
                tmp.append(b)
                m[a] = tmp
            else:
                m[a] = [b]
            
        def bfs(start, m, visited, currVisited = None):
            if currVisited is None:
                currVisited = []
            if start in currVisited:
                return visited, False
            currVisited.append(start)
            visited.append(start)
            if start in m:
                for deps in m[start]:
                    if deps in m:
                        visited, canFinish = bfs(deps, m, visited, currVisited)
                        if not canFinish:
                            return visited, False
            currVisited.pop()
            del m[start]
            return visited, True
        
        visited = []
        for x in range(numCourses):
            if x not in m:
                continue
            if x not in visited:
                visited, canFinish = bfs(x, m, visited)
                if not canFinish:
                    return False
        return True     