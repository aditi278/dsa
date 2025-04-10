#given a targetSum and array of nums, find if targetSum possible
def canSum(targetSum, nums, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for x in nums:
        newTargetSum = targetSum - x
        if canSum(newTargetSum, nums, memo=memo):
            memo[newTargetSum]=True
            return True
    memo[newTargetSum]=False
    return False

if __name__=="__main__":
    print("targetSum:7, Array:[2,3]", canSum(7, [2,3]))
    print("targetSum:7, Array:[5,3,4,7]", canSum(7, [5,3,4,7]))
    print("targetSum:7, Array:[2,4]", canSum(7, [2,4]))
    print("targetSum:300, Array:[7,14]", canSum(300, [7,14]))