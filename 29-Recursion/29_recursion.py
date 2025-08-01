# Factorial series 

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

# factorial(n) = n * factorial(n-1)
def factorial(n):
  if (n == 0 or n == 1):
    return 1
  else:
    return n * factorial(n - 1)


print(factorial(5))


# Fibonacci series

# f(n) = f(n-1) + f(n-2)
# it usually starts with 0 and 1.
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# the base cases return 1 and 0, and the results are summed back up the chain

# base case returns 1 for n=1, fib(1) = 1
# fib(2) = fib(1) + fib(0) = 1 + 0 = 1
# fib(3) = fib(2) + fib(1) = 1 + 1 = 2
# fib(4) = fib(3) + fib(2) = 2 + 1 = 3
# fib(5) = fib(4) + fib(3) = 3 + 2 = 5
# fib(6) = fib(5) + fib(4) = 5 + 3 = 8



def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


