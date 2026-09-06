"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Node value passed will be stored here
        self.value = value

        # Left and right child nodes are empty
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # initializing root with no value
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.
        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # This calls the recursive helper method, starting at the root.
        # Once that method successfully completes, it will return the updated node reference.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.
        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # This statement tells the method to create a new Node if the current node is empty.
        if node is None:
            return Node(value)

        # The example I chose to use in main() is a list of author names.
        # Because string comparisons are case-sensitive by default, I chose to use .lower() to
        # make the BST's alphabetical ordering case-insensitive.
        # This case insensitivity is only used during the insertion of values, and
        # the original value (case) of the node is preserved.

        # If the value being passed is SMALLER than the value of the node being compared, it moves to the LEFT in the BST.
        if value.lower() < node.value.lower():
            # This statement recursively searches the left subtree using the recursive helper method.
            # The recursive call keeps going until it finds an empty node (None).
            # Once it reaches the empty node, it effectively passes self._insert_recursive(None, value),
            # at which point it creates and returns the new Node.
            # That returned Node is then assigned to node.left.
            node.left = self._insert_recursive(node.left, value)

        # If the value being passed is LARGER than the value of the node being compared, it moves to the RIGHT in the BST.
        elif value.lower() > node.value.lower():
            # As above, this statement recursively searches the right subtree until it finds an empty node.
            # Once it does, it creates and returns the new Node, assigning it to node.right.
            node.right = self._insert_recursive(node.right, value)

        # If the value is equal, the method returns the node.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST can be more efficient than linear search because it
        # eliminates part of the remaining search space with each comparison.
        # In a *balanced* BST, the search space is roughly cut in half with each comparison,
        # with the search time being roughly O(log n).
        # However, an *unbalanced* BST can become less efficient and approach O(n).
        # In comparison to a BST, a linear search may have to check every item before it finds the target value.

        # Calling on the recursive search helper method,
        # starting with root and searching for the specified value.
        # The recursive helper method returns either True or False if found.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Checking whether the node exists before continuing with the search.
        # If the node is empty, the value is not in the tree.
        if node is None:
            return False
        # If the current node's value is the value that is being searched for, return True.
        if node.value.lower() == value.lower():
            return True
        # If the value is less than that of the current node, return the recursive search of the left node.
        if value.lower() < node.value.lower():
            return self._search_recursive(node.left, value)
        # If none of the above, then the value must be more than that of the current node.
        # Therefore, return the recursive search of the right node.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        # Creating an empty Python list, which is then passed to the helper below.
        values = []
        # This method returns the results of the recursive inorder helper method.
        # Once the helper method is done running, it will return the filled values.
        return self._inorder_recursive(self.root, values)

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # Inorder traversal visits all nodes in a BST from smallest to largest.
        # Therefore, starting from the root, this method adds all node values in sorted order,
        # first visiting the left subtree, then the current node, and finally the right subtree.

        # Note that in this case, we deliberately inserted all values as lower-case,
        # and the inorder traversal will visit all nodes in this BST in order from smallest to largest
        # according to the case-insensitive comparison used during value insertion.

        # As long as the node is not None, the following three lines will run recursively.
        # Because of the recursive calls, each node will independently follow the same three instructions.
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)
        # Once there are no more nodes to visit, the completed values list will be returned.
        return values

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # Creating a BST object for the subsequent author names.
    author_tree = BST()
    # The values that will be inserted into the BST.
    author_names = ["Poe", "Shelley", "Tolkien", "Austen", "Gaiman", "Shakespeare", "Dickens", "Asimov", "Orwell", "Hemingway"]
    # Looping through the list to insert the author names into the BST.
    for author in author_names:
        author_tree.insert(author)

    # Printing the list of author names added, in the order they were added.
    # The in-order printing is in the next to-do section below.
    print(f"\nAuthors added to BST, displayed in order of addition:\n\t"
          f"{', '.join(author_names)}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # Calling on .inorder() to perform an in-order traversal and print the author names.
    print("\nAfter performing an in-order traversal:")
    print(f"\t{', '.join(author_tree.inorder())}")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Demonstrating what happens in a BST search for a value that exists.
    # UPPER and lower case searches included to demonstrate effectiveness of .lower()
    print("\nSearching for authors that ARE in the BST: ")
    print("\t'Shelley' is in the BST: ", author_tree.search("Shelley"))
    print("\t'AUSTEN' is in the BST: ", author_tree.search("AUSTEN"))
    print("\t'Gaiman' is in the BST: ", author_tree.search("Gaiman"))
    print("\t'tolkien' is in the BST: ", author_tree.search("tolkien"))

    # Demonstrating what happens in a BST search for a value that does NOT exist.
    print("\nSearching for authors that are NOT in the BST: ")
    print("\t'Christie' is in the BST: ", author_tree.search("Christie"))
    print("\t'Paulsen' is in the BST: ", author_tree.search("Paulsen"))


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case")
    print("Edge case: Inserting duplicate values")

    # Creating a new BST object for the edge case test
    test_tree = BST()

    # Note that this list differs from the author_names list above in there being only five unique names, each added twice.
    # I also took this opportunity to test case sensitivity and check whether .lower() was functioning properly.
    # Since string comparisons are case-sensitive, this test checks that .lower() allows the BST to
    # treat different capitalization of the same name as a duplicate of that name.
    duplicate_names = ["Poe", "Shelley", "Tolkien", "Austen", "Gaiman",
                       "POE", "shelley", "TOLKIEN", "Austen", "Gaiman"]
    # Inserting the list into the test_tree BST.
    for name in duplicate_names:
        test_tree.insert(name)

    # Printing the complete list of names that were added, demonstrating the duplicates.
    print(f"\nTesting duplicate names. Names inserted: \n\t"
          f"{', '.join(duplicate_names)}")

    # Calling on the in-order traversal method to print the names, in-order, that were inserted into the tree.
    # Note that the printed result only contains five nodes.
    # The duplicates were not inserted into the tree.
    print(f"\nAfter performing in-order traversal:")
    print(f"\t{', '.join(test_tree.inorder())}")

if __name__ == "__main__":
    main()