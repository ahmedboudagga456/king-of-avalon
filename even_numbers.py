# Different ways to print even numbers

# Method 1: Print even numbers in a range
print("Even numbers from 0 to 20:")
for i in range(0, 21, 2):  # Start at 0, go to 20, step by 2
    print(i)

print("\n" + "="*30 + "\n")

# Method 2: Check if numbers are even in a range
print("Even numbers from 0 to 20 (using condition):")
for i in range(0, 21):
    if i % 2 == 0:  # Check if number is divisible by 2
        print(i)

print("\n" + "="*30 + "\n")

# Method 3: Print even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Even numbers from a list:")
for num in numbers:
    if num % 2 == 0:
        print(num)

print("\n" + "="*30 + "\n")

# Method 4: Using list comprehension to create and print even numbers
print("Even numbers from 0 to 20 (using list comprehension):")
even_numbers = [i for i in range(0, 21) if i % 2 == 0]
for num in even_numbers:
    print(num)

print("\n" + "="*30 + "\n")

# Method 5: Function to print even numbers from any list
def print_even_numbers(numbers_list):
    """Print only the even numbers from a list"""
    print("Even numbers from the provided list:")
    for num in numbers_list:
        if num % 2 == 0:
            print(num)

# Example usage
sample_numbers = [15, 22, 7, 18, 33, 40, 51, 64, 77, 82]
print_even_numbers(sample_numbers)