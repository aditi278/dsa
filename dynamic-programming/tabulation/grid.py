def grid(m, n):
    table = [[0]*(n+1) for i in range(m+1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            if i+1 <= m:
                table[i+1][j] += table[i][j]
            if j+1 <= n:
                table[i][j+1] += table[i][j]
    return table[m][n]

if __name__ == "__main__":
    print("Grid 1,1", grid(1,1))
    print("Grid 2,3", grid(2,3))
    print("Grid 18,18", grid(18,18))