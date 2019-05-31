def calculator(calc):
    element_list = []
    for user_input in calc:
        for elements in user_input:
            element_list.append(elements)
    
    try:
        try:
            if '/' in element_list:
                new_list = []
                numbers = calc.split('/')
                for e_number in numbers:
                    e_number = float(e_number)
                    new_list.append(e_number)
                    result = new_list[0] / new_list[1]
                    return(result)
        except ZeroDivisionError:
            return('Деление на 0 невозможно')
        if '+' in element_list:
            new_list = []
            numbers = calc.split('+')
            for e_number in numbers:
                e_number = float(e_number)
                new_list.append(e_number)
            return(sum(new_list))
        elif '*' in element_list:
            new_list = []
            numbers = calc.split('*')
            for e_number in numbers:
                e_number = float(e_number)
                new_list.append(e_number)
            result = new_list[0] * new_list[1]
            return(result)
        if '-' in element_list:
            new_list = []
            numbers = calc.split('-')
            for e_number in numbers:
                e_number = float(e_number)
                new_list.append(e_number)
            result = new_list[0] - new_list[1]
            return(result)
    except ValueError:
        print('Введите 2 числа')



print(calculator(input('Введите выражение: ')))


