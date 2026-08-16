# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

The following learning objectives were outlined for module: 
- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## My Approach

For this first assignment, I created the parent class SewingProject with child class Apparel (further detail provided in "Implementation of Requirements" section below). Tying the assignment to one of my hobbies made it more tangible when thinking about the concept of object-oriented programming, and helped me wrap my head around the layers of abstraction inherent in OOP. Working first with pseudocode, I thought about sewing projects at a high level before working my way down to what data would be specific to different types of sewing projects, paying attention to what information could be inherited across types of sewing projects and what data needed to be unique to the child class. Focusing on just the one child class (Apparel) for this assignment, the design as a whole allows for the child class to inherit common traits while keeping more unique data encapsulated within the child class. This also allows for additional child classes to be added in the future to expand the class as a whole.

## Implementation of Requirements

Complete all TODO sections in the source code:

1. Create a parent class: I created the parent class `SewingProject`. This class includes the class variable `category` and three instance variables: `project_name`, `skill_level`, and `est_time`. This class contains a constructor and a method that displays information about the object.
2. Create a child class using inheritance: I created the child class `Apparel`, which inherits functionality from the parent `SewingProject`. It contains the new class variable `project_type` as well as three new instance variables: `fabric_quantity`, `fabric_type`, and `notion_list`. It contains a new method for adding notions to `notion_list` and overrides the `display()` method from the parent class.
3. Demonstrate class and instance namespaces: The function `demonstrate_namespaces()` was created with the purpose of printing information about each object's namespace as well as information about the class namespace. To do this, I created two objects of the child class (named `project1` and `project2`) and then used __dict__ to display the relevant namespace information.
4. Demonstrate shallow and deep copying: To demonstrate shallow and deep copying, I created an object that contains mutable data (`notion_list`), then used `demonstrate_copying()` to print the `original` and `shallow_copy` nested data as well as the `deep_copy` nested data. This demonstrated how shallow copies create new outer objects, however they copy the REFERENCES of nested objects instead of creating new copies of them, whereas deep copies create completely new copies of referenced objects, including the nested objects. This means that any changes to the original object's referenced data will also affect the shallow copy and vice versa, while the deep copy will remain unchanged.
5. Create and test objects in `main()`: In `main()` I created one object each from the parent class `SewingProject` and child class `Apparel`, followed by calling `demonstrate_namespace()` and `demonstrate_copying()` to show namespace information and copy-type comparisons.
6. Add a student-created extension: Added the functionality of checking whether the project is in progress or complete. See `is_complete` and `status`.

## Discussion Board Reflection

1. What concepts or skills did you learn while completing this assignment?

This assignment was a good refresher on parent/child classes and inheritance, however I don't recall coming across shallow vs. deep copying before. Seeing the difference between shallow and deep copying in action (and doing the teeniest amount of additional reading) helped solidify the concept. This is also the first time I have created a GitHub repository, so it's nice to get practical experience with it!

2. What challenges did you encounter, and how did you overcome them?

The biggest challenge was just re-acclimating myself to working with Python and accepting that I'm going to be a bit slower until I get back into the swing of things. I overcame roadblocks by referencing the course materials and examples in the text, and looking online for more information when I needed to go more in-depth.

3. Compare OOP to procedural programming.

A key differentiator of OOP from procedural programming is the emphasis on modularity. OOP focuses on "objects", their attributes, and how they relate and interact with one another. Procedural programming, on the other hand, relies more on standalone functions and operate in a more linear fashion.

4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

The modularity of OOP lends itself to easier maintainability and reusability. Because logic is encapsulated within classes, it's easier to update/add/remove unique features without inadvertently breaking another part of the system. This modularity also helps with debugging and lends itself to a bottom-up approach to testing: bottom-level functions that don't rely on other classes can be tested first to ensure they are functioning correctly before moving "up" through the class structure to identify and fix bugs within the code. This lowers overhead in terms of testing, but also lends itself to scalability since additional classes can be added/developed without requiring significant changes to existing functionality.
