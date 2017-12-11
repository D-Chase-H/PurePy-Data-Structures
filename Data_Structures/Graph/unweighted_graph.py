
# Author: Dustin Chase Harmon

"""
License: 

MIT License

Copyright (c) 2017 Dustin Chase Harmon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class Node(object):
    """docstring for Node."""
    def __init__(self):
        self.id_num = None
        self.edges = set()


class Graph(object):
    """docstring for Graph."""
    def __init__(self):
        self.nodes = dict()



    ############################################################################
    # Insertion Methods
    ############################################################################
    def insert_node(self, id_num):
        try:
            self.nodes[id_num]
        except KeyError:
            new_node = Node()
            new_node.id_num = id_num
            self.nodes[id_num] = new_node
        return


    def undirected_insert_nodes_from_edge_pair(self, pair):
        """ pair: list/tuple type == [x, y] """
        node_1_id_num = pair[0]
        self.insert_node(node_1_id_num)
        node_1 = self.nodes[node_1_id_num]

        node_2_id_num = pair[1]
        self.insert_node(node_2_id_num)
        node_2 = self.nodes[node_2_id_num]

        node_1.edges.add(node_2)
        node_2.edges.add(node_1)
        return


    def directed_insert_nodes_from_edge_pair(self, from_node, to_node):
        """
        from_node = integer
        to_node = integer
        """
        node_1_id_num = from_node
        self.insert_node(node_1_id_num)
        node_1 = self.nodes[node_1_id_num]

        node_2_id_num = to_node
        self.insert_node(node_2_id_num)
        node_2 = self.nodes[node_2_id_num]

        node_1.edges.add(node_2)
        return


    ############################################################################
    # Disjoint-Set Methods
    ############################################################################
    def arr_of_disjoint_sets(self):

        def search_forest(curr_node, curr_subset):
            if curr_node.id_num in curr_subset:
                return

            curr_subset.add(curr_node.id_num)
            visited_nodes.add(curr_node.id_num)

            for node in curr_node.edges:
                search_forest(node, curr_subset)
            return


        arr = []
        visited_nodes = set()

        for n in self.nodes.values():

            if n.id_num not in visited_nodes:
                curr_subset = set()
                search_forest(n, curr_subset)

                if curr_subset:
                    arr.append(curr_subset)

        return arr


    ############################################################################
    # Depth-First-Search Methods
    ############################################################################
    def depth_first_search_bool(self, start, end):
        """
        start = integer
        end = integer
        Returns: Bool
        """

        def dfs_check(curr_node):
            nonlocal is_connected
            nonlocal end_node

            if is_connected is True:
                return

            if curr_node in visited_nodes:
                return

            visited_nodes.add(curr_node)

            for node in curr_node.edges:
                if node == end_node:
                    is_connected = True
                    return
                else:
                    dfs_check(node)


        start_node = self.nodes[start]
        end_node = self.nodes[end]

        if start_node == end_node:
            return True

        visited_nodes = set([])
        is_connected = False
        dfs_check(start_node)
        return is_connected


    def depth_first_search_all_paths(self, start, end):
        from copy import copy
        """
        start = integer
        end = integer
        Returns: Bool
        """

        def dfs_find_path(curr_node, visited_nodes=set(), path=[]):
            nonlocal all_paths
            nonlocal end_node

            if curr_node in visited_nodes:
                return

            visited_nodes.add(curr_node)
            path.append(curr_node)

            for node in curr_node.edges:
                if node == end_node:
                    temp_path = tuple(copy(path) + [node])
                    all_paths.append(temp_path)
                else:
                    temp_visited_nodes = copy(visited_nodes)
                    temp_path = copy(path)
                    dfs_find_path(node, temp_visited_nodes, temp_path)


        start_node = self.nodes[start]
        end_node = self.nodes[end]

        if start_node == end_node:
            return [[start_node]]

        all_paths = []
        dfs_find_path(start_node)
        return all_paths


    ############################################################################
    # Breadth-First-Search Methods
    ############################################################################
    def breadth_first_search_bool(self, start, end):
        """
        start = integer
        end = integer
        Returns: Bool
        """

        def bfs_check(curr_edges):
            nonlocal is_connected
            nonlocal visited_nodes
            nonlocal end_node

            if end_node in curr_edges:
                is_connected = True
                return

            new_edges = set()

            for node in curr_edges:
                visited_nodes.add(node)

                for node_edge in node.edges:
                    if node_edge not in visited_nodes:
                        new_edges.add(node_edge)

            if not new_edges:
                return
            else:
                bfs_check(new_edges)


        start_node = self.nodes[start]
        end_node = self.nodes[end]

        if start_node == end_node:
            return True

        visited_nodes = set([start_node])
        curr_edges = set([edg for edg in start_node.edges])
        is_connected = False
        bfs_check(curr_edges)
        return is_connected


    def bfs_shortest_path(self, start, end):
        """
        start = integer
        end = integer
        Returns: Bool
        """

        def determine_path():
            nonlocal curr_edges
            nonlocal visited_nodes
            nonlocal start_node
            nonlocal end_node
            nonlocal depth

            paths = [[end_node]]
            complete = False
            tally = 0

            for loop_num in range(depth):
                remove_nodes = set()
                new_paths = []

                for index, p in enumerate(paths):
                    last_node = p[-1]
                    poss_paths = []

                    for node in last_node.edges:

                        # If we are on the last node, then skip any edge-node
                        # that is not the start node.
                        if loop_num == depth - 1:
                            if node != start_node:
                                continue

                        if node in visited_nodes:
                            temp = p + [node]
                            poss_paths.append(temp)
                            remove_nodes.add(node)

                    for sub_path in poss_paths:
                        new_paths.append(sub_path)

                for node in remove_nodes:
                    visited_nodes.remove(node)

                paths = new_paths
            paths = tuple([tuple(reversed(p)) for p in paths])
            return paths


        def bfs_check(curr_edges):
            nonlocal is_connected
            nonlocal visited_nodes
            nonlocal end_node
            nonlocal depth

            depth += 1
            if end_node in curr_edges:
                is_connected = True
                return

            new_edges = set()

            for node in curr_edges:
                visited_nodes.add(node)

                for node_edge in node.edges:
                    if node_edge not in visited_nodes:
                        new_edges.add(node_edge)

            if not new_edges:
                return
            else:
                bfs_check(new_edges)


        start_node = self.nodes[start]
        end_node = self.nodes[end]

        if start_node == end_node:
            return [[start_node]]

        depth = 0
        visited_nodes = set([start_node])
        curr_edges = set([edg for edg in start_node.edges])
        is_connected = False
        bfs_check(curr_edges)
        paths = determine_path()
        return paths


if __name__ == '__main__':
    import sys
    from random import randrange

    print("START\n")
    ############################################################################


    pairs = set()
    while len(pairs) < 20:
        num1 = randrange(20)
        num2 = randrange(20)
        if num1 == num2:
            continue

        new = (num1, num2)
        pairs.add(new)

    pairs = list(pairs)
    g = Graph()

    print(pairs, "\n")

    for p in pairs:
        g.undirected_insert_nodes_from_edge_pair(p)

    d_set = g.arr_of_disjoint_sets()
    print("Disjoint Set:  ", d_set, "\n")

    start = pairs[9][0]
    end = pairs[4][1]

    dfs = g.depth_first_search_bool(start, end)
    print("DFS: Path from {} to {} is {}\n".format(start, end, dfs))


    dfs_paths = g.depth_first_search_all_paths(start, end)
    dfs_paths = [[node.id_num for node in path] for path in dfs_paths]
    print("DFS: All paths from {} to {} are {}\n".format(start, end, dfs_paths))


    bfs = g.breadth_first_search_bool(start, end)
    print("BFS: Path from {} to {} is {}\n".format(start, end, bfs))


    bfs_short = g.bfs_shortest_path(start, end)
    bfs_short = [[j.id_num for j in i] for i in bfs_short]
    print("BFS Shortest: Path from {} to {} is {}\n".format(start, end, bfs_short))

    ############################################################################
    print("\nEND")
