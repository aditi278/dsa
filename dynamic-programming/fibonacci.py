def fib(n, memo={}):
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

if __name__ == "__main__":
    print("Fib 2", fib(2))
    print("Fib 5", fib(5))
    print("Fib 7", fib(7))
    print("Fib 10", fib(10))
