import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)


def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def run_calculation():
    # 1. Ask for the first number
    prompt(data["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(data["invalid_number"])
        number1 = input()

    # 2. Ask for the second number
    prompt(data["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(data["invalid_number"])
        number2 = input()

    prompt(f"{number1} & {number2}")

    # 3. Ask which operation to perform
    prompt(data["operations_options"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(data["invalid_operation"])
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
    prompt(f"{data["result"]}{result}")

prompt(data["welcome"])

while True:
    run_calculation()
    prompt(data["run_again"])
    answer = input()

    while answer not in ["y", "n"]:
        prompt(data["invalid_answer"])
        answer = input()

    if answer == "n":
        break
