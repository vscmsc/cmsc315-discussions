"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque

def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track order nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were order.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # If the start node is not in the graph, there is nothing to search.
    if start not in graph:
        print(f"Sorry, '{start}' is not in the graph.")
        return []

    # Creating the queue to manage traversal order.
    # BFS explores nodes in the order they are discovered, moving level by level.
    queue = deque([start])

    # Creating a set to prevent the same node from being added to the queue more than once.
    # Because these nodes have been "discovered" but may not have been processed yet,
    # I chose this name to clearly distinguish between discovery and processing.
    # I recognize that this set is conventionally named "visited" in BFS implementations.
    discovered = {start}

    # Creating a list to store the order in which nodes are processed.
    order = []

    # A while loop to continue searching while there are still nodes in the queue.
    while queue:
        current = queue.popleft()

        # Once a node is processed, append it to the ordered list
        order.append(current)

        # Search each neighboring node
        for neighbor in graph[current]:
            # If a new node is discovered
            if neighbor not in discovered:
                # Add it to the queue to be processed later
                queue.append(neighbor)
                # And add it to the discovered set so it is not added to the queue again
                discovered.add(neighbor)

    # Returns the nodes in the order they were processed
    return order

def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # Representing the graph using a dictionary and adjacency lists.
    # Because this is an undirected graph, every connection must work in both directions.
    # For example, if Jane has a connection to Mary, then Mary must have a connection to Jane.
    # These connections are the "edges" that represent the relationships between each person, or "node".
    graph = {
        "Jane": ["Emily", "Mary"],
        "Mary": ["Agatha", "Jane", "Sarah"],
        "Agatha": ["Mary", "Emily"],
        "Emily": ["Jane", "Agatha"],
        "Sarah": ["Robin", "Mary"],
        "Robin": ["Sarah"]
    }

    # Displaying the contents of the graph, using a for loop for cleaner display.
    print("\nThe contents of the graph are:")
    for node in graph:
        print(f"\t{node}: {graph[node]}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    # Performing the BFS traversal using Sarah as the starting node.
    # Because the ordered list is returned, we can call on bfs() directly to have it print the traversal order.
    print(f"\nStarting with Sarah, the BFS traversal order is:\n\t{bfs(graph, 'Sarah')}")

    # Updating the existing graph to add one additional node and edge
    # Added Naomi with a connection to Robin, so both are updated to show the undirected connection.
    graph["Naomi"] = ["Robin"]
    graph["Robin"].append("Naomi")

    # Naomi ends up changing the traversal order because she is connected to Robin.
    # Starting with Sarah, BFS first processes Sarah and then discovers Robin and Mary.
    # After Robin is processed, Naomi is discovered and added to the queue to be processed after nodes already in queue.
    print(f"\nAfter updating the graph, the traversal order starting from Sarah is:\n\t{bfs(graph, 'Sarah')}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Creating an empty graph for the first edge case.
    # When searching an empty graph, our initial check should trigger.
    # This will print our message and return an empty list rather than attempting the bfs.
    empty_graph = {}
    print("\nWhen searching an empty graph, the following is returned:")
    print(bfs(empty_graph, "Sarah"))

    # Searching our existing graph with a non-existent start node
    # will also trigger our check, again printing our message and returning an empty list.
    print("\nWhen searching a graph for a non-existent start node, the following is returned:")
    print(bfs(graph, "Neil"))

if __name__ == "__main__":
    main()