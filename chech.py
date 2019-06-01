import csv

all_cities =[]
all_removed_cities = []

with open('city.csv', 'r', encoding='Windows 1251') as c:
    fields = ['city_id', 'country_id', 'region_id', 'name']
    reader = csv.DictReader(c, fields, delimiter=';')
    for row in reader:
        if row['name'] not in all_cities:
            all_cities.append(row['name'])
        else:
            continue
            

def cities(user_answer):
    if user_answer in all_cities:
        for n_city in all_cities:
            if user_answer[-2:] == 'ый':
                if n_city[0] == user_answer[-3].upper():
                    all_removed_cities.append(n_city)
                    all_removed_cities.append(user_answer)
                    all_cities.remove(n_city)
                    all_cities.remove(user_answer)
                    return(n_city)
            elif user_answer[-1] == 'ь' or user_answer[-1] == 'ъ' or user_answer[-1] == 'ы' or user_answer[-1] == 'й':
                if n_city[0] == user_answer[-2].upper():
                    all_removed_cities.append(n_city)
                    all_removed_cities.append(user_answer)
                    all_cities.remove(n_city)
                    all_cities.remove(user_answer)
                    return(n_city)
            else:
                if n_city[0] == user_answer[-1].upper():
                    all_removed_cities.append(n_city)
                    all_removed_cities.append(user_answer)
                    all_cities.remove(n_city)
                    all_cities.remove(user_answer)
                    return(n_city)
                else:
                    continue
    elif user_answer in all_removed_cities:
        return('Такой город уже был. Введите другое название')
    else:
        return('Допущена ошибка в названии. Повторите ввод')
                     

while True:
    user_input = (input('Введите город: ')).strip().capitalize()
    print(cities(user_input))