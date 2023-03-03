# def sum_num(n):
#     sum = 0
#     for i in range(n + 1):
#         sum += i
#     return sum

# print(sum_num(5))

# def sum_str(*args):  # неогрниченнное количество элементов *args
#     res = ""
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 'l'))

# import Exm as E
# print(E.max1(10,9))

# Фибоначи

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)

# ///////////////////////////////////////////////

# def quick_sort(array):  #Быстрая сортировка
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] +quick_sort(greater)

# print(quick_sort([14,5,9,6,3,58,7,5,2,7]))

# ///////////////////////////////////////////////

# def merge_sort(nums): #Сортировка слиянием
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i<len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k]= left[i]
#                 i+=1
#             else:
#                 nums[k] = right[j]
#                 j+=1
#             k+=1
#         while i < len(left):
#             nums[k]= left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             nums[k]= right[j]
#             j+=1
#             k+=1
# list1= [1,4,5,6,76,48,1,0,4,6,7,4]
# merge_sort(list1)
# print(list1)

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a, b: a + b

# math(lambda a, b: a + b, 5, 45)

# array = [1, 2, 3, 5, 8, 15, 23, 38]
# array1 = []
# for i in array:
#     if i % 2 == 0:
#         array1.append((i, i**2))
# print(array1)

# ///////////////////////////////////////////////
# def select(f, col):
#     return [f(x)for x in col]

# def where(f, col):
#     return[x for x in col if f(x) ]
# array = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, array)
# print(res)
# res = where(lambda x: x%2==0,res)
# print(res)
# res = list(select(lambda x:(x, x**2),res))
# print(res)

# list1 = [ x for x in range(1,20)]
# print(list1)
# list1 = list(map(lambda x:x +10,list1))
# print(list1)

# ///////////////////////////////////////////////
# data = '26 156 48 468 486 468 4'
# print(data)

# data = list(map(int, data.split()))
# print(data)

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x%10==5,data))
# print(res)