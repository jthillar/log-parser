import json


def print_new_data(line_number: int, new_data: str):
    print(f'{line_number} : {new_data}')


def print_multiple_of_five(line_number: int):
    print_new_data(line_number, 'Multiple de 5')


def print_space_as_underscore(line_number: int, data: str):
    print_new_data(line_number, data.replace(' ', '_'))


def print_data(line_number: int, data: str):
    print_new_data(line_number, data)


def print_dict_with_pair_info(line_number: int, data: str):
    line_as_dict = json.loads(data)
    line_as_dict['pair'] = True if line_number % 2 == 0 else False
    print_new_data(line_number, json.dumps(line_as_dict, ensure_ascii=False).encode('utf8').decode())

