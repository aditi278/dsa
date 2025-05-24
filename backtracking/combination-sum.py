class Solution:
    def combinationSum(self, candidates: List[int], target: int, ans = None, curr = None) -> List[List[int]]:
        if ans is None:
            ans = []
        if curr is None:
            curr = []
        if target == 0:
            if sorted(curr) not in ans:
                tmp = [x for x in curr]
                ans.append(sorted(tmp))
            return ans
        for x in candidates:
            if x <= target:
                curr.append(x)
                self.combinationSum(candidates, target - x, ans, curr)
                curr.pop()
        return ans