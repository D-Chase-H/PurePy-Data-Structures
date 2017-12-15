
# Author: Dustin Chase Harmon

"""
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
import sys

class Node(object):
    """docstring for Node."""
    def __init__(self):
        self.data = None
        self.end_of_word = False
        self.children = dict()


class Trie(object):
    """docstring for Trie."""
    def __init__(self):
        self.start_nodes = dict()


    def insert_word(self, new_word):

        first_lett = new_word[0]

        try:
            new_node = self.start_nodes[first_lett]
        except KeyError:
            new_node = Node()
            new_node.data = first_lett

            self.start_nodes[first_lett] = new_node

        if len(new_word) == 1:
            new_node.end_of_word = True
            return

        else:
            curr_node = self.start_nodes[first_lett]

            for index, lett in enumerate(new_word[1:]):

                try:
                    curr_node = curr_node.children[lett]
                except KeyError:
                    new_child_node = Node()
                    new_child_node.data = lett

                    curr_node.children[lett] = new_child_node
                    curr_node = new_child_node

                if index == len(new_word) - 2:
                    curr_node.end_of_word = True
        return


    def search(self, word):
        is_in_trie = False
        curr_node = self.start_nodes[word[0]]
        index = 1

        while True:
            try:
                curr_node = curr_node.children[word[index]]

            except IndexError:
                if curr_node.end_of_word is True:
                    is_in_trie = True
                break

            except KeyError:
                break

            index += 1

        return is_in_trie


    def delete_word(self, word):
        try:
            curr_node = self.start_nodes[word[0]]
        except KeyError:
            raise ValueError("Word is not in the Trie")

        prev_node = None
        fork_node = curr_node
        fork_letter = None
        index = 0

        while True:
            if curr_node.data != word[index]:
                raise ValueError("Word is not in the Trie")

            if curr_node.end_of_word is True and len(curr_node.children) <= 1:
                fork_node = prev_node
                fork_letter = word[index]

            index += 1

            try:
                prev_node = curr_node
                curr_node = curr_node.children[word[index]]
            except IndexError:
                # If we are on the last letter of the word and it is not marked
                # as the end of a word, then the word is not in the Trie, then
                # we raise a ValueError.
                if curr_node.end_of_word is False:
                    raise ValueError("Word is not in the Trie")

                break

        if fork_node:
            try:
                del fork_node.children[fork_letter]
            except KeyError:
                # This handles the deletion of single character words.
                del fork_node

        else:
            # This branching path occurs whenever the most recent forking node
            # is the node that contains the last letter of the word.
            # If the last node has children nodes, then keep the node, but
            # change the node's end_of_wrd attribute to False.
            # However, if it has no children nodes, then delete it.
            if curr_node.children:
                curr_node.end_of_word = False
            else:
                del curr_node
        return


    def as_list_recursive(self):
        def recursive_search(node, curr_word):
            nonlocal words

            if node.end_of_word is True:
                words.append(curr_word)

            for child_node in node.children.values():
                partial = curr_word + child_node.data
                recursive_search(child_node, partial)

            return

        words = []
        for node in self.start_nodes.values():
            first_lett = node.data
            recursive_search(node, first_lett)

        return words


    def as_list_iterative(self):
        def iterative_search(node_dict):
            nonlocal words

            temp_dict = dict()

            for partial_word, child_dict in node_dict.items():
                for child_lett, child_node in child_dict.items():
                    if child_node not in visited:

                    new_partial_word = partial_word + child_lett

                    if child_node.end_of_word is True:
                        words.append(new_partial_word)

                        if child_node.children:
                            temp_dict[new_partial_word] = child_node.children

                    else:
                        temp_dict[new_partial_word] = child_node.children

            return temp_dict


        words = []

        for lett, curr_node in self.start_nodes.items():
            if curr_node.end_of_word is True:
                words.append(lett)

            node_dict = {lett: curr_node.children}

            while True:
                node_dict = iterative_search(node_dict)
                if not node_dict:
                    break

        return words
    
    
    
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
