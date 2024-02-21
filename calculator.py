def add(x, y):
    return x + y 

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print('Select an operator\n1) +\n2) -\n3) *\n4) /')
    operator_choice = input('Enter choice here (number): ')
    print('----------------------------------')

    if operator_choice in ('1', '2', '3', '4'):
        try:
            num_1 = float(input('Enter the first number here: '))
            num_2 = float(input('Enter the second number here: '))
        except ValueError:
            print('Invalid input, enter a number.')
            continue

        if operator_choice == '1':
            print(num_1, '+', num_2, '=', add(num_1, num_2))
            print('----------------------------------')
        elif operator_choice == '2':
            print(num_1, '-', num_2, '=', subtract(num_1, num_2))
            print('----------------------------------')
        elif operator_choice == '3':
            print(num_1, '*', num_2, '=', multiply(num_1, num_2))
            print('----------------------------------')
        elif operator_choice == '4':
            print(num_1, '/', num_2, '=', divide(num_1, num_2))
            print('----------------------------------')

        carry_on = input('Enter [c] to go again or [q] to quit: ')
        if carry_on == 'q':
            quit()
    else:
        print('Invalid input')
