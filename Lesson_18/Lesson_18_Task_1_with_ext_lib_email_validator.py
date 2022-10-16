from email_validator import validate_email, EmailNotValidError

class Validate:
    def __init__(self, email):
        self.email = email
        self.validate(self.email)

    def validate(self, email):
        try:
            v = validate_email(email)
            email = v["email"]
            print("True")
        except EmailNotValidError as e:
            print(str(e))

#invalid mails:
Validate('abc-@mail.com')
Validate('abc..def@mail.com')
Validate('.abc@mail.com')
Validate('abc#def@mail.com')
print('-----------------------------------')
#valid mails:
Validate('abc-d@mail.com')
Validate('abc.def@mail.com')
Validate('abc@mail.com')
Validate('abc_def@mail.com')
print('-----------------------------------')
#invalid mails:
Validate('abc.def@mail.c')
Validate('abc.def@mail#archive.com')
Validate('abc.def@mail')
Validate('abc.def@mail..com')
print('-----------------------------------')
#valid mails:
Validate('abc.def@mail.cc')
Validate('abc.def@mail-archive.com')
Validate('abc.def@mail.org')
Validate('abc.def@mail.com')