def reverse(input_str: str):
    if input_str != '':
        return input_str[-1] + reverse(input_str.replace(input_str[-1], '', 1))
    else:
        return ''

if __name__ == '__main__':
    print(reverse('hello'))
    print(reverse('o'))


