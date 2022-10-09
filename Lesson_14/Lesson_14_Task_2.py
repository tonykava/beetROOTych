def stop_words(words):
    def decorator(fnc):
        def wrapper(name):
            return ' '.join(['*' if i in words else i for i in fnc(name)[:-1:].split(' ')]) + '!'
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def slogan(name):
     return f'{name} drinks pepsi in his brand new BMW!'

print(slogan('Tony'))

