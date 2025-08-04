calc_mode = input('Enter operation(+,-,*,/) or fahrenheit value : ')
num1 = float(input('Enter first number: '))
if calc_mode.lower() == 'fahrenheit':
    print(f'{num1} Celsius is equals to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if calc_mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif calc_mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif calc_mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif calc_mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Please enter a valid operation!')