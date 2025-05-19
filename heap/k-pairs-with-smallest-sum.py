import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        l = []
        h = []
        heapq.heappush(h, (nums1[0]+nums2[0], 0 ,0))
        n = len(nums1)
        m = len(nums2)

        while k:
            k-=1
            _, i, j = heapq.heappop(h)
            l.append([nums1[i], nums2[j]])
            print(i, j, nums1[i], nums2[j])
            if j == 0 and i+1 < n:
                heapq.heappush(h, (nums1[i+1]+nums2[0], i+1, 0))
            if j+1 < m:
                heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))
        return l