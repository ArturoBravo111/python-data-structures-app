def add_entry(dictionary, key, value):
    dictionary[key] = value
    return dictionary

def remove_entry(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

def get_value(dictionary, key):
    return dictionary.get(key, None)