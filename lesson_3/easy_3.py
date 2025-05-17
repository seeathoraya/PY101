# Question 1

numbers = [1, 2, 3, 4]
numbers.clear() 
print(numbers) # or:

while numbers:
    numbers.pop()


# Question 2
# [1, 2, 3, 4, 5]


# Question 3
# "hello there"


# Question 4
# "[{"first": 42}, {"second": "value2"}, 3, 4, 5]""


# Question 5
def is_color_valid(color):
    return (color == "blue" or color == "green")

    # or:
    return color in ["blue", "green"]
