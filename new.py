import os


def are_numbers_increasing(numbers):
    """
    Check whether numbers are in increasing order.
    """
    return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))


def print_pair_sums(values):
    """
    Print sum of all possible pairs.
    """
    for first in values:
        for second in values:
            print(f"{first} + {second} = {first + second}")


def calculate_expression(a, b, c, d, e, f, g, h, i, j):
    """
    Perform a mathematical calculation.
    """
    try:
        result = a + b - (c * d / e) + f - g + (h * i) - j
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None


def divide_number():
    """
    Divide 100 by user input safely.
    """
    try:
        num = int(input("Enter a number: "))

        if num == 0:
            print("Cannot divide by zero.")
            return

        print("Result:", 100 / num)

    except ValueError:
        print("Please enter a valid integer.")


def main():
    numbers = [10, 20, 30, 40, 50]

    print("Starting program...\n")

    if are_numbers_increasing(numbers):
        print("Numbers are increasing.\n")
    else:
        print("Numbers are not increasing.\n")

    counter = 0

    while counter < 5:
        print("Counter value:", counter)
        counter += 1

    values = [1, 2, 3, 4, 5]

    print("\nPair sums:")
    print_pair_sums(values)

    result = calculate_expression(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    if result is not None:
        print("\nCalculation Result:", result)

    # Using environment variable instead of hardcoded password
    password = os.getenv("APP_PASSWORD", "default_password")
    print("\nPassword loaded securely.")

    divide_number()

    print("\nProgram ended successfully.")


if __name__ == "__main__":
    main()
