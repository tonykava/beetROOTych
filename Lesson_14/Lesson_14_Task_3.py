def validate(l, n):
    for i in l:
        if i in n:
            return True
    return False

def arg_rules(type_, max_length, contains):
    def decorator(fcn):
        def wrapper(name):
            if isinstance(name, type_) and len(name) <= max_length and validate(contains, name) == True:
                return fcn(name)
            else:
                raise Exception('ERROR')
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['@', '05'])
def create_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'


print(create_slogan('Yura'))