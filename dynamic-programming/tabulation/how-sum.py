def howSum(targetSum, nums):
    arr = [None]*(targetSum+1)
    arr[0] = []
    for i in range(targetSum):
        if arr[i] is None:
            continue
        for n in nums:
            if i + n <= targetSum:
                temp = [x for x in arr[i]]
                temp.append(n)
                arr[i+n] = temp
    return arr[targetSum]

if __name__=="__main__":
    print("targetSum:7, Array:[2,3]", howSum(7, [2,3]))
    print("targetSum:7, Array:[5,3,4,7]", howSum(7, [5,3,4,7]))
    print("targetSum:7, Array:[2,4]", howSum(7, [2,4]))
    print("targetSum:300, Array:[7,14]", howSum(300, [7,14]))