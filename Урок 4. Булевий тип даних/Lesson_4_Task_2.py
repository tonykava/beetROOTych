phone_number = input('Enter your phone number here: ')
if phone_number.isnumeric() and len(phone_number) == 10:
    print('Valid number')
if not phone_number.isnumeric():
    print('Not a phone number. Phone number contain numbers only')
if len(phone_number) != 10:
    print('Phone number must contain 10 numbers')






