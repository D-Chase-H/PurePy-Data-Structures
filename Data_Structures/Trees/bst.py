
from random import randrange


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
