from random import uniform
from itertools import chain

# 1. Случайности не случайны
def generate_random_numbers(number: int):
    return [uniform(0, number) for i in range(number)]



# 2. Ленивое объединение 
def merge_list(first_list: list, second_list: list):
    return chain(first_list,second_list)



# 3. Рефакторинг
def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids
    responses = [dict(item_id = item_id) for item_id in item_ids]
    return responses



