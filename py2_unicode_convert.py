
import json

py_dict = {"Message": "success", "RequestId": "692030F0-C9D4-4DF4-A100-2D29B9890976",
           "Data": {"AvailableCashAmount": "87.28", "MybankCreditAmount": "0.00", "Currency": "CNY",
                    "AvailableAmount": "87.28", "CreditAmount": "0.00"}, "Code": "200", "Success": True}

json_dict = json.loads(json.dumps(py_dict))


def unicode_convert(data):
    if isinstance(data, dict):
        return {unicode_convert(key): unicode_convert(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [unicode_convert(i) for i in data]
    elif isinstance(data, unicode):
        return data.encode('utf-8')
    elif isinstance(data, str):
        return data.encode('utf-8')
    else:
        return data


json_dicts = unicode_convert(json_dict)
print(json_dicts)
