def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

if __name__ == "__main__":
    num = int(input("Enter how many Fibonacci numbers you want: "))
    series = fibonacci(num)
    print("Fibonacci series:", series)
