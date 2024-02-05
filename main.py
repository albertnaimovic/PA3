# from typing import Generator

# def infinite_range(start: int = 0) -> Generator[int, None, None]:
#     current = start
#     while True:
#         yield current
#         current += 1


# # Usage
# counter = 0
# for value in infinite_range(10):
#     print(value)
#     counter += 1
#     if counter == 5:
#         break

# 1.Write a Python program to create a generator that generates the squares of numbers up to a given number.


# from typing import Generator

# def simple_generator(n: int) -> Generator[int, None, None]:
#     for i in range(n):
#         yield pow(i, 2)


# for value in simple_generator(5):
#     print(value)

# 2.Write a Python program to create a generator that yields "n" random numbers between a low and high number that are inputs.

# from typing import Generator
# import random


# def random_num_generator(n: int, low_num: int, high_num: int) -> Generator[int, None, None]:
#     if (high_num > low_num) and ((high_num - low_num) >= n):
#         for _ in range(n):
#             yield random.randint(low_num, high_num)
#     else:
#         yield "Low number cannot be higher than high number and n cannot be higher than difference between high and low numbers."


# n = input("Enter range of numbers: ")
# low_num = input("Enter low number: ")
# high_num = input("Enter high number: ")

# try:
#     for value in random_num_generator(int(n), int(low_num), int(high_num)):
#         print(value)
# except Exception as err:
#     print(err)

# 3. Write a Python program to create a generator that iterates over a string.

# from typing import Generator


# def string_iterator(input: str) -> Generator[str, None, None]:
#     for x in input:
#         yield x


# for value in string_iterator("Kompiuteris"):
#     print(value)

# 4.Write a Python program to create a Fibonacci series generator.

# from typing import Generator


# def fibonacci_generator(n: int) -> Generator[int, None, None]:
#     num_1 = 0
#     num_2 = 1
#     for _ in range(n):
#         yield num_1 + num_2
#         num_3 = num_1
#         num_1 = num_2
#         num_2 = num_3 + num_2


# for value in fibonacci_generator(10):
#     print(value)


# 5.Write a Python program to create a generator from a list that yields item from the list if it is a number.

# from typing import Generator


# def return_numbers(my_list: list) -> Generator[list, None, None]:
#     for x in my_list:
#         if isinstance(x, (int, float, complex)):
#             yield x
#         # else:
#         #     if str(x).isnumeric():
#         #         yield x


# for value in return_numbers([1, 2, 3, "ne skaicius", 414, "5", 2.3, 10, "sis irgi"]):
#     print(value)

# 6.Create a list of tuples, each representing a person's information. Each tuple contains the following information:
# (name: str, age: int, city: str, salary: float). Your task is to create Python generators to perform the following tasks:

# Filtering Generator: Create a generator function that filters the people who are below a certain age threshold.
# Mapping Generator: Create a generator function that maps the names of people to uppercase.
# Aggregation Generator: Create a generator function that calculates the average salary of the selected group.
from typing import Generator

persons = [
    ("Albert", 26, "Vilnius", 7000.0),
    ("Jonas", 36, "Kaunas", 2000.0),
    ("Algirdas", 85, "Jonava", 500.0),
    ("Marius", 41, "Vilnius", 5000.0),
]


def filtering_generator(
    persons: list, age_threshold: int
) -> Generator[tuple, None, None]:
    filtered_persons = filter(lambda person: person[1] < age_threshold, persons)
    for person in filtered_persons:
        yield person
    # for person in persons:
    #     if person[1] < age_threshold:
    #         yield person


for person in filtering_generator(persons=persons, age_threshold=40):
    print(person)
print()


def mapping_generator(persons: list) -> Generator[str, None, None]:
    uppercase_names = map(lambda person: person[0].upper(), persons)
    for name in uppercase_names:
        yield name
    # for person in persons:
    #     yield person[0].upper()


for person in mapping_generator(persons=persons):
    print(person)
