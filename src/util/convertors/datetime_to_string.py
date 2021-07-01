from datetime import datetime


def convert_datetime_to_string(date_time: datetime):
    if isinstance(date_time, datetime):
        return date_time.__str__()
