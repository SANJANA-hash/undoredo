class UndoRedoManager:
    def __init__(self):
        self.undo_stack = []  # Stack to keep history of actions
        self.redo_stack = []  # Stack to keep history of undone actions
        self.current_text = ""  # The current state of the text editor

    def perform_action(self, action, text=""):
        """Perform a new action: ADD or DELETE."""
        if action == "ADD":
            self.undo_stack.append(("ADD", text))
            self.current_text += text
            self.redo_stack.clear()  # Clear redo history on new action

        elif action == "DELETE":
            if text in self.current_text:
                self.undo_stack.append(("DELETE", text))
                self.current_text = self.current_text.replace(text, "", 1)
                self.redo_stack.clear()

    def undo(self):
        """Undo the last action."""
        if not self.undo_stack:
            print("Nothing to undo.")
            return

        action, text = self.undo_stack.pop()

        if action == "ADD":
            self.current_text = self.current_text[:-len(text)]
            self.redo_stack.append(("ADD", text))

        elif action == "DELETE":
            self.current_text += text
            self.redo_stack.append(("DELETE", text))

    def redo(self):
        """Redo the last undone action."""
        if not self.redo_stack:
            print("Nothing to redo.")
            return

        action, text = self.redo_stack.pop()

        if action == "ADD":
            self.current_text += text
            self.undo_stack.append(("ADD", text))

        elif action == "DELETE":
            if text in self.current_text:
                self.current_text = self.current_text.replace(text, "", 1)
            self.undo_stack.append(("DELETE", text))

    def show_text(self):
        """Display the current text."""
        print(f"Current Text: '{self.current_text}'")


# Testing the Manager
if __name__ == "__main__":
    manager = UndoRedoManager()

    # Simulating a text editor
    manager.perform_action("ADD", "Hello ")
    manager.perform_action("ADD", "World")
    manager.show_text()

    manager.undo()
    manager.show_text()

    manager.redo()
    manager.show_text()

    manager.perform_action("DELETE", "Hello ")
    manager.show_text()

    manager.undo()
    manager.show_text()
