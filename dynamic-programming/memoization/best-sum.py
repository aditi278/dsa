#given a targetSum and array of nums, find list of nums that add up to targetSum
def bestSum(targetSum, nums, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    for x in nums:
        newTargetSum = targetSum - x
        valid_nums = bestSum(newTargetSum, nums, memo=memo)
        if valid_nums is not None:
            valid_nums.append(x)
            if targetSum not in memo.keys() or len(memo[targetSum]) > len(valid_nums):
                memo[targetSum] = valid_nums
    if targetSum in memo.keys():
        return memo[targetSum]
    memo[targetSum] = None
    return None

if __name__=="__main__":
    print("targetSum:7, Array:[2,3]", bestSum(7, [2,3]))
    print("targetSum:7, Array:[5,3,4,7]", bestSum(7, [5,3,4,7]))
    print("targetSum:7, Array:[2,4]", bestSum(7, [2,4]))
    print("targetSum:5, Array:[2,3,5]", bestSum(8, [2,3,5]))
    print("targetSum:300, Array:[7,14]", bestSum(300, [7,14]))