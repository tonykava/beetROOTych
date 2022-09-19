
# path = 'D:\\TONY\\PYT\\text.txt' - Якщо файл лежить не в одній директорії з виконуваним файлом
path = 'text.txt'
def count_lines(path):
    with open(path, 'rt') as file:
        number_of_lines_in_a_file = sum(1 for line in file)
        return 'Number of lines in a file: {}'.format(number_of_lines_in_a_file)

def count_chars(path):
    with open(path, 'rt') as file:
        text = file.read()
        return 'Number of characters in a text: {}'.format(len(text))

def test(path):
    print(count_lines(path))
    print(count_chars(path))
    return ''

def main():
    print(test(path))

if __name__ == '__main__':
    main()








