"""
File: main.py
Author: Jake Mitton
Date: February 29, 2024
Description: An algorithm to compute the propagation time of
             Zero Forcing Sets for a given graph
"""


class Graph:
    vertices = {}

    def __init__(self) -> None:
        print("Graph initializer")
        pass


class Vertex(Graph):

    def __init__(self, tag: str, is_coloured=False) -> None:
        self.tag = tag
        self.is_coloured = is_coloured
        self.adjacent = []
        super().vertices[self] = self.adjacent
        print("Vertex initializer")
        print("vertex is coloured =", self.is_coloured)


if __name__ == "__main__":
    graph = Graph()
    vertex = Vertex("One")
    vertex2 = Vertex("Two", True)

    print("Hello, world")
    print("Graph vertices = ")

    for each in graph.vertices:
        print("\t", each.tag, "is coloured:", each.is_coloured)
