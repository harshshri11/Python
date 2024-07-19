def calculate(num1, num2, operation):
    match operation:
        case '+':
            result = num1 + num2
            return result
        case '-':
            result = num1 - num2
            return result
        case '/':
            result = num1 / num2
            return result
        case _:
            result = "invalid operation"
            return result

while True:
    print("operation")
    print("enter '+' for addition")
    print("enter '-'for substarcation")
    print("enter '/' for division")
    print("enter'exit' for end the program")
    user_input = input(":")
    if user_input == 'exit':
        break
    if user_input in ('+','-','/'):
        num1 = float(input("enter the first number:"))
        num2 = float(input("enter the second number:"))
        result = calculate(user_input,num1,num2)
        print("result",result)
    else:
        print("invalid input. please try again.")



