DEFAULT_COUNT = 0


def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    letters = "".join(str_.split())
    for symbol in letters:
        if symbol.isalpha():
            dict_[symbol] = dict_.get(symbol, DEFAULT_COUNT) + 1
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

dict_2 = get_count_char(main_str)


def percent_func(new_dict):
    sum_values = sum(new_dict.values())
    for key in new_dict.keys():
        new_dict[key] = str(round(new_dict[key] / sum_values * 100, 2)) + " %"
    return new_dict


#print(percent_func(dict_2))
