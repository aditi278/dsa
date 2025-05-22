class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = [0]*n
        total = 0
        for i in range(n):
            tank[i] = gas[i] - cost[i]
            total += tank[i]
        if total < 0:
            return -1
        if n == 1 and tank[0] >= 0:
            return 0
        start = -1
        i = 0
        while i < n:
            while tank[i] < 0:
                i += 1
                if i == n:
                    return -1
            start = i
            fuel = tank[i]
            i+=1
            while fuel >= 0 and i < n:
                fuel+=tank[i]
                i+=1
            if i == n-1 and fuel >=0:
                return start
        return start