def if_palindrome(looking_str: str):
    if looking_str != '':
        if looking_str[0] != looking_str[-1]:
            return False
        else:
            return if_palindrome(looking_str[1:-1])
    else:
        return True

if __name__ == "__main__":
    print(if_palindrome('sasas'))
    print(if_palindrome('kook'))
    print(if_palindrome('sos'))
    print(if_palindrome('o'))


