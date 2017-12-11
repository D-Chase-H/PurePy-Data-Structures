
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
        self.data = None
        self.end_of_word = False
        self.children = []


class Trie(object):
    """docstring for Trie."""
    def __init__(self):
        self.start_nodes = []


    def insert_node(self, new_word):

        curr_node = None
        node_list = self.start_nodes
        end = False
        for index, lett in enumerate(new_word):
            node_in_list = False
            if index == len(new_word) - 1:
                end = True

            for node in node_list:
                if node.data == lett:
                    curr_node = node
                    node_list = node.children
                    node_in_list = True
                    break

            if node_in_list is False:
                new_node = Node()
                new_node.data = lett

                if index == 0:
                    self.start_nodes.append(new_node)

                if curr_node is not None:
                    curr_node.children.append(new_node)

                curr_node = new_node
                node_list = new_node.children

            if end is True:
                curr_node.end_of_word = True


    def as_list(self):

        def recursive_search(node, curr_word, words=[]):

            if node.end_of_word is True:
                words.append(curr_word)

            for child in node.children:
                partial = curr_word + child.data
                recursive_search(child, partial, words)

            return words

        for node in self.start_nodes:
            curr_word = node.data
            words = recursive_search(node, curr_word)

        return words


    def search(self, word):

        word = list(word)
        last_index = len(word) - 1
        node_list = self.start_nodes
        is_in_trie = False

        for index, letter in enumerate(word):
            letter_check = False

            for node in node_list:

                if node.data == letter:
                    letter_check = True
                    node_list = node.children

                    if index == last_index:
                        if node.end_of_word is True:
                            is_in_trie = True
                            return is_in_trie
                    break

            if letter_check is False:
                is_in_trie = False
                return is_in_trie

        return is_in_trie



    def delete_word(self, word):
        word = list(word)
        last_index = len(word) - 1
        node_list = self.start_nodes
        fork_node = None
        levels_since_fork = 0

        for index, letter in enumerate(word):
            letter_check = False

            for node in node_list:

                if node.data == letter:
                    levels_since_fork += 1
                    letter_check = True
                    node_list = node.children

                    if index == last_index:
                        if node.end_of_word is True:
                            if not node.children:
                                print("step1")

                                nodes_to_del = []
                                curr_node = fork_node
                                for n in range(levels_since_fork):
                                    next_node = curr_node.children[0]
                                    curr_node.children.remove(next_node)
                                    curr_node = next_node
                                    nodes_to_del.append(curr_node)

                                for n in nodes_to_del:
                                    del n

                            else:
                                print("step2")
                                node.end_of_word = False
                            return "Word successfully deleted"

                    if node.end_of_word is True and len(node.children) == 1:
                        levels_since_fork = 0
                        fork_node = node
                    break

            if letter_check is False:
                return "Word not found in Trie."

        return



if __name__ == "__main__":

    words = []

    with open("words_alpha.txt", "r") as f:
        for line in f:
            words.append(line[:-1])
        f.close()

    new_trie = Trie()

    for w in words:
        new_trie.insert_node(w)

    arr_of_words = (new_trie.as_list())
    print("")

    d = new_trie.delete_word("aasvogels")
    print(d)
    print("\n\n")
    arr_of_words = (new_trie.as_list())
    print(len(arr_of_words))
    print("")

    d = new_trie.delete_word("aasvogel")
    print(d)
    print("\n\n")
    arr_of_words = (new_trie.as_list())
    print(len(arr_of_words))
    print("")
