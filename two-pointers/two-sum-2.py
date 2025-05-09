class Solution:
    def findTarget(self, numbers, target, start, end):
        if end < start:
            return -1
        mid = start +(end-start)//2
        if target==numbers[mid]:
            return mid
        elif target < numbers[mid]:
            return self.findTarget(numbers, target, start, mid-1)
        elif target > numbers[mid]:
            return self.findTarget(numbers, target, mid+1, end)
        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n-1):
            j = self.findTarget(numbers, target - numbers[i], i+1, n-1)
            if j > 0:
                return [i+1, j+1]