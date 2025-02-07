def factorial(n):
    """

    real fact.
    dev added
    
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n < 0:
        return "Invalid input. Please enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Input from user
number = int(input("Enter a number to calculate its factorial: "))

# display
result = factorial(number)
print(f"The factorial of {number} is: {result}")

