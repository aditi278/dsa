class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        q = deque()
        depCount = [0]*numCourses
        m = {}
        for course in prerequisites:
            depCount[course[0]] += 1
            if course[1] not in m:
                m[course[1]] = [course[0]]
            else:
                tmp = m[course[1]]
                tmp.append(course[0])
                m[course[1]] = tmp
        
        for i in range(numCourses):
            if depCount[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            result.append(course)
            if course not in m:
                continue
            for x in m[course]:
                depCount[x] -= 1
                if depCount[x] == 0:
                    q.append(x)

        return result if len(result)==numCourses else []