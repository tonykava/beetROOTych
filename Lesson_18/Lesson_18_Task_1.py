from itertools import product

class Validate:
    def __init__(self, email):
        self.email = email
        print(self.validate(self.email))

    def validate(self, email):
        if self.email.count('@') != 1:
            return False

        prefix = self.email.split('@')[0]
        domain = self.email.split('@')[-1]

        #prefix validation
        if not prefix[0].isalnum() or not prefix[-1].isalnum():
            return False
        for i in prefix:
            if not i.isalnum() and i not in '-_.':
                return False
        for i in [''.join(i) for i in list(product('-_.', repeat=2))]:
            if i in prefix:
                return False

        #domain validation
        if domain.count('.') != 1:
            return False

        first_portion_of_domain = domain.split('.')[0]
        second_portion_of_domain = domain.split('.')[-1]

        for i in first_portion_of_domain:
            if not i.isalnum() and i != '-':
                return False
        if not second_portion_of_domain.isalpha() or len(second_portion_of_domain) < 2:
            return False

        return True

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
