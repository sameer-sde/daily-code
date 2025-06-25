import random

def generate_random_numbers(count=20, start=1, end=100):
    """Generates a list of random integers."""
    return [random.randint(start, end) for _ in range(count)]

def sort_numbers(numbers):
    """Sorts the list of numbers in ascending order."""
    return sorted(numbers)

def display_stats(numbers):
    """Displays basic statistics about the number list."""
    print(f"Total numbers: {len(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Average: {sum(numbers)/len(numbers):.2f}")

if __name__ == "__main__":
    print("Generating random numbers...")
    nums = generate_random_numbers()
    print("Original List:")
    print(nums)

    print("\nSorted List:")
    sorted_nums = sort_numbers(nums)
    print(sorted_nums)

    print("\nStatistics:")
    display_stats(nums)
