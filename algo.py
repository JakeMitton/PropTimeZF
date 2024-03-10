"""
File: algo.py
Author: Jake Mitton
Date: February 29, 2024
Description: An algorithm to compute the propagation time of
             Zero Forcing Sets for a given graph
"""
import sys
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self) -> None:
        self.adjacency_list = []
        # Each index in colour/colour_prime corresponds to a vertex
        # 1 = coloured and 0 = uncoloured
        self.colour = []
        self.colour_prime = []

    def build_adjacency_list(self, file: str) -> None:
        """
                Parses an input file to form the adjacency list.
                :param file: .txt file (Format specified in README.md)
                :return: None
                """
        try:
            f = open(file, 'r')
        except FileNotFoundError:
            print("Invalid\n")
            print("Error: File Not Found")
        else:
            input = list(f)
            input = [line.split() for line in input]
            input = [line for line in input]
            if input[0][0] != '$':
                print("Incorrectly formatted input file.")
                exit()

            row = 0
            for line in input[1:]:
                col = 1
                self.adjacency_list.append([])
                self.colour.append(0)
                self.colour_prime.append(0)
                for each in line[1:]:
                    if each == '1':
                        self.adjacency_list[row].append(input[0][col])
                    col += 1
                row += 1

            print("****************************************")
            for line in self.adjacency_list:
                print(line)
            print("Colour = ", self.colour)
            print("Colour_Prime = ", self.colour_prime)
            print("****************************************")
            f.close()

    def get_ZF_set(self) -> list:
        print("Please enter the vertices in the Zero Forcing Set on a single line, seperated by spaces.")
        print("Close the graph image to proceed.")
        printGraph(self)
        ZF_set_str = input("Zero Forcing Set: ")
        ZF_set = list(ZF_set_str.split())
        ZF_set = [int(item) for item in ZF_set]
        return ZF_set

    def set_ZF_set(self) -> bool:
        ZF_set = self.get_ZF_set()
        for each in ZF_set:
            if each <= len(self.colour):
                self.colour[each] = 1
                self.colour_prime[each] = 1
            else:
                print(each, " is not a vertex in the graph. Please try again.")
                return False
        return True

    def find_prop_time(self) -> int:
        # TODO: Comment this function better / add docstring
        propagation_time = 0
        blank_neighbours = []
        updated_flag = True
        while updated_flag:
            updated_flag = False
            coloured_flag = True
            for each in self.colour:
                if each == 0:
                    coloured_flag = False
            if coloured_flag:
                return propagation_time
            for s in range(0, len(self.adjacency_list)):
                # If a vertex is coloured then we look at each of its adjacent vertices
                if self.colour[s] == 1:
                    for a in self.adjacency_list[s]:
                        # If the adjacent vertex is uncoloured then add it to blank_neighbours
                        if self.colour[int(a)] == 0:
                            blank_neighbours.append(int(a))
                if len(blank_neighbours) == 1:
                    self.colour_prime[int(blank_neighbours[0])] = 1
                    blank_neighbours.clear()
                    updated_flag = True
            for vertex in range(0, len(self.colour_prime)):
                self.colour[vertex] = self.colour_prime[vertex]
            propagation_time += 1
        return propagation_time


def printGraph(graph: Graph) -> None:
    G = nx.Graph()
    for each in range(0, len(graph.adjacency_list)):
        G.add_node(each)
        G.add_edge(each, int(graph.adjacency_list[each][0]))
        for adj in graph.adjacency_list[each]:
            G.add_edge(each, int(adj))
    nx.draw_circular(G, with_labels=True, node_color='#ABAEB0', node_size=500)
    plt.show()


if __name__ == "__main__":
    graph = Graph()
    file = sys.argv[1]
    graph.build_adjacency_list(file)
    graph.set_ZF_set()
    print("Colour =", graph.colour)
    print("The propagation time is:", graph.find_prop_time())
