def make_operation(*args):
    args = list(args)
    if args[0] == '+':
        return sum(args[1::])
    elif args[0] == '-':
        result = args[1]
        for i in args[2::]:
            result -= i
        return result
    elif args[0] == '*':
        result = args[1]
        for i in args[2::]:
            result *= i
        return result

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))

