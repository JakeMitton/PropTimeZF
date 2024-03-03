# PropTimeZF
Implementation of an algorithm to compute the propagation time of zero forcing sets on a given graph.

The input file should be a .txt file and adhere to the following format:
    - First line must begin with $ followed by the names of the vertices with spaces between them.
    - The following lines form an adjacency matrix with the vertex names down the left edge and 1s and 0s to denote adjacencies.
    - The diagonal must be composed solely of 0s. This program only runs on irreflexive graphs.
    - Eg:

      ```
        $ a b c d e
        a 0 1 0 1 1
        b 1 0 0 0 0
        c 0 0 0 1 0
        d 1 0 1 0 1
        e 1 0 0 1 0

      ```

