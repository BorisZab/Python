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

# def quick_sort(array):  #Быстрая сортировка
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] +quick_sort(greater)

# print(quick_sort([14,5,9,6,3,58,7,5,2,7]))


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