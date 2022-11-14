import random


def get_unique_list_numbers(min, max, total) -> list[int]:
    list_ = []
    while len(list_) != total:
        current_number = random.randint(min, max)
        if current_number not in list_:
            list_.append(current_number)
    return list_


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
