nums = []

def add(nums_list):
    result = 0
    for num in nums_list:
        result += num
    return result

def subtract(nums_list):
    result = nums_list[0]
    nums_list.pop(0)
    for num in nums_list:
        result -= num
    return result

def multiply(nums_list):
    result = nums_list[0]
    nums_list.pop(0)
    for num in nums_list:
        result *= num
    return result

def divide(nums_list):
    result = nums_list[0]
    nums_list.pop(0)
    for num in nums_list:
        result /= num
    return result

print("Calculator - 1.0")
while True:
    nums_amount = int(input("How many numbers?"))
    for num in range(nums_amount):
        number = int(input("Insert Number:"))
        nums.append(number)
    operator = input("Insert function (+, -, *, /): ")
    if operator == "+":
        print(add(nums))
    elif operator == "-":
        print(subtract(nums))
    elif operator == "*":
        print(multiply(nums))
    elif operator == "/":
        print(divide(nums))
    else:
        print("Unknown operator!")