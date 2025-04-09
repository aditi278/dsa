#given a targetSum and array of nums, find list of nums that add up to targetSum
def howSum(targetSum, nums, memo=None):
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
        valid_nums = howSum(newTargetSum, nums, memo=memo)
        if valid_nums is not None:
            valid_nums.append(x)
            memo[targetSum] = valid_nums
            return valid_nums
    memo[targetSum] = None
    return None

if __name__=="__main__":
    print("targetSum:7, Array:[2,3]", howSum(7, [2,3]))
    print("targetSum:7, Array:[5,3,4,7]", howSum(7, [5,3,4,7]))
    print("targetSum:7, Array:[2,4]", howSum(7, [2,4]))
    print("targetSum:300, Array:[7,14]", howSum(300, [7,14]))