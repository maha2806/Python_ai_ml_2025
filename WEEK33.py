# Assignment — Conditional Statements (No Loops)
# 1. Simple `if`
# Store age and check if adult
age = 20  # Change this value to test different cases
if age >= 18:
    print("Adult")  # This will print if age is 18 or more

# 2. `if...else`
# Check bank balance status
bank_balance = 750  # Change this value to test different cases
if bank_balance > 1000:
    print("Sufficient funds")  # Prints if balance > 1000
else:
    print("Low balance")  # Prints otherwise

# 3. `if...elif...else`
# Check if number is positive, zero or negative
number = -5  # Change this value to test different cases
if number > 0:
    print("Positive")  # Prints if number > 0
elif number == 0:
    print("Zero")  # Prints if number == 0
else:
    print("Negative")  # Prints if number < 0

# 4. Nested `if`
# Check driving eligibility
age = 19  # Change this value to test different cases
has_license = True  # Change this to ,False to test
if age >= 18:
    if has_license:  # This only checks if age >= 18

        print("Can drive")  # Prints only if both conditions are True

# 5. Ternary Operator
# Check pass/fail status
score = 65  # Change this value to test different cases
result = "Pass" if score >= 50 else "Fail"  # Ternary operation
print(result)  # Prints "Pass" if score >=50, else "Fail"

# 6. `and` / `or`
# Check if it's a day off
is_weekend = True  # Change this to , False to test
is_holiday = False  # Change this to True to test
if is_weekend or is_holiday:  # Using 'or' operator
    print("Day off")  # Prints if either condition is True

# 7. `in` / `not in`
# Check color availability
colors = ["red", "blue", "yellow"]  # Modify list to test different cases
if "red" in colors:
    print("Red available")  # Prints if "red" is in the list
if "green" not in colors:
    print("Green not available")  # Prints if "green" is not in the list

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
