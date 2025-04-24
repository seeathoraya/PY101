import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)


LANGUAGE = 'sv'


def prompt(key):
    intl_message = messages(key, LANGUAGE)
    print(f"==> {intl_message}")


def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False


def messages(message, lang):
    return MESSAGES[lang][message]


def run_calculation():
    # 1. Ask for the first number
    prompt("first_number")
    number1 = input()

    while invalid_number(number1):
        prompt("invalid_number")
        number1 = input()

    # 2. Ask for the second number
    prompt("second_number")
    number2 = input()

    while invalid_number(number2):
        prompt("invalid_number")
        number2 = input()

    print(f"==> {number1} & {number2}")

    # 3. Ask which operation to perform
    prompt("operations_options")
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt("invalid_operation")
        operation = input()

    # 4. Carry out calculation
    match operation:
        case "1":  # 1 is addition
            result = float(number1) + float(number2)
        case "2":  # 2 is subtraction
            result = float(number1) - float(number2)
        case "3":  # 3 is multiplication
            result = float(number1) * float(number2)
        case "4":  # 4 is division
            result = float(number1) / float(number2)

    # 5. Print the result
    prompt("result")
    print(f"==> {result}")


prompt("welcome")

while True:
    run_calculation()
    prompt("run_again")
    answer = input()

    while answer not in ["y", "n"]:
        prompt("invalid_answer")
        answer = input()

    if answer == "n":
        break
