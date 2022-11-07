def sum_of_digits(digit_str: str):
    if not digit_str.isdigit():
        raise ValueError('input string must be digit string')
    if digit_str != '':
        return int(digit_str[0]) + int(digit_str.replace(digit_str[0], '', 1))
    else:
        return 0

if __name__ == "__main__":
    print(sum_of_digits('26'))
    print(sum_of_digits('test'))
    

