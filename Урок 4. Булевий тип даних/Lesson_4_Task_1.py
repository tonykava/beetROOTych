a = input('Enter ur string right here: ')
if len(a) <= 1:
    print('')
else:
    print(a[:2:] + a[-2::])
