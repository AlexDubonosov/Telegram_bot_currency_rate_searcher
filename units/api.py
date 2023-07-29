from config_data import config
import json
import requests


def find_keys_in_json_format(data: [dict, list], key: str) -> str:
    if isinstance(data, dict):
        result = data.get(key)
        if result is not None:
            return result
        else:
            for value in data.values():
                result = find_keys_in_json_format(value, key)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for i_data in data:
            result = find_keys_in_json_format(i_data, key)
            if result is not None:
                return result




def return_value_from_api(key):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    with open('E:\python\skillbox\python_basic_diploma\database\current_currency.txt', 'r') as file:
        user_currency = file.read()

    querystring = {"region": "US", "symbols": user_currency}
    headers = {
        "X-RapidAPI-Key": config.API_KEY,
        "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    needed_data = json.loads(response.text)

    needed_value = find_keys_in_json_format(needed_data, key)
    return needed_value


