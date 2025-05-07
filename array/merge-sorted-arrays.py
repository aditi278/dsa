class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        l=m+n
        count = 0
        
        while i<l and j<n and count<m:
            if nums1[i]>nums2[j]:
                for k in range(l-1-i):
                    print(k)
                    nums1[m+n-k-1] = nums1[m+n-k-2]
                nums1[i]=nums2[j]
                print(nums1)
                i+=1
                j+=1
                
            else:
                i+=1
                count+=1
        while j<n:
            print(i,j)
            nums1[i]=nums2[j]
            i+=1
            j+=1