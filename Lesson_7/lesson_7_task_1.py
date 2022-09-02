s = 'Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.'
s = s.split(' ')
print({i: s.count(i) for i in s})
