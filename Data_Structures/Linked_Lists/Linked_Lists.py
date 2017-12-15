
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


class Node(object):
    """docstring for Node."""

    def __init__(self):
        self.data = None
        self.next_node = None



class LinkedList(object):
    """docstring for LinkedList."""

    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.length = 0


    def append(self, data, double=True):
        new_node = Node()
        new_node.data = data

        if not self.start_node:
            self.start_node = new_node
            self.end_node = new_node
        else:
            self.end_node.next_node = new_node

            if double is True:
                new_node.previous_node = self.end_node

            self.end_node = new_node

        self.length += 1
        return


    def append_left(self, data, double=False):
        new_node = Node()
        new_node.data = data

        if not self.start_node:
            self.start_node = new_node
            self.end_node = new_node
        else:
            new_node.next_node = self.start_node

            if double is True:
                self.start_node.previous_node = new_node

            self.start_node = new_node


    def insert_at_index(self, data, index, double=False):
        assert index <= self.length - 1, \
        ("\nIndexing Error: "
         "The index provided exceeds the maximum index in the Linked List.")
        assert index < 0, \
        ("\nIndexing Error: "
         "The index provided is below the minimum index in the Linked List.")

        curr_node = self.start_node
        prev_node = None
        curr_index = 0

        while curr_node:
            if curr_index == index:
                new_node = Node()
                new_node.data = data
                prev_node.next_node = new_node
                new_node.next_node = curr_node
                if double is True:
                    new_node.previous_node = prev_node
                    curr_node.previous_node = new_node
                return

            index += 1
        return


    def perform_removal(self, prev_node, removal_node, next_node, double=False):
        if not prev_node:
            if removal_node.next_node:
                self.start_node = removal_node.next_node
            else:
                self.start_node = None
        else:
            if next_node:
                prev_node.next_node = next_node

                if double is True:
                    next_node.previous_node = prev_node

            else:
                prev_node.next_node = None
                self.end_node = prev_node

        self.length -= 1
        del removal_node
        return


    def remove(self, data, double=False, remove_all=False):
        """
        Removes:
            - The first occurence of the input data
            or
            - All occurences of the input data.
        """

        curr_node = self.start_node
        prev_node = None

        while curr_node:
            if curr_node.data == data:
                next_node = curr_node.next_node
                self.perform_removal(prev_node, removal_node, next_node, double)

                if remove_all is False:
                    return

            prev_node = curr_node
            curr_node = curr_node.next_node
        return


    def remove_all_occurences(self, data, double=False):
        return self.remove(data, double, True)


    def get_slice(self, start_index, end_index):
        """
        Uses 0-based indexing, and works like a standard Python List when
        slicing, meaning that 0:0 returns empty, and 0:1 returns the first
        element, and 1:4 returns the second, third and fourth element.
        """
        temp_list = list()
        curr_node = self.start_node
        prev_node = None
        curr_index = 0

        while curr_node and curr_index <= end_index:
            if start_index <= curr_index <= end_index:
                temp_list.append(curr_node.data)

            curr_node = curr_node.next_node
            curr_index += 1

        return temp_list


    def linked_list_generator(self):
        """
        Returns a generator that generates a single node's data in the
        Linked List at a time.
        """
        curr_node = self.start_node

        while curr_node:
            yield curr_node.data

            curr_node = curr_node.next_node


    def as_list(self):
        temp_list = list()
        curr_node = self.start_node

        while curr_node:
            temp_list.append(curr_node.data)
            curr_node = curr_node.next_node

        return temp_list



class SingleyLinkedList(LinkedList):
    """docstring for SingleyLinkedList."""

    def __init__(self):
        super().__init__()


class DoubleyLinkedList(LinkedList):
    """docstring for DoubleyLinkedList."""

    def __init__(self):
        super().__init__()

    def __append(self, data):
        return self.append(data, True)


    def __append_left(self):
        return self.append_left(data, True)


    def __perform_removal(self, prev_node, removal_node, next_node):
        return self.perform_removal(prev_node, removal_node, next_node, True)


    def __remove(self, data, remove_all=False):
        return self.remove(data, True, remove_all)


    def __remove_all_occurences(self, data):
        return self.remove_all_occurences(data, True, True)


    def __insert_at_index(self, data, index):
        return self.insert_at_index(data, index, True)






if __name__ == '__main__':
    from random import randrange
    print("")
    ############################################################################

    arr = [randrange(1, 100) for i in range(10)]
    print(arr, "\n\n")

    sll = SingleyLinkedList()
    dll = DoubleyLinkedList()

    for num in arr:
        sll.append(num)
        dll.append(num)


    sll_arr = sll.as_list()
    dll_arr = dll.as_list()

    print(sll_arr == dll_arr == arr)
    print(sll_arr)
    print(dll_arr, "\n")

    sll_gen = sll.linked_list_generator()
    print(sll_gen)
    print(list(sll_gen), "\n")

    sll_slice = sll.get_slice(2, 7)
    print(sll_slice, "\n")

    ############################################################################
    print("")
