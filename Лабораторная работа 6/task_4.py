import json

INPUT_FILE = "input.csv"
DELIMITER = ","


def csv_to_list_dict(filename) -> list[dict]:
    list_ = []
    with open(filename) as f:
        for line in f:
            list_.append((line.rstrip().split(DELIMITER)))

    total_list = [{j: i[list_[0].index(j)] for j in list_[0]} for i in list_[1:]]

    return total_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
