def canSum(targetSum, nums):
    arr = [False]*(targetSum+1)
    arr[0] = True
    for i in range(targetSum):
        if not arr[i]:
            continue
        for n in nums:
            if i+n <= targetSum:
                arr[i+n] = True
    return arr[targetSum]

if __name__=="__main__":
    print("targetSum:7, Array:[2,3]", canSum(7, [2,3]))
    print("targetSum:7, Array:[5,3,4,7]", canSum(7, [5,3,4,7]))
    print("targetSum:7, Array:[2,4]", canSum(7, [2,4]))
    print("targetSum:300, Array:[7,14]", canSum(300, [7,14]))