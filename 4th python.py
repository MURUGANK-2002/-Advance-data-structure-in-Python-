from collections import deque

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = deque()
        self.redo_stack = deque()

    def type_text(self, new_text):
        self.undo_stack.append(self.text)
        self.text += new_text
        self.redo_stack.clear()
        self.display_text("Typed")

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
            self.display_text("Undo performed")
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()
            self.display_text("Redo performed")
        else:
            print("Nothing to redo.")

    def display_text(self, action):
        print(f"{action}. Current Text: '{self.text}'")

if __name__ == "__main__":
    editor = TextEditor()
    actions = {
        "1": lambda: editor.type_text(input("Enter text to type: ")),
        "2": editor.undo,
        "3": editor.redo,
        "4": exit
    }
    while True:
        print("\n--- Text Editor Menu ---")
        print("1. Type Text\n2. Undo\n3. Redo\n4. Exit")
        choice = input("Enter your choice: ")
        actions.get(choice, lambda: print("Invalid choice! Please try again."))()
