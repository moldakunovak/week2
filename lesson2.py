
# a = [2, 3, 4]
# s = "String"
# a.reverse()
# s.lower()
# print(a)
# print(s.lower())

# условные операторы if
# num1 = int(input("num1 "))
# num2 = int(input("num2 "))
# if num1 > num2:
#     print(f"{num1} more {num2}")
# elif num2 > num1:
#     print(f"{num2} more {num1}")

# num1 = int(input("num1 "))
# num2 = int(input("num2 "))
# operator = input("operator ")
# if operator == '+':
#     result = num1 + num2
#     print('result', result)
#
# elif operator == '-':
#     result = num1 - num2
#     print('result', result)
#
# elif operator == '*':
#     result = num1 * num2
#     print('result', result)
#
# elif operator == '/':
#     result = num1 / num2
#     print('result', result)


# lists = [1, 2, 3, 4]
# if 5 in lists:
#     print("Hello")

# or and
# lists = [18, 22, 25, 6]
# if 1 in lists and 25 in lists:
#     print("yes")

# if 1 in lists or 25 in lists:
#     print("yes")
#
# lists = []
# for n in range(1, 1001):
#     if n % 3 == 0 and n % 5 == 0 and n % 15 == 0:
#         lists.append(n)
# print(lists)

# zadachi 1
# temp = int(input("temp: "))
# temp_type = input("f or c ")
# if temp_type == 'f':
#     convert = (9/5)*temp+32
#     print("temperatura po farengeitu = ", convert)
#
# elif temp_type == "c":
#     convert = (5/9)*(temp-32)
#     print("temperatura po farengeitu = ", convert)

# zad_2
# temp = int(input("temp in C: "))
# if temp < -273.15:
#     print("недействительна, она ниже абсолютного нуля ")
# elif -273.15 == -273.15:
#     print("равна абсолютному 0")
# elif temp in range(-273.15, 0):
#     print("температура ниже точки замерзания ")
# elif temp == 0:
#     print("температура в точке замерзания ")
# elif temp in range(0, 100):
#     print("температура в нормальном диапазоне")
# elif temp == 100:
#     print("в точне кипения")2
# elif temp > 100:
#     print("выше точки кипения ")

# табл умнож
# num = int(input("enter a number: "))
# for i in range(1, 11):
#     print(f"{num} * {i} = {i*num}")
#
# num_1 = int(input("enter 1 number: "))
# num_2 = int(input("enter 2 number: "))
# operator = input("choose operator: ")
# if operator == '+':
#     print(num_1 + num_2)
# elif operator == '-':
#     print(num_1-num_2)
# elif operator == '*':
#     print(num_1*num_2)
# elif operator == '/':
#     print(num_1/num_2)

# num_1 = int(input("enter number: "))
# for i in range(1, 11):
#     print(f"{num_1} * {i} = {num_1*i}")

# temp = int(input("enter temp to convert: "))
# temp_type = input("far or cel: ")
# if temp_type == "far":
#     convert = (9/5)*temp+32
#     print("temp in far: ", convert)
# elif temp_type == "cel":
#     convert = (5/9)*(temp-32)
#     print("temp in cel: ", convert)

# year = int(input("enter year for check: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("yes")
# else:
#     print("no")
from typing import List

# list = []
# for i in range(1, 1001):
#     if i % 3 == 0 and i % 5 == 0 and i % 15 == 0:
#         list.append(i)
# print(list)

