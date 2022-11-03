from pprint import pprint
total_num = 15
list_of_numbers = [{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(total_num+1)]
pprint(list_of_numbers)
