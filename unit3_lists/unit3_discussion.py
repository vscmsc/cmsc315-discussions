"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # .insert() inserts the specified value at the specified index position
    # after a value is inserted, all values at that index or higher get shifted one position to the right (index value +1)
    # the earlier a value is inserted (the lower the index), the more elements need to be shifted
    lst.insert(index, value)

def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # checking whether the provided index is in range
    # index cannot be negative, and cannot be equal to/greater than the length of the list
    if index >= len(lst) or index < 0 or len(lst) == 0:
        return None
    # .pop() removes and returns the value at the specified index position
    return lst.pop(index)

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # using a loop to iterate through all values in lst
    # this is a linear search because it is sequential
    # it starts at the index 0 and works through all subsequent positions
    # until the value is found, or it reaches the end of the list
    for index in range(len(lst)):
        if lst[index] == value:
            return index
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.\n")

    # initializing our list for the character's inventory
    character_inventory = ["Boots", "Sword", "Helmet"]

    # printing the original character_inventory list
    print(f"Character's starting inventory: {', '.join(character_inventory)}")

    # inserting items, printing contents of updated list
    insert_at(character_inventory,0, "Cloak")    # insert at beginning
    print(f"Inserting at beginning. Updated inventory: {', '.join(character_inventory)}")
    insert_at(character_inventory, 2, "Key")    # insert in middle
    print(f"Inserting in middle. Updated inventory: {', '.join(character_inventory)}")
    insert_at(character_inventory, len(character_inventory), "Gloves")    # insert at end
    print(f"Inserting at end. Updated inventory: {', '.join(character_inventory)}")


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.\n")

    # deleting items from the character inventory
    # each line contains item deleted and display of updated list
    print(f"{delete_at(character_inventory, 0)} removed. Updated inventory: {', '.join(character_inventory)}")     # item deleted from beginning
    print(f"{delete_at(character_inventory, 3)} removed. Updated inventory: {', '.join(character_inventory)}")    # item deleted from middle
    print(f"{delete_at(character_inventory, len(character_inventory) - 1)} removed. Updated inventory: {', '.join(character_inventory)}")     # item deleted from end

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # searching for a value that exists
    print("\nSearching for 'Key':")
    result_key = search_value(character_inventory, "Key")
    # if/else to print the results of the search
    if result_key >= 0:
        print("Character has that item. It is at index " + str(result_key) + ".")
    else:
        print("Character does not have that item.")

    # searching for a value that does not exist in character_inventory
    print("\nSearching for 'Gold':")
    result_gold = search_value(character_inventory, "Gold")
    # if/else to print the results of the search
    if result_gold >= 0:
        print("Character has that item. It is at index " + str(result_gold))
    else:
        print("Character does not have that item.")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.\n")

    new_character_inventory = []

    # attempting to delete from an empty list
    print("When attempting to delete an item from an empty list, returns: ", delete_at(new_character_inventory, 0))

    # adding items to test removal from an invalid index
    new_character_inventory = ["Hat", "Gloves", "Boots"]
    # deleting from invalid index
    print("When attempting to delete from an invalid index, returns: ", delete_at(new_character_inventory, len(new_character_inventory)))

if __name__ == "__main__":
    main()