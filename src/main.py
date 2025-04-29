from data_structures.lists import add_element, remove_element, iterate_list
from data_structures.dictionaries import add_entry, remove_entry, get_value
from data_structures.sets import add_to_set, remove_from_set, set_operations
from data_structures.tuples import create_tuple, access_element

def demonstrate_list_operations():
    """Demonstrates operations on lists."""
    print("\n--- List Operations ---")
    my_list = []
    add_element(my_list, 10)
    add_element(my_list, 20)
    print("List after adding elements:", my_list)
    remove_element(my_list, 10)
    print("List after removing an element:", my_list)
    print("Iterating over list:", iterate_list(my_list))


def demonstrate_dictionary_operations():
    """Demonstrates operations on dictionaries."""
    print("\n--- Dictionary Operations ---")
    my_dict = {}
    add_entry(my_dict, 'name', 'Alice')
    add_entry(my_dict, 'age', 30)
    print("Dictionary after adding entries:", my_dict)
    print("Value for 'name':", get_value(my_dict, 'name'))
    remove_entry(my_dict, 'age')
    print("Dictionary after removing an entry:", my_dict)


def demonstrate_set_operations():
    """Demonstrates operations on sets."""
    print("\n--- Set Operations ---")
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    
    # Add and remove elements
    add_to_set(set_a, 7)
    remove_from_set(set_b, 6)
    
    print("Set A:", set_a)
    print("Set B:", set_b)
    
    # Perform set operations
    results = set_operations(set_a, set_b)
    print("Union:", results['union'])
    print("Intersection:", results['intersection'])
    print("Difference (A-B):", results['difference'])


def main():
    # Demonstrate list operations
    demonstrate_list_operations()

    # Demonstrate dictionary operations
    demonstrate_dictionary_operations()

    # Demonstrate set operations
    demonstrate_set_operations()


if __name__ == "__main__":
    main()