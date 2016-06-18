import copy

class Bunch(object):
    """Convert a dictionary into a Variable Depth Namespace Object - Making things pretty"""
    def __init__(self, data, depth='one'):
        if depth == 'one':
            self.__dict__.update(data)
        else:
            for name, value in data.items():
                setattr(self, name, self._wrap(value, depth))

    def _wrap(self, value, depth='two'):
        if isinstance(value, (tuple, list, set, frozenset)): 
            return type(value)([self._wrap(v) for v in value])
        else:
            if depth == 'two':
                return Bunch(value) if isinstance(value, dict) else value
            else:
                return Bunch(value, depth) if isinstance(value, dict) else value


def sanitize(data, rules, strict=False, empty=False):
    payload = {}

    for item in rules:
        if item in data:
            payload[item] = data[item]
        else:
            if strict:
                raise Exception("Not all required fields are present")
            elif not empty:
                payload[item] = ''

    return payload


def upsert(d1, d2):
    d2 = copy.deepcopy(d2)
    for k, v in d1.items():
        if k in d2:
            if all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                d2[k] = upsert(v, d2[k])
    d3 = d1.copy()
    d3.update(d2)
    return d3
