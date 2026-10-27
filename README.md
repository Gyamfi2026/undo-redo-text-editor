# StackWrite: Undo/Redo Text Editor

A simple command-line text editor built in Python to demonstrate a real-world use of the **stack** data structure. It implements Undo and Redo using the **Last In, First Out (LIFO)** principle.

## Real-world application

Text editors and word processors commonly provide Undo and Redo features. If a user makes several changes, Undo reverses the most recent change first. Redo restores a change that was undone.

## Features

- Enter or replace the current text.
- Undo the most recent edit.
- Redo a previously undone edit.
- Display the current text.
- Clear the text and undo the clear operation.
- Handle empty undo and redo stacks safely.
- Unit tests using Python's built-in `unittest` framework.

## Requirements

- Python 3.8 or newer
- No third-party packages required

## How to run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

4. Select an option from the menu and follow the prompts.

## Example

Suppose you enter these text states in order:

1. `Hello`
2. `Hello World`
3. `Hello World!`

Selecting **Undo** changes the current text from `Hello World!` to `Hello World`. Selecting Undo again restores `Hello`. Selecting **Redo** returns the text to `Hello World`.

## How stacks are used

The program uses two Python lists as stacks:

- **Undo stack:** stores previous text states.
- **Redo stack:** stores states that have been undone and can be restored.

The `append()` method pushes a state onto a stack, while `pop()` removes the most recently added state. This is LIFO: Last In, First Out.

When a new edit is made after an undo, the redo stack is cleared because the previous redo path is no longer valid.

## Project structure

```text
undo-redo-text-editor/
├── main.py
├── tests/
│   └── test_text_editor.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Run the tests

From the project folder, run:

```bash
python -m unittest discover -s tests -v
```

## Complexity

The stack push and pop operations are O(1) amortised and O(1), respectively. These estimates describe stack operations; storing or copying large text values may require additional time and memory.

## Limitations and possible improvements

This is an educational example that stores complete text states, rather than individual editing commands. A production text editor may use edit operations or more advanced history mechanisms to reduce memory usage. Possible extensions include saving text to a file, limiting history size, and adding a graphical user interface.

## Learning objectives

- Explain the stack and the LIFO principle.
- Demonstrate push and pop operations.
- Apply stacks to a practical software feature.
- Test edge cases such as undoing or redoing when history is empty.

## License

This project is provided for educational use. Add a license if you intend to distribute or reuse it under specific terms.
