class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        longest = 0
        curr = ""
        for x in s:
            if x not in curr:
                curr+=x
            else:
                curr = curr.split(x)[1]+x
            longest = max(longest, len(curr))
        return longest