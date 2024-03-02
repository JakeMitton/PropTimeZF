"""
File: main.py
Author: Jake Mitton
Date: February 29, 2024
Description: An algorithm to compute the propagation time of
             Zero Forcing Sets for a given graph
"""
import sys
from typing import Optional


class _Vertex:

    def __init__(self, tag: str, is_coloured: bool) -> None:
        self.tag = tag
        self.adjacent = []
        self.is_coloured = is_coloured
        self.n_coloured = 0

    def add_adjacent(self, vertex) -> None:
        self.adjacent.append(vertex)

    def set_colour(self, setting: bool) -> None:
        self.is_coloured = setting


class Graph:

    def __init__(self) -> None:
        self.vertices = {}

    def _find_vertex(self, tag: str) -> Optional[_Vertex]:
        for vertex in self.vertices:
            if vertex.tag == tag:
                return vertex
        return None

    def build_graph(self, file: str) -> None:
        try:
            f = open(file, 'r')
        except FileNotFoundError:
            print("Invalid\n")
            print("Error: File Not Found")
        else:
            # TODO: Read in the file input to turn adjacency matrix into graph class
            f.close()
            pass

    def add_vertex(self, tag: str, is_coloured: bool = False) -> None:
        vertex = _Vertex(tag, is_coloured)
        self.vertices[vertex] = vertex.adjacent

    def add_edge(self, tag_1: str, tag_2: str) -> None:
        """
        Add the vertex with tag_1 to the adjacency list of the vertex
        with tag_2 and vice versa
        :param tag_1: Tag for first adjacent vertex
        :param tag_2: Tag for second adjacent vertex
        :return: None
        """
        vertex_1 = self._find_vertex(tag_1)
        vertex_2 = self._find_vertex(tag_2)
        if vertex_1 is not None and vertex_2 is not None:
            vertex_1.add_adjacent(vertex_2)
            vertex_2.add_adjacent(vertex_1)
        else:
            if vertex_1 is None:
                print(tag_1, "does not exist. Edge not possible.")
            elif vertex_2 is None:
                print(tag_2, "does not exist. Edge not possible.")

    def set_ZF_set(self) -> None:
        raise NotImplementedError
        pass

    def clean_colour(self) -> None:
        for each in self.vertices.keys():
            each.set_colour(False)

    def run_ZF(self) -> None:
        raise NotImplementedError
        pass


if __name__ == "__main__":
    graph = Graph()
    file = sys.argv[1]
    graph.build_graph(file)

    # graph.add_vertex("One")
    # graph.add_vertex("Two")
    # graph.add_vertex("Three")
    # graph.add_edge("One", "Two")
    # graph.add_edge("One", "Three")

    # for each in graph.vertices.keys():
    #     print("Vertex:", each.tag)
    #     if len(each.adjacent) > 0:
    #         for node in each.adjacent:
    #             print("\t", each.tag, "--> ", node.tag)
