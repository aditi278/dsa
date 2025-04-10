#number of ways to parse m*n grid from top left to bottom right
def grid(n, m, memo={}):
    key = str(n) + "," + str(m)
    if key in memo.keys():
        return memo[key]
    if n==1 and m==1:
        return 1
    if n==0 or m==0:
        return 0
    memo[key] = grid(n-1, m, memo) + grid(n, m-1, memo)
    return memo[key]

if __name__ == "__main__":
    print("Grid 1,1", grid(1,1))
    print("Grid 2,3", grid(2,3))
    print("Grid 18,18", grid(18,18))