def get_non_negative_integer() -> int:
    """
    Prompts the user to enter a non-negative integer and validates the input.

    Returns:
        int: A validated non-negative integer.
    """
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number >= 0:
                return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of the given number.
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main():
    """
    Main function to get user input and compute the factorial.
    """
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")


if __name__ == "__main__":
    main()
