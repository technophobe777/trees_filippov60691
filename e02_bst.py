from tree_node import TreeNode
from tree_visualizer import TreeVisualizer
from e01_traversals import RecursiveTraversal

class BST:
    def __init__(self):
        self.root = None

    def __eq__(self, other):
        if not isinstance(other, BST):
            return False
        return self.root == other.root


    def insert_node(self, data, current_node=0):
        pass


    def insert_list(self, data_list):
        pass


    def find_node(self, data, current_node=0):
        pass


    def delete_node(self, node_to_delete, current_node=0):
        pass


    def visualize(self):
        TreeVisualizer.visualize(self.root)


    def traverse(self):
        return RecursiveTraversal.inorder(self.root)
