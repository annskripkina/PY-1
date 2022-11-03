import random


def get_unique_list_numbers() -> list[int]:
    total = 15
    list_ = []
    while len(list_) != total:
        current_number = random.randint(-10, 10)
        if current_number not in list_:
            list_.append(current_number)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

