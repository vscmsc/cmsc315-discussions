"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Creating an empty dictionary named 'course_catalog'
    course_catalog = {}

    # Adding 5 key-value pairs (the available classes for the next semester)
    course_catalog["SEW101"] = "Introduction to Sewing"
    course_catalog["SEW215"] = "Buttonholes and Closures"
    course_catalog["SEW305"] = "Garment Construction: Patterns"
    course_catalog["SEW310"] = "Working with Knits"
    course_catalog["SEW425"] = "Advanced Tailoring"

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    print("\nSearching for available courses in course_catalog:")
    # Retrieving and displaying two existing keys from course_catalog
    # The lookup uses the key to search the dictionary, and
    # returns the value located at that reference.
    print(f"\tSearching for SEW101 returns: {course_catalog['SEW101']}")
    print(f"\tSearching for SEW305 returns: {course_catalog['SEW305']}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # To update the value associated with an existing key,
    # we can just specify the key and 'set' it as something different.
    # This overwrites the existing value.

    # Introducing/explaining/printing the original name of the course
    print(f"\nNext semester, ~~(SEW305) {course_catalog['SEW305']}~~ will change to: ")

    # Changing the value associated with the key 'SEW305'
    course_catalog["SEW305"] = "Reading Commercial Patterns"

    # Printing the new value for 'SEW305'
    print(f"\t\t(SEW305): {course_catalog['SEW305']}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # Printing the current course catalog
    print(f"\nCourse Catalog: ")
    for course in course_catalog:
        print(f"\t{course}: {course_catalog[course]}")

    # Printing the intent to delete a key-value pair from the course catalog
    # (Demonstrates that the key-value pair exists)
    print(f"\nDue to insufficient staffing, ~~{course_catalog['SEW215']}~~ will not be offered this semester.")

    # Deleting the key-value pair from the dictionary
    del course_catalog["SEW215"]

    # Printing the updated dictionary after deletion of key-value pair
    print(f"\nUpdated Course Catalog: ")
    for course in course_catalog:
        print(f"\t{course}: {course_catalog[course]}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Using a try-except block allows us to look up a missing key
    # without a resulting KeyError from crashing the program.
    # Instead, we can print a message if the key is not found.
    print("\nSearching for course not in course_catalog:")
    try:
        print(course_catalog["SEW450"])
    except KeyError:
        print("\tCourse is not listed, no details available.")

    # Similarly, we can use this same method when attempting to delete a key.
    # If an attempt to delete a missing key is made,
    # the except block will catch the error and print the designated message.
    print("\nAttempting removal of course not in course_catalog:")
    try:
        del course_catalog["SEW450"]
    except KeyError:
        print("\tCourse is not offered, nothing to delete.")

    # Assigning a value to a dictionary key will update the value if the key already exists,
    # or will add a new key-value pair if the key does not exist (is 'missing').
    # Therefore, this:
        # course_catalog["SEW450"] = "Couture Sewing Techniques"
    # will either add *or* update "SEW450", depending on whether the key already exists.
    # Using an if-else statement to demonstrate both possibilities
    print("\nSearching for course to add or update: ")
    if "SEW450" in course_catalog:
        course_catalog["SEW450"] = "Couture Sewing Techniques"
        print("\tSEW450 was already in Course Catalog. Therefore, course name was updated.")
    else:
        course_catalog["SEW450"] = "Couture Sewing Techniques"
        print("\tSEW450 was not found in existing catalog. Course added.")

if __name__ == "__main__":
    main()