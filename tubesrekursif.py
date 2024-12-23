import time
import csv

# Class definition for a tree node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    """Insert a new key into the BST."""
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    """Perform an inorder traversal of the BST."""
    if root is None:
        return
    # Traverse the left subtree
    inorder_traversal(root.left)
    # Visit the root
    print(root.key, end=" ")
    # Traverse the right subtree
    inorder_traversal(root.right)

def load_data_from_csv(file_path, max_count=None):
    """Load numbers from a CSV file into a list with an optional limit."""
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        data = [int(row[0]) for row in reader]
        if max_count is not None:
            return data[:max_count]
        return data

# Main execution
if __name__ == "__main__":

    # Load file path and user-defined limit
    file_path = "random_data_1000.csv"  # Replace with the actual path if necessary
    print("Enter the number of data points to sort (up to 1000):")
    max_count = int(input("> "))

    start_time = time.perf_counter()
    
    # Load data from the CSV file
    keys = load_data_from_csv(file_path, max_count)

    # Build the BST
    root = None
    for key in keys:
        root = insert(root, key)

    # Perform inorder traversal
    print("\nInorder Traversal of the BST:")
    inorder_traversal(root)

    # Calculate elapsed time
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("\n")
    print(f"Elapsed time: {elapsed_time:.10f} seconds")
