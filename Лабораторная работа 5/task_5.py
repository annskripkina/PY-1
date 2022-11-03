import random
import string


def get_random_password(n=8) -> str:
    str_of_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = "".join(random.sample(str_of_symbols, n))
    return password


print(get_random_password())
