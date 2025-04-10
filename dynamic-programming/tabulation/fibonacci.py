def fib(n):
    arr = []*(n+1)
    arr[1] = 1
    for i in range(n):
        arr[i+1]+=a[i]
        arr[i+2]+=a[i]
    return arr[n]


if __name__ == "__main__":
    print("Fib 2", fib(2))
    print("Fib 5", fib(5))
    print("Fib 7", fib(7))
    print("Fib 50", fib(50))