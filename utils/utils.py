from dataclasses import asdict
from datetime import datetime


def datetime_string_to_datetime(date_string: str) -> datetime:
    try:
        return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S%z')
    except Exception as e:
        return None


def print_list_of_dataclass(data: list):
    result = []
    for i in data:
        result.append(asdict(i))

    print(result)
    return result
