def full_name():
    fname = input('Give me name: ')
    lname = input('Give me last name: ')
    return 'Hello {} {}'.format(fname, lname)


def pr1nt():
    return full_name()

print(pr1nt())


