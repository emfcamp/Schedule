from jinja2 import Environment, Undefined
import datetime

def day_sort(iterable):
    if iterable is None or isinstance(iterable, Undefined):
        return iterable
    else:
        return sorted(iterable, key=_sort_ordinal)

def _sort_ordinal(date):
    offset = 10000000000
    if date is not None:
        if date < datetime.date.today(): # It's in the past
            return offset - date.toordinal()
        else:
            return date.toordinal()
    else:
        return offset

