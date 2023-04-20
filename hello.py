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

# def calculate_tax(bill, tax_rate):
#     return bill * tax_rate / 100
    
# print('Total tax', calculate_tax(1000, 8))

# def sum_of(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum

# print (sum_of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# nums = 34
# for i in nums:
#     print(i)

# list_items = [10, 22, 45, 67, 90]
# print(list_items[2])

# new_list = [1,2,3,4]
# new_list.insert(0,0)

# print(new_list)

def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True

print(isPalindrome('racecar'))