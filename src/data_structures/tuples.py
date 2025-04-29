def create_tuple(elements):
    """Create a tuple from the given elements."""
    return tuple(elements)

def access_element(tup, index):
    """Access an element in the tuple by index."""
    if index < 0 or index >= len(tup):
        raise IndexError("Index out of range")
    return tup[index]