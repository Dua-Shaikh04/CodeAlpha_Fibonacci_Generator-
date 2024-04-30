def fibonacci(num):
    if num<= 0:
        return "Invalid input"
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)#recurcive function

# Function call to generate Fibonacci series up to the nth term
def generate_fibonacci_series(n):
    fibonacci_series = []#here we create empty array where we store series
    for i in range(1, n + 1):
        fibonacci_series.append(fibonacci(i))#append is used to add or put things in a list
    return fibonacci_series

# Example: Generating Fibonacci series up to the 10th term
print(generate_fibonacci_series(10))