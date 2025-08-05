

print("Welcome to my First github repo ever which is personally been used and being used by me ")
print("hello sita")


#### these are the answers for lists.md

# 1. Create a list with mixed elements
my_list = [10, "chemistry", 3.14, 42, "mathematics", 5.67]

# 2. Access and print the 2nd and 5th elements (Python uses 0-based indexing)
print("2nd element:", my_list[1])   # Output: "hello" (index 1 is the 2nd element)
print("5th element:", my_list[4])   # Output: "world" (index 4 is the 5th element)

# 3. Slice middle 3 elements (indices 1 to 4, excluding 4)
middle_sublist = my_list[1:4]
print("Middle 3 elements:", middle_sublist)  # Output:[chemistry,3.14,42]

#4. Reversed the list
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list) # Output:[5.67, 'mathematics', 42, 3.14, 'chemistry', 10]

#5.Append the word sai srivatsa in to the list
my_list.append("sai srivatsa")
print("After append:", my_list)# Output:[10, 'chemistry', 3.14, 42, 'mathematics', 5.67, 'sai srivatsa']

#6. insert the word bharatula to the list
my_list.insert(1, "bharatula")
print("After insert:", my_list) # output: [10, 'bharatula', 'chemistry', 3.14, 42, 'mathematics', 5.67, 'sai srivatsa']

#7.remove the element  3.14 from the list and then the last element from the list also pop up the remaining list
my_list.remove(3.14)
print("After remove:", my_list) # Output:[10, 'bharatula', 'chemistry', 42, 'mathematics', 5.67, 'sai srivatsa']
last_element = my_list.pop()
print("Removed last element:", last_element)
print("After pop:", my_list)  #output:[10, 'bharatula', 'chemistry', 42, 'mathematics', 5.67]


#8.1.a.Created a new list sorted
my_numbers = [5, 2, 9, 1, 5.67, 3.14, 42]
my_numbers.sort()  # Sorts the list in-place (modifies original)
print("Sorted (ascending):", my_numbers)

#8.1.b.Alternative
sorted_my_numbers = sorted(my_numbers)
print("New sorted list:", sorted_my_numbers)
print("Original list (unchanged):", my_numbers)

#8.2.a.Reverse the Sorted List
my_numbers.reverse()  # Reverses the list in-place
print("Reversed sorted list:", my_numbers)

#8.2.b.Using Slicing (Creates a New List)
reversed_my_numbers = my_numbers[::-1]  # Returns a reversed copy
print("Reversed (slicing):", reversed_my_numbers)

### lets stick to the same list
my_numbers = [5, 2, 9, 1, 5.67, 3.14, 42]

 #9.1Count Occurrences of a Specific Item
count_5 = my_numbers.count(5)
print("Number of times 5 appears:", count_5)

#9.1.a Example with Non-Existent Item
count_99 = my_numbers.count(99)
print("Number of times 99 appears:", count_99)  # Output: 0

 #9.2Find Index of First Occurrence

index_5_67 = my_numbers.index(5.67)
print("Index of 5.67:", index_5_67)

#9.2.a.Handling Missing Items
item = 99
if item in my_numbers:
    print("Index of 99:", my_numbers.index(item))
else:
    print(f"{item} not in the list")  # Output: "99 not in the list"


#10.extend vs append
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

#10.1 using append
list1.append(list2)
print("After append:", list1)

 #10.2 using extend
list1 = [1, 2, 3]  # Resetting list1
list1.extend(list2)
print("After extend:", list1)
### please note
##When to Use Which:
##Use append() when you want to add a single element (even if that element is a list)
##Use extend() when you want to combine two lists into one flat list

#11.7. List Comprehension
#11.7.1.Use list comprehension to create a list of squares from 1 to 10.

squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

#11.7.2.Use list comprehension to filter out odd numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print("Even numbers only:", evens)

#12.1.Copying Lists - Shallow Copy with copy()
original = [1, 2, 3, ["a", "b"]]  # Contains a nested list
shallow_copy = original.copy()     # Creates a shallow copy

print("Original:", original)
print("Shallow Copy:", shallow_copy)

#12.2.Modify the Shallow Copy
##Case 1: Change a Top-Level Element
###Modifying a non-nested element in the copy does not affect the original:

shallow_copy[0] = 99  # Change first element

print("\nAfter modifying top-level element:")
print("Original:", original)       # Unchanged
print("Shallow Copy:", shallow_copy)

#Case 2: Modify the Nested List
#Since the nested list is shared, changes to it affect both lists:

shallow_copy[3].append("c")  # Modify nested list
print("\nAfter modifying nested list:")
print("Original:", original)  # Nested list changed!
print("Shallow Copy:", shallow_copy)

#13. Nested Lists - 2D Matrix Operations
#1. Create a 3x3 Matrix (List of Lists)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original Matrix:")
for row in matrix:
    print(row)

#2. Access the Middle Element

middle = matrix[1][1]
print("\nMiddle Element:", middle)  # Output: 5

#3. Change the Bottom-Right Element
matrix[2][2] = 99  # Change value from 9 to 99
print("\nModified Matrix:")
for row in matrix:
    print(row)

#14.Looping Through Lists
#1.Print Each Item with Its Index

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

#2. Sum All Numeric Values in a List
mixed_list = [10, "hello", 3.14, 42, "world", 5.67]
total = 0

for item in mixed_list:
    if isinstance(item, (int, float)):  # Check if item is numeric
        total += item

print("Sum of numeric values:", total)  # Output: 60.81 (10 + 3.14 + 42 + 5.67)









###these are the answers for tuples.md
#1. Create and Index

# Create a tuple with 5 elements of different types
mixed_tuple = (42, "Hello", 3.14, True, [1, 2, 3])

# Print the 3rd element (index 2 since tuples are 0-based)
print("3rd element:", mixed_tuple[2])  # Output: 3.14

#2. Tuple Unpacking
# Person tuple (name, age, profession)
person = ("Alice", 30, "Engineer")

# Unpack into individual variables
name, age, profession = person

print(f"Name: {name}, Age: {age}, Profession: {profession}")
# Output: Name: Alice, Age: 30, Profession: Engineer

#3.Count and Index
numbers = (10, 20, 30, 20, 40, 20)

# Count occurrences of 20
count_20 = numbers.count(20)
print("Count of 20:", count_20)  # Output: 3

# Find first index of 20
index_20 = numbers.index(20)
print("First index of 20:", index_20)  # Output: 1

#4.Tuple Immutability Check
immutable_tuple = (1, 2, 3)

try:
    immutable_tuple[1] = 99  # Attempt modification
except TypeError as e:
    print("Error:", e)  # Output: Error: 'tuple' object does not support item assignment

#5.Dictionary key with tuple
# Dictionary with (lat, long) keys
cities = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

# Retrieve city by coordinates
ny_coords = (40.7128, -74.0060)
print("City:", cities[ny_coords])  # Output: City: New York

#6.Functioning return tuple
def stats(numbers):
    """Returns (min, max, avg) of a list."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Call function and unpack
data = [4, 2, 9, 5]
min_val, max_val, avg_val = stats(data)
print(f"Min: {min_val}, Max: {max_val}, Avg: {avg_val:.2f}")
# Output: Min: 2, Max: 9, Avg: 5.00

#7.Nested tuple access
# 3-level nested tuple
nested = (("a", "b"), (1, (2.5, ("deep", "value"))), True)

# Access "value" (path: nested[1][1][1][1])
deep_value = nested[1][1][1][1]
print("Deep value:", deep_value)  # Output: Deep value: value


