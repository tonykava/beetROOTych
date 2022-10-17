class uc_getitem():
    def __init__(self, text):
        self.text = text.upper()
    def __getitem__(self, index):
        return self.text[index]

for i in uc_getitem('abcde'):
    print(i)


print(uc_getitem('abcde')[3].lower())






