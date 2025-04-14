# EXAMPLE
""" 
——Casual——

Given a collection of numbers.
    Iterate through the collection one by one.
        save the first value as the starting value.
        for each iteration, compare the saved value with the current value.
            if the current number is greater
                reassign the saved value as the current value
            otherwise, if the current value smaller or equal
                move to the next value in the collection
    After iterating through the collection, return the saved value. 

——Formal——
START

# Given a collection of integers called "numbers"

SET iterator = 1
SET savedNumber = value within numbers collection at space 1

WHILE iterator <= length of numbers
    SET currentNumber = value within numbers collection at space "iterator"
    IF currentNumber > savedNumber
        savedNumber = currentNumber

    iterator = iterator + 1

PRINT savedNumber

——Python——
def find_greatest(numbers):
    iterator = 0
    saved_number = numbers[iterator]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number

        iterator += 1

    return saved_number
"""


# a function that returns the sum of two numbers
""" 
——Casual——

Given two numers
    return the first number + the second number

——Formal——
START

# Given two arguments of integers, num1 and num2

return num1 + num2

END
"""


# a function that takes a list of strings, and returns a string 
# that is all those strings concatenated together
""" 
——Casual——
Given a list of strings
    create an empty string to hold the concatenated values
    iterate through each item in the list
        for each item, add the string to the concatenation string
    After iterating, return the concatenated string

——Formal——
START

# Given a list of strings called "strings"

SET concat_string = ""
SET index = 0

WHILE index < lengt of strings
    SET current_string = value of "strings" collection at space of "index"
    SET concat_string = concat_string + current_string
    SET index = index + 1

PRINT concat_string

END
"""


# a function that takes a list of integers, 
# and returns a new list with every other element 
# from the original list, starting with the first element.
"""
——Casual——
Given a list of integers
    create a new empty list
    create a index starting at 0
    iterate through the integers, starting with the first one
        for each iteration, append the integer to the empty list
        increase the index by two

——Formal——
START

# Given a list of integers called "integers"

SET extracted_numbers = empty list
SET index = 0

WHILE index < length of integers
    append value of integers at space of index to extracted_numbers
    index = index + 2

return extracted_numbers

END
"""



# a function that determines the index of the 3rd occurrence 
# of a given character in a string. For instance, if the given 
# character is 'x' and the string is 'axbxcdxex', the function 
# should return 6 (the index of the 3rd 'x'). If the given 
# character does not occur at least 3 times, return None.
""" 
——Casual——
Given a string and a character
    iterate over each character in the string
        evaluate if the character is equal to the given character
            if it is, increment a counter by 1 and set store its position in the index
                if the counter is equal to 3, return the position
            else, continue with the next character
        if the counter is not 3, return none

——Formal——
START

# Given two string arguments: a string and a single character

SET index = 0
SET count = 0

WHILE index < length of string
    IF character == string at current index
        SET count = count + 1
        SET position = index
        IF count == 3
            PRINT position
            END
    SET index = index + 1

IF count < 3
    PRINT None

END
""" 


# a function that takes two lists of numbers and returns the result 
# of merging the lists. The elements of the first list should become 
# the elements at the even indexes of the returned list, while the 
# elements of the second list should become the elements at the odd indexes. 
"""
——Casual——
Given two lists of numbers
    create an empty list
    iterate over the list length (equal length so any of the two is fine)
        append the number at the current index from list 1 to the empty list
        append the number at the current index from list 2 to the empty list
    return the new list

——Formal——
START

# Given two arguments with lists of numbers (list1, list2), 
# both with the same length

SET merged_list =[]
SET index = 0

WHILE index < length of first list
    append number at current index of list1 to merged_list
    append number at current index of list2 to merged_list
    SET index = index + 1

PRINT merged_list
END
"""