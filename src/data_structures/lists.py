def add_element(my_list, element):
    my_list.append(element)
    return my_list

def remove_element(my_list, element):
    if element in my_list:
        my_list.remove(element)
    return my_list

def iterate_list(my_list):
    return [element for element in my_list]