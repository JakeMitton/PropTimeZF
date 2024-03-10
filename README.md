# PropTimeZF
Implementation of an algorithm to compute the propagation time of zero forcing sets on a given graph.

The input file should be a .txt file and adhere to the following format:
    - First line must begin with $ followed by the names of the vertices with spaces between them.
    - The vertices must be named integers, beginning with 0 and increasing from left to right along the matrix.
    - The following lines form an adjacency matrix with the vertex names down the left edge and 1s and 0s to denote adjacencies.
    - The diagonal must be composed solely of 0s. This program only runs on irreflexive graphs.
    - Eg:

      ```
        $ 0 1 2 3 4
        0 0 1 0 1 1
        1 1 0 0 0 0
        2 0 0 0 1 0
        3 1 0 1 0 1
        4 1 0 0 1 0

      ```

