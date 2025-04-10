def bestSum(targetSum, nums):
    arr = [None]*(targetSum+1)
    arr[0] = []
    for i in range(targetSum):
        if arr[i] is None:
            continue
        for n in nums:
            if i+n <= targetSum and (arr[i+n] is None or len(arr[i])<len(arr[i+n])):
                temp = [x for x in arr[i]]
                temp.append(n)
                arr[i+n] = temp
    return arr[targetSum]
                

if __name__=="__main__":
    print("targetSum:7, Array:[2,3]", bestSum(7, [2,3]))
    print("targetSum:7, Array:[5,3,4,7]", bestSum(7, [5,3,4,7]))
    print("targetSum:7, Array:[2,4]", bestSum(7, [2,4]))
    print("targetSum:8, Array:[2,3,5]", bestSum(8, [2,3,5]))
    print("targetSum:300, Array:[7,14]", bestSum(300, [7,14]))