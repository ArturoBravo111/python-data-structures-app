def add_to_set(s, element):
    """Adds an element to the set."""
    s.add(element)
    return s

def remove_from_set(s, element):
    """Removes an element from the set if it exists."""
    s.discard(element)  # Using discard to avoid KeyError
    return s

def set_operations(set_a, set_b):
    """Performs union, intersection, and difference operations on two sets."""
    union = set_a.union(set_b)
    intersection = set_a.intersection(set_b)
    difference = set_a.difference(set_b)
    return {
        'union': union,
        'intersection': intersection,
        'difference': difference
    }