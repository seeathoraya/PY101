# Question 1
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# The second function would return none because the value to return is on a separate line


# Question 2

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary) # {'first': [1, 2]}  because the value that the key is pointing to is mutated 


# Question 3
# A) reassigns variables but the variables are shadowing the original ones. 
# Thus, the print function in the end outputs the original values.

def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

"""
one is: ["one"]
two is: ["two"]
three is: ["three"]
"""

# B) Returns an error because it cannot assign to literal.
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

"""
one is: "two"
two is: "three"
three is: "two"
"""

# C) Can't mutate strings.


# Question 4
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

ip_address = input()
print(is_dot_separated_ip_address(ip_address))


# Question 5
# It would raise a name error since the variable is not defined (because the assignment is not executed)