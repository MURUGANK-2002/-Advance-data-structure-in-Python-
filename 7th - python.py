class Node:
    def __init__(self, isbn, title, author):
        self.isbn, self.title, self.author = isbn, title, author
        self.left, self.right = None, None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, isbn, title, author):
        if not self.root:
            self.root = Node(isbn, title, author)
        else:
            self._insert(self.root, isbn, title, author)

    def _insert(self, node, isbn, title, author):
        if isbn < node.isbn:
            if node.left:
                self._insert(node.left, isbn, title, author)
            else:
                node.left = Node(isbn, title, author)
        elif isbn > node.isbn:
            if node.right:
                self._insert(node.right, isbn, title, author)
            else:
                node.right = Node(isbn, title, author)
        else:
            node.title, node.author = title, author  # Update info if ISBN exists

    def search(self, isbn):
        return self._search(self.root, isbn)

    def _search(self, node, isbn):
        if not node or node.isbn == isbn:
            return node
        return self._search(node.left, isbn) if isbn < node.isbn else self._search(node.right, isbn)

    def in_order_traversal(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if not node:
            return []
        left_books = self._in_order_traversal(node.left)  # Traverse left subtree
        current_book = [(node.isbn, node.title, node.author)]  # Current node data
        right_books = self._in_order_traversal(node.right)  # Traverse right subtree
        return left_books + current_book + right_books  # Combine the results


if __name__ == "__main__":
    bst = BinarySearchTree()
    while True:
        print("\nLibrary Management System:")
        print("1. Add a Book\n2. Search for a Book by ISBN\n3. Display All Books\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print("\nAdd a Book")
            isbn = input("Enter the ISBN of the book: ")
            title = input("Enter the title of the book: ")
            author = input("Enter the author's name: ")
            bst.insert(isbn, title, author)
            print(f"Book '{title}' added successfully!")

        elif choice == "2":
            print("\nSearch for a Book")
            isbn = input("Enter the ISBN to search: ")
            book = bst.search(isbn)
            if book:
                print(f"Book found: ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}")
            else:
                print("Book not found!")

        elif choice == "3":
            print("\nAll Books in the Library (In-Order):")
            books = bst.in_order_traversal()
            if books:
                for isbn, title, author in books:
                    print(f"ISBN: {isbn}, Title: {title}, Author: {author}")
            else:
                print("No books in the library.")

        elif choice == "4":
            print("Exiting the application...")
            break

        else:
            print("Invalid choice! Please choose a valid option (1-4).")
