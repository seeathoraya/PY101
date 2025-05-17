# Question 1
'''
Yes it will raise an error because there is no item at index 5 (out of index range).
'''


# Question 2

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def ends_with_exclamation(string):
    return string[-1] == '!'


# Question 3

famous_words = "seven years ago..."

new_string_1 = "Four score and " + famous_words
new_string_2 = f"Four score and {famous_words}"


# Question 4

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'

print(munsters_description.capitalize())


# Question 5

munsters_description = "The Munsters are creepy and spooky."

print(munsters_description.swapcase())


# Question 6

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print("Dino" in str1)
print("Dino" in str2)


# Question 7

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")


# Question 8

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])


# Question 9

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

print(advice.split("house")[0])


# Question 10

advice = "Few things in life are as important as house training your pet dinosaur."

print(advice.replace("important", "urgent"))