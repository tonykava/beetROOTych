import json

new_data = {
    "first_name": "",
    "last_name": "",
    "mobile": "",
    "city": "",
    "country": ""
}

file_name = 'data.json'

new_first_name = ''
new_last_name = ''
new_city = ''
new_country = ''

def print_contacts(data_list):
    for index, value in enumerate(data_list):
        name, familyname = tuple(value[0].split('__'))
        phone, city, country = tuple(value[1])
        print(f'Contact №{index + 1}:', f'First name: {name}, Last name: {familyname}, Phone: {phone}, City: {city}, Country: {country}')
        return f'Contact №{index + 1}:', f'First name: {name}, Last name: {familyname}, Phone: {phone}, City: {city}, Country: {country}'


def input_data():
    field_names = ["First name", "Last name", "Phone number", "City", "Country"]

    our_data = new_data.copy()
    for key, name in zip(our_data.keys(), field_names):
        our_data[key] = input(f'Enter {name}: ')
    return our_data


def create(data):
    with open(file_name, 'r') as json_file:
        result = json.load(json_file)
        result.update({f"{data['first_name']}__{data['last_name']}": [data['mobile'], data['city'], data['country']]})
    with open(file_name, 'w') as json_file:
        json.dump(result, json_file)


def search_first_name(name):
    with open(file_name, 'r') as json_file:
        result = json.load(json_file)

    list_of_contacts = []
    for key, value in result.items():
        if name in key.split('__')[0]:
            list_of_contacts.append((key, value))

    return print_contacts(list_of_contacts)


def search_last_name(name):
    with open(file_name, 'r') as json_file:
        result = json.load(json_file)

    list_of_contacts = []
    for key, value in result.items():
        if name in key.split('__')[1]:
            list_of_contacts.append((key, value))

    return print_contacts(list_of_contacts)


def search_full_name(name, familyname):
    with open(file_name, 'r') as json_file:
        result = json.load(json_file)

    list_of_contacts = []
    for key, value in result.items():
        if name + '__' + familyname == key:
            list_of_contacts.append((key, value))

    return print_contacts(list_of_contacts)


def search_mobile(mobile):
    with open(file_name, 'r') as json_file:
        result = json.load(json_file)

    list_of_contacts = []
    for key, value in result.items():
        if mobile in value[0]:
            list_of_contacts.append((key, value))

    return print_contacts(list_of_contacts)


def search_city(city):
    with open(file_name, 'r') as json_file:
        result = json.load(json_file)

    list_of_contacts = []
    for key, value in result.items():
        if city in value[1]:
            list_of_contacts.append((key, value))

    return print_contacts(list_of_contacts)


def search_country(country):
    with open(file_name, 'r') as json_file:
        result = json.load(json_file)

    list_of_contacts = []
    for key, value in result.items():
        if country in value[2]:
            list_of_contacts.append((key, value))

    return print_contacts(list_of_contacts)

def delete(mobile):
    search_mobile(mobile)
    command = input('Are u sure that u want do delete contact with this number?: (type Y or N): ').lower()
    if command == 'y':
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                if mobile in value[0]:
                    data.pop(key)
                    break
        with open(file_name, 'w') as out:
            json.dump(data, out)


def update(mobile):
    search_mobile(mobile)
    command = input('Are u sure that u want do update contact with this number?: (type Y or N): ').lower()
    global new_last_name
    global new_first_name
    global new_city
    global new_country
    if command == 'y':
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                if mobile in value[0]:
                    new_first_name = input('New first name: ')
                    new_last_name = input('New last name: ')
                    data[f"{new_first_name}__{new_last_name}"] = data.pop(key)
                    new_city = value[1] = input('New city: ')
                    new_country = value[2] = input('New country: ')
                    break
            with open(file_name, 'w') as out:
                json.dump(data, out)


def main():
    print('All available commands:', 'create', 'update', 'delete', 'search first name -> first',
          'search last name -> last', 'search full name -> full', 'search mobile -> mobile',
          'search city -> city', 'search country -> country', 'exit', sep='\n')
    while True:
        command = input('Please enter the command: ')
        if command.lower() == 'exit':
            break
        elif command.lower() == 'create':
            data = input_data()
            create(data)
        elif command.lower() == 'update':
            mobile = input('Enter mobile number: ')
            update(mobile)
        elif command.lower() == 'delete':
            mobile = input('Enter FULL mobile number: ')
            delete(mobile)
        elif command.lower() == 'first':
            name = input('Enter name: ')
            search_first_name(name)
        elif command.lower() == 'last':
            name = input('Enter familyname: ')
            search_last_name(name)
        elif command.lower() == 'full':
            name = input('Enter name: ')
            familyname = input('Enter familyname: ')
            search_full_name(name, familyname)
        elif command.lower() == 'mobile':
            mobile = input('Enter mobile: ')
            search_mobile(mobile)
        elif command.lower() == 'city':
            city = input('Enter city: ')
            search_city(city)
        elif command.lower() == 'country':
            country = input('Enter country: ')
            search_country(country)
        else:
            print('Choose command from list')


if __name__ == '__main__':
    main()
