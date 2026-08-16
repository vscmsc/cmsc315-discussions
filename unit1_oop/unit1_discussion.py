"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.

class SewingProject:
    category = "Sewing"    # class variable

    def __init__(self, project_name: str, skill_level: str, est_time: float, status: str):    # constructor
        self.project_name = project_name    # instance variable
        self.skill_level = skill_level    # instance variable
        self.est_time = est_time    # instance variable
        self.is_complete = False    # student-created extension (TO-DO 6)
        self.status = status

    def display(self):    # method that displays information about the object
        print(f"Project name: {self.project_name}")
        print(f"Skill level: {self.skill_level}")
        print(f"Estimated time: {self.est_time} hours")
        print(f"Status: {self.status}")

    def project_check(self, is_complete: bool):
        if is_complete:
            self.status = "Project has been completed!"
        else:
            self.status = "In Progress"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.

class Apparel(SewingProject):    # child class, inherits from parent SewingProject
    project_type = "Clothing"    # new class variable

    def __init__(self, project_name: str, skill_level: str, est_time: float, fabric_type: str, fabric_quantity: float, status: str):
        super().__init__(project_name, skill_level, est_time, status)
        self.fabric_quantity = fabric_quantity    # instance variable
        self.fabric_type = fabric_type    # instance variable
        self.notion_list = []

    def add_notion(self, notion: str):    # new method for adding to notion_list
        self.notion_list.append(notion)

    def display(self):    # overrides display() method from the parent class
        super().display()
        print(f"Fabric type: {self.fabric_type}")
        print(f"Fabric quantity: {self.fabric_quantity} yards")
        print(f"Required notion(s): {', '.join(self.notion_list)}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===\n")

    # create first object using child class
    project1 = Apparel("Floral Dress", "Beginner", 4.0, "Cotton", 2.5, "In Progress")
    project1.add_notion("Elastic")

    # create second object using child class
    project2 = Apparel("Autumn Coat", "Intermediate", 8.5, "Wool", 4.0, "In Progress")
    project2.add_notion("Buttons")
    project2.add_notion("Interfacing")
    project2.is_warm = True    # adding attribute to project2

    # display information about each object's namespace
    print("Project 1 Instance Namespace: \n", project1.__dict__)
    print("Project 2 Instance Namespace: \n", project2.__dict__)
    # display information about the class namespace
    print("Apparel Class Namespace: \n", Apparel.__dict__)

    print("\n=== Access class variable through Class ===\n")
    print(Apparel.project_type)

    print("\n=== Access class variable through Object ===\n")
    print("Project 1: ", project1.project_type)
    print("Project 2: ", project2.project_type)

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===\n")

    # object with nested mutable data
    original = Apparel("Floral Dress", "Beginner", 4.0, "Cotton", 2.5, "In Progress")
    original.add_notion("Elastic")

    shallow_copy = copy(original)    # creating shallow copy
    deep_copy = deepcopy(original)    # creating deep copy

    original.notion_list.remove("Elastic")    # modifying the original object's nested data

    # display the original object, shallow copy and deep copy
    print(f"Original notions: {original.notion_list}")
    print(f"Shallow copy: {shallow_copy.notion_list}")
    print(f"Deep copy: {deep_copy.notion_list}")

"""
    Shallow copies create new outer objects, however they copy the REFERENCES of nested objects instead of creating new copies of them.
    Deep copies create completely new copies of referenced objects, including the nested objects.
    This means that any changes to the original object's referenced data will also affect the shallow copy and vice versa.
    Meanwhile, the deep copy will remain unchanged.
    Reference: https://www.geeksforgeeks.org/blogs/difference-between-shallow-and-deep-copy-of-a-class/
"""

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object\n")

    # create object from the parent class
    project1 = SewingProject("Floral Dress", "Beginner", 4.0, "In Progress")
    project1.display()

    print("\nTODO: Create and test your child object\n")

    # create object from the child class
    apparel1 = Apparel("Floral Dress", "Beginner", 4.0, "Cotton", 2.5, "In Progress")
    apparel1.add_notion("Elastic")
    apparel1.project_check(True)    # using project_check to change the status to "complete"
    apparel1.display()

    # call to namespace and copy demonstration functions
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()