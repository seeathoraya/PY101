def prompt(message):
    print(f"==> {message}")

prompt("Welcome to Calculator!")

# 1. Ask for the first number
prompt("What's the first number?")
number1 = input()

# 2. Ask for the second number
prompt("What's the second number?")
number2 = input()

prompt(f"{number1} & {number2}")

# 3. Ask which operation to perform
prompt("What operation would you like to perform?\n"
      "1) Add \n2) Subtract \n3) Multiply \n4) Divide")
operation = input()

# 4. Carry out calculation
match operation:
    case "1":  # 1 is addition
        result = int(number1) + int(number2)
    case "2":  # 2 is subtraction
        result = int(number1) - int(number2)
    case "3":  # 3 is multiplication
        result = int(number1) * int(number2)
    case "4":  # 4 is division
        result = int(number1) / int(number2)

# 5. Print the result
prompt(f"The result is: {result}")

