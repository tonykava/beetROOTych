class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'a') as f:
            f.write(self.msg)


password = input('Enter your password here: ')

if len(password) < 10:
    raise CustomException('Your password is too short\n')
if len(password) > 20:
    raise CustomException('Your password is too long\n')

