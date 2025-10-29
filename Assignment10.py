# create a menu driven program of binary search tree which include the following options 
# 1. Insert
# 2. Delete
# 3. Search
# 4. Traversal
    # PreOrder , InOrder , PostOrder
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a new node into the BST
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            print("Element added successfully.")
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                print("Element added successfully.")
            else:
                self._insert(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                print("Element added successfully.")
            else:
                self._insert(node.right, data)
        else:
            print("Duplicate value not allowed in BST.")

    # Search an element in BST
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    # Delete a node
    def delete(self, data):
        self.root = self._delete_rec(self.root, data)

    def _delete_rec(self, node, data):
        if node is None:
            print("Element not found in BST.")
            return node

        if data < node.data:
            node.left = self._delete_rec(node.left, data)
        elif data > node.data:
            node.right = self._delete_rec(node.right, data)
        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with two children: Get inorder successor (smallest in right subtree)
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete_rec(node.right, temp.data)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Traversals
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


# ---------------- MENU DRIVEN PROGRAM ----------------
if __name__ == "__main__":
    bst = BST()

    while True:
        print("\n=== BINARY SEARCH TREE MENU ===")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Traversal")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = int(input("Enter value to insert: "))
            bst.insert(data)

        elif choice == '2':
            data = int(input("Enter value to delete: "))
            bst.delete(data)

        elif choice == '3':
            data = int(input("Enter value to search: "))
            found = bst.search(data)
            print("Element found!" if found else "Element not found.")

        elif choice == '4':
            print("\nTraversal Options:")
            print("a. Preorder")
            print("b. Inorder")
            print("c. Postorder")
            t_choice = input("Enter your choice: ").lower()

            if t_choice == 'a':
                print("Preorder traversal:")
                bst.preorder(bst.root)
            elif t_choice == 'b':
                print("Inorder traversal:")
                bst.inorder(bst.root)
            elif t_choice == 'c':
                print("Postorder traversal:")
                bst.postorder(bst.root)
            else:
                print("Invalid traversal option!")
            print()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")

