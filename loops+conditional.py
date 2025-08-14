# Assignment — Loops + Conditional Statements

# 1. Print numbers 1-20, labeling even/odd
print("\n1. Even/Odd numbers from 1 to 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(f"{num}: Even")
    else:
        print(f"{num}: Odd")

# 2. Print names starting with "A"
names = ["Alice", "Bob", "Anna", "Charlie", "Alex", "David"]
print("\n2. Names starting with 'A':")
for name in names:
    if name.startswith('A'):
        print(name)

# 3. FizzBuzz for numbers 1-50
print("\n3. FizzBuzz for numbers 1-50:")
for num in range(1, 51):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 4. Print students with marks > 75
students = {"John": 82, "Emma": 75, "Michael": 90, "Sophia": 68}
print("\n4. Students with marks > 75:")
for name, mark in students.items():
    if mark > 75:
        print(name)

# 5. Print prime numbers between 1-30
print("\n5. Prime numbers between 1-30:")
for num in range(2, 31):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# 6. Print words with length > 5
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
print("\n6. Words with length > 5:")
for word in words:
    if len(word) > 5:
        print(word)

# 7. Multiplication table (1-5) skipping results > 15
print("\n7. Multiplication table (1-5), skipping results > 15:")
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        if product <= 15:
            print(f"{i} x {j} = {product}")
        else:
            continue  # This line is optional as the loop would continue anyway
