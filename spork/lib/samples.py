
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case


def is_not_palindrome(string):
    reversed_string = ""
    for i in range(len(string)):
        rev_i = -(1 + i)
        reversed_string += string[rev_i]

    return string != reversed_string


def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero!"
    else:
        return "Invalid operation."


def fibonacci_dp(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Create a table to store Fibonacci numbers
    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    # Fill the table iteratively
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]


def is_palindrome(string):
    return string == string[::-1]
