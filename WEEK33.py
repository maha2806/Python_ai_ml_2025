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

