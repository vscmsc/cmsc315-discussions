# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

0. General reflection/approach: 

For this first discussion, I created the parent class SewingProject with child class Apparel. Tying the assignment to one of my hobbies made it more tangible when thinking about the concept of object-oriented programming, and helped me wrap my head around the layers of abstraction inherent in OOP. Working first with pseudocode, I thought about sewing projects at a high level before working my way down to what data would be specific to different types of sewing projects, paying attention to what information could be inherited across types of sewing projects and what data needed to be unique to the child class. Focusing on just the one child class (Apparel) for this assignment, the design as a whole allows for the child class to inherit common traits while keeping more unique data encapsulated within the child class. This also allows for additional child classes to be added in the future to expand the class as a whole.

1. What concepts or skills did you learn while completing this assignment?

This assignment was a good refresher on parent/child classes and inheritance, however I don't recall coming across shallow vs. deep copying before. Seeing the difference between shallow and deep copying in action (and doing the teeniest amount of additional reading) helped solidify the concept. This is also the first time I have created a GitHub repository, so it's nice to get practical experience with it!

2. What challenges did you encounter, and how did you overcome them?

The biggest challenge was just re-acclimating myself to working with Python and accepting that I'm going to be a bit slower until I get back into the swing of things. I overcame roadblocks by referencing the course materials and examples in the text, and looking online for more information when I needed to go more in-depth.

3. Compare OOP to procedural programming.

A key differentiator of OOP from procedural programming is the emphasis on modularity. OOP focuses on "objects", their attributes, and how they relate and interact with one another. Procedural programming, on the other hand, relies more on standalone functions and operate in a more linear fashion.

4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

The modularity of OOP lends itself to easier maintainability and reusability. Because logic is encapsulated within classes, it's easier to update/add/remove unique features without inadvertently breaking another part of the system. This modularity also helps with debugging and lends itself to a bottom-up approach to testing: bottom-level functions that don't rely on other classes can be tested first to ensure they are functioning correctly before moving "up" through the class structure to identify and fix bugs within the code. This lowers overhead in terms of testing, but also lends itself to scalability since additional classes can be added/developed without requiring significant changes to existing functionality.
