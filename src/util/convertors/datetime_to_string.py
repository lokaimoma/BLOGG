from datetime import datetime


def convert_datetime_to_string(object: datetime):
    if isinstance(object, datetime):
        return object.__str__()
