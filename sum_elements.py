# A refactored example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles basic error cases.

MAX = 100

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def get_integer_input(prompt, error_message="Invalid input. Please enter a valid integer."):
    """Prompt the user for an integer input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)

def get_numbers(count):
    """Prompt the user to input a specified number of integers."""
    numbers = []
    print(f"Enter {count} integers:")
    for _ in range(count):
        number = get_integer_input("> ")
        numbers.append(number)
    return numbers

def main():
    """Main function to execute the program."""
    try:
        n = get_integer_input("Enter the number of elements (1-100): ", 
                              "Invalid input. Please enter a valid integer.")
        if not 1 <= n <= MAX:
            print(f"Invalid input. Please provide a number between 1 and {MAX}.")
            return

        numbers = get_numbers(n)
        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
