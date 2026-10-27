"""A simple command-line text editor demonstrating stacks.

The editor uses two stacks:
- undo_stack stores previous text states.
- redo_stack stores states that can be restored after an undo.
"""


class TextEditor:
    """Manage text and its undo/redo history using stacks."""

    def __init__(self):
        self.current_text = ""
        self.undo_stack = []
        self.redo_stack = []

    def edit(self, new_text):
        """Replace the current text and record the previous state."""
        if new_text == self.current_text:
            return False

        self.undo_stack.append(self.current_text)
        self.current_text = new_text
        # A new edit creates a new history branch, so redo is no longer valid.
        self.redo_stack.clear()
        return True

    def undo(self):
        """Undo the latest edit. Return True if an undo was performed."""
        if not self.undo_stack:
            return False

        self.redo_stack.append(self.current_text)
        self.current_text = self.undo_stack.pop()
        return True

    def redo(self):
        """Restore the latest state that was undone."""
        if not self.redo_stack:
            return False

        self.undo_stack.append(self.current_text)
        self.current_text = self.redo_stack.pop()
        return True

    def clear(self):
        """Clear the text while preserving the ability to undo the change."""
        if not self.current_text:
            return False

        self.undo_stack.append(self.current_text)
        self.current_text = ""
        self.redo_stack.clear()
        return True


def main():
    """Run the interactive command-line application."""
    editor = TextEditor()

    while True:
        print("\n=== StackWrite: Undo/Redo Text Editor ===")
        print("1. Enter or replace text")
        print("2. Undo")
        print("3. Redo")
        print("4. Display current text")
        print("5. Clear text")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            new_text = input("Enter the new text: ")
            if editor.edit(new_text):
                print("Text updated.")
            else:
                print("The text is unchanged.")
            print("Current text:", repr(editor.current_text))

        elif choice == "2":
            if editor.undo():
                print("Undo successful.")
            else:
                print("Nothing to undo.")
            print("Current text:", repr(editor.current_text))

        elif choice == "3":
            if editor.redo():
                print("Redo successful.")
            else:
                print("Nothing to redo.")
            print("Current text:", repr(editor.current_text))

        elif choice == "4":
            print("Current text:", repr(editor.current_text))

        elif choice == "5":
            if editor.clear():
                print("Text cleared. You can undo this change.")
            else:
                print("The text is already empty.")
            print("Current text:", repr(editor.current_text))

        elif choice == "6":
            print("Thank you for using StackWrite.")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
