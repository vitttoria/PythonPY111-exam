# Оценить асимптотическую сложность приведенного ниже алгоритма:
# a = len(arr) - 1  - O(1)
# out = list() - O(1) - создание пустого списка
# while a > 0: - O(nlogn)
#     out.append(arr[a]) - O(n) - добавление в массив
#     a = a // 1.7 - O(1)
# out.merge_sort() - O(nlogn)
# Максмальная сложность = O(1) + O(1) + O(nlogn) + O(n) + O(1) + O(nlogn) => O(nlogn)
