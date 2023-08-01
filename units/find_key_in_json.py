def find_keys_in_json(data: [dict, list], key: str) -> str:
    if isinstance(data, dict):
        result = data.get(key)
        if result is not None:
            return result
        else:
            for value in data.values():
                result = find_keys_in_json(value, key)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for i_data in data:
            result = find_keys_in_json(i_data, key)
            if result is not None:
                return result
