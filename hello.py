# for i in range(10):
#     print('looping ..', i)

# favorites = ['pizza', 'pasta', 'ice cream', 'chocolate', 'sushi']

# for idx, item in enumerate(favorites):
#     print(idx, item)

# count = 0

# while count < len(favorites):
#     print('i like this food', favorites[count])
#     count += 1

# bill = 100
# tax_rate = 15
# total_tax = bill * tax_rate / 100
# print('Total tax', total_tax)

def calculate_tax(bill, tax_rate):
    return bill * tax_rate / 100
    