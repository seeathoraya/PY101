# Question 1
string = "-The Flinstones Rock!"

for i in range(0, 10):
    print(string)
    string = "-" + string


# Question 2

def factors(number):
    divisor = number
    result = []
    while divisor > 0: # only loop as long as the input is a positive number
        if number % divisor == 0: # check if the factor is a whole number
            result.append(number // divisor)
        divisor -= 1
    return result


# Question 3
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element) # appends the new element (mutates the list)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element] # concatenates the new element (creates a new list)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


# Question 4
"""
First: 0.9
Second: True
"""


# Question 5
nan_value = float("nan")

print(nan_value == float("nan")) # False

# Use math.isnan(nan_value)


# Question 6

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8) # 42 - 8 = 34


# Question 7
# No, because the dict in the function is shadowing the original
# Okay, yes. Because the function mutates the items in the dict


# Question 8

def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

print(
    rps(
        rps(
            rps("rock", "paper"), # paper
            rps("rock", "scissors") # rock
            ), # paper
        "rock")
    ) # paper <-- printed


# Question 9
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

bar(foo()) # False


# Question 10
# True