# list тип или список,коллекция к-я содержит разыне типы данных
# a = [1, 2, 3, 4]
# lists = [1, "dfdff", 2.3, [1, 2], {"s": 3}, ]
#
# print(lists[3])
#
# for i in lists:
#     print(i)
# print("len = ", len(lists))

# str_1 = "hello world"
# for i in str_1:
#    print(i)
# print("len = ", len(lists))

# str_1 = "hello world"
# for i in range(10, 15, 2):
#    print(i)
# print("len = ", len(lists))

# for i in range(0, 101, 2):
#     print(i)
# lists_1 = list(range(0, 101, 2))
# lists_1 = list("str")
# print(lists_1)

# append добавление элемента в список
# lists = [1, "Nazgul", 2.3, [1, 2], {"s": 3}, ]
# lists.append({"name": "Nazgul"})
# lists.append([1, 2, ])
# lists.extend([1, 2, ]) расширяет
# print(lists)

# insert
# print(lists[1], "before")
# lists.insert(1, 5)
# print(lists[1], "after")
# print(lists)

#pop
# phone_numbers = ["+996555443322", "+996777665544", "+996500443322"]
# black_list = phone_numbers.pop(2)
# print(black_list)
# print(phone_numbers)
# phone_numbers.insert(2, black_list)
# print(phone_numbers)

# remove
# phone_numbers.remove("+996500443322")
# print(phone_numbers)

# count метод подсчета
# print(phone_numbers.count("+996777665544"))

# reverse переворачивает
# print(phone_numbers.count("+996777665544"))
# phone_numbers.reverse()
# print(phone_numbers)

# задача
# start = int(input("enter start "))
# end = int(input("enter end "))
# step = int(input("enter step "))
# power = int(input("enter power "))
# # нужно чтобы он сохранял знаение , чтобы каждый раз не создавал новую , если б внутри цикла сделала б , то он каждый раз создавал б
# list_1 = []
# for i in range(start, end, step):
#     list_1.append(pow(i, power))
# print(list_1)
# list_1.clear()
# print(list_1)

# sort
# empty = [1, 4, 3, 2]
# empty.sort()
# print(empty)

# # задачи 1
# name = input("enter name ")
# for i in range(5):
#     print(name)

# # задачи 3
# name = input("enter name ")
# for i in range(100):
#     print(i, name)

# # задача 4
# a = "---"
# for i in range(1, 21):
#     print(i, a, (i**2))

# задача 5
# for i in range(8, 90, 3):
#     print(i)

# задача 6
# for i in range(102, 0, -2):
#     print(i)

# задача 7
# word_1 = input("word_1 ")
# word_2 = input("word_2 ")
# word_3 = input("word_3 ")
# word_4 = input("word_4 ")
# for i in range(7):
#     print(word_1, end="")
# for i in range(7):
#     print(word_2, end="")
# for i in range(7):
#     print(word_3, end="")
# for i in range(7):
#     print(word_4, end="")

# задача 8
# name = input("name: ")
# time = int(input("number of iteration: "))
# for i in range(time):
#     print(name)

# задача 9
# fibonacci_1 = int(input("enter num fibonacii: "))
# num_1 = 0
# num_2 = 1
# length = 0
# print(num_1, num_2, end="")
# length -= 2
# for i in range(length > 0):
#     print(num_1 + num_2, end="")
# num = num_2
# num_2 = num_1+num_2
# num_1 = num
# length -= 1
# print("fibonacii: ")
#
# fib1 = fib2 = 1
# n = int(input("chislo fib= "))
# print(fib1, fib2, end="")
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1+fib2
# print(fib2, end="")

# chislo = int(input("enter chislo: "))
# num_1 = 1
# num_2 = 1
# # count = 0
# i = 2
# for i in range(chislo):
#     new_num = num_1 + num_2
#     num_1 = num_2
#     num_2 = new_num
#     i += 1
# print(new_num)
#


# задача 10
# for x in range(4):
#     print("x"*20)

# задача 11
# for x in range(1):
#     print("x"*15)
# for x in range(2):
#     print("x             x")
# for x in range(3):
#     print("x             x")
# for x in range(1):
#     print("x"*15)

# задача 12
