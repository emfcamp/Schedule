from jinja2 import Environment, Undefined

def day_sort(iterable):
    if iterable is None or isinstance(iterable, Undefined):
        return iterable
    else:
        return sorted(iterable, key=_sort_ordinal)

def _sort_ordinal(date):
    if date is not None:
        return date.toordinal()
    else:
        return 1000000000

