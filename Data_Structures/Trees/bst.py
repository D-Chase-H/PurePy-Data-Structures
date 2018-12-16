
#   Author: D-Chase-H

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
        self.left_child = None
        self.right_child = None
        self.parent = None



class BST(object):
    """docstring for RedBlackTree."""
    def __init__(self):
        self.root = None
        self.height = 0


    def recursive_insert(self, curr_node, number):

        if curr_node.left_child == None:
            new_node = Node()
            new_node.data = number
            curr_node.left_child = new_node
            return
        if curr_node.right_child == None:
            new_node = Node()
            new_node.data = number
            curr_node.right_child = new_node
            return

        if curr_node.left_child != None and number <= curr_node.data:
            return self.recursive_insert(curr_node.left_child, number)
        if curr_node.right_child != None and number > curr_node.data:
            return self.recursive_insert(curr_node.right_child, number)

    def insert_node(self, number):

        if not self.root:
            new_node = Node()
            new_node.data = number
            self.root = new_node
            return

        return self.recursive_insert(self.root, number)


    def print_inorder(self, curr_node=None):
        if curr_node is None:
            curr_node = self.root

        if curr_node.left_child != None:
            self.print_inorder(curr_node.left_child)
        if curr_node.data != None:
            print(curr_node.data,)
        if curr_node.right_child != None:
            self.print_inorder(curr_node.right_child)


    def search_tree(self, number, curr_node=None):
        if curr_node is None:
            curr_node = self.root

        if curr_node.data == number:
            return True

        if curr_node.left_child != None and number <= curr_node.data:
            return self.search_tree(number, curr_node.left_child)
        if curr_node.right_child != None and number > curr_node.data:
            return self.search_tree(number, curr_node.right_child)

        return False


if __name__ == '__main__':
    from random import randrange

    print("\n\n")

    arr = [randrange(1000) for num in range(1000)]
    bst = BST()

    print("inserting")
    for i in arr:
        bst.insert_node(i)
    print("\n\n")
    bst.print_inorder()

    print("searching")
    print(bst.search_tree(arr[5]))
    print(bst.search_tree(455545546))
    print("\n\n")
