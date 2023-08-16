"""
Модуль для обработки полученных от API данных
"""


def find_keys_in_json(data: [dict, list], key: str) -> list:
    """
    Функция ищет нужный ключ в десериализованном json
    Если есть несколько одинаковых ключей - добавляет все в список, это нужно для запроса сразу нескольких валют

    :param data:
    :param key:
    :return:
    """
    result_list = []
    if isinstance(data, dict):
        result = data.get(key)
        if result is not None:
            result_list.append(result)
        for value in data.values():
            result_list.extend(find_keys_in_json(value, key))
    elif isinstance(data, list):
        for i_data in data:
            result_list.extend(find_keys_in_json(i_data, key))
    return result_list
