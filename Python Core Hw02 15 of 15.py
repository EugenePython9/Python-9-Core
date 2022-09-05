result = 0
operand = None
operator = None
wait_for_number = True

    
while True:
    if wait_for_number:
        try:
            operand = int(input('Input operand:'))

            if operator == None or operator == '+':
                result = result + operand
            elif operator == '-':
                result = result - operand
            elif operator == '*':
                result = result * operand
            elif operator == '/':
              try:
                result = result / operand
              except ZeroDivisionError:
                print('Can not Divide by Zero')
                continue
                    
        except ValueError:
            print('Not A Number')
            continue
    else:           
        operator = input('Input operator:')

        if operator == '+' or operator == '-' or operator == '*' or operator == '/':
            x = 1
        elif operator == '=':
                break
        else: 
                print('Wrong operator')
                continue

    wait_for_number = not wait_for_number
    print(result)

print(f"The result is: {result}")