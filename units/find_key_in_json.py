# Ищет нужный ключ в json
# Если несколько одинаковых ключей - добавляет все в список, это нужно для запроса сразу нескольких валют
def find_keys_in_json(data: [dict, list], key: str) -> list:
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
