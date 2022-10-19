class File:
    counter = 0

    @classmethod
    def get_counter(cls):
        return cls.counter

    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        File.counter += 1
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
        if type == FileExistsError:
            with open('logging.txt', 'a') as log:
                log.write(f'{type}\n')
        print(f'Counter: {self.counter}')
        return True

with File('text.txt', 'r') as f:
    print(f.read())



with File('text.txt', 'r') as f:
    print(f.read())
    raise FileExistsError

