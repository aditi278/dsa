class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        l = len(nums)//2 
        for x in nums:
            if x in hashMap.keys():
                hashMap[x]+=1
            else:
                hashMap[x]=1
            if hashMap[x]>l:
                return x
        