from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(int(fn(*args, **kwargs)))
        return wrapper

    @staticmethod
    def to_float(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(float(fn(*args, **kwargs)))
        return wrapper

    @staticmethod
    def to_str(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(' '.join(fn(*args, **kwargs)))
        return wrapper

    @staticmethod
    def to_bool(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(bool(fn(*args, **kwargs)))
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_float
def do_something(integer: int):
    return integer

@TypeDecorators.to_str
def comeon(l1st: list):
    return l1st

@TypeDecorators.to_bool
def booooooool(string: str):
    return string


do_nothing('23')
do_something(23)
comeon(['Ah', 'shit.', 'Here', 'we', 'go', 'again'])
booooooool(None)



