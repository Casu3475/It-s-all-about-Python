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

# def isPalindrome(str):
#     startIndex = 0
#     endIndex = len(str) - 1 

#     for x in str:
#         if str[startIndex] != str[endIndex]:
#             return False
#     return True

# print(isPalindrome('racecar'))

# menu = ['pizza', 'pasta', 'ice cream', 'chocolate', 'sushi']

# def find_sushi(sushi):
#     if sushi[0] == 's':
#         return sushi

# map_sushi = map(find_sushi, menu)
# print(map_sushi)
# for x in map_sushi:
#     print(x)

# a=[[96],[69]]
# print(''.join(list(map(str,a))))

# z = ["alpha", "bravo", "charlie"]
# new_z = [i[0]*2 for i in z]
# print(new_z)

# def sum(n):
#     if n == 1:
#         return 0
#     return n + sum(n-1)

# a = sum(5)
# print(a)

# numbers = [15,30,47,82,95]
# def lesser(numbers):
#     return numbers < 50

# small = list(map(lesser, numbers))
# print(small)

# class MyClass:
#     a = 5
class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass
