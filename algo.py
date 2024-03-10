"""
File: algo.py
Author: Jake Mitton
Date: February 29, 2024
Description: An algorithm to compute the propagation time of
             Zero Forcing Sets for a given graph
"""
import sys
from typing import Optional


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

        def set_ZF_set(self, ZF_set: list) -> None:
            
            pass


if __name__ == "__main__":
    graph = Graph()
    file = sys.argv[1]
    graph.build_adjacency_list(file)