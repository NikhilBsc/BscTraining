Day 1 : 26 - 06 -2026

## List comprehention example:
# ex 1:
Traditional approach:

Two nested for loops are used to create all possible (i, j) pairs. Each pair is added to the list using append().

List Comprehension:

The same logic is written in a single line using list comprehension. It produces the same output with less code.

# ex 2:

Traditional Approach:

The outer loop selects even values of i, and the inner loop selects odd values of j. The valid pairs are then added to the list.

List Comprehension:

The same conditions and loops are combined into a single expression, making the code shorter while producing the same result.

## 2nd Task

# Dictionary Comprehension with Nested Loops
Traditional Approach:

Two nested for loops are used to create key-value pairs. The tuple (i, j) is used as the key, and the product i * j is stored as its value.

Dictionary Comprehension:

The same logic is written in a single line using dictionary comprehension.itgi creates the same dictionary in a more  readable way.

## 3rd Task

# Generator Function using yield
ex 1:

This generator produces even numbers one at a time using the yield keyword unlike a normal function, calling even_num() does not execute the function immediately. Instead, it returns a generator object, and each value is generated only when the for loop requests the next one.

ex 2:

This example uses a generator to return product names one by one. The products() function creates a generator object, and each product is yielded only when it is needed. This approach is memory-efficient because it doesn't store all the values at once.
