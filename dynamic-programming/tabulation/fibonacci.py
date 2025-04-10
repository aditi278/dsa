def fib(n):
    arr = [0]*(n+2)
    arr[1] = 1
    for i in range(n):
        arr[i+1]+=arr[i]
        arr[i+2]+=arr[i]
    return arr[n]

if __name__ == "__main__":
    print("Fib 2", fib(2))
    print("Fib 5", fib(5))
    print("Fib 7", fib(7))
    print("Fib 50", fib(50))