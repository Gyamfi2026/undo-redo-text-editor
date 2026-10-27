# StackWrite — Undo/Redo Text Editor

StackWrite is a responsive, browser-based text editor that demonstrates a real-world use of the **stack** data structure. It is built with **HTML, CSS, and JavaScript**.

## Real-world application

Text editors and word processors provide Undo and Redo features. Undo reverses the most recent edit, while Redo restores an edit that was undone. Stacks are a natural fit because they follow the **Last In, First Out (LIFO)** principle.

## Features

- Responsive, clean writing interface.
- Undo and Redo buttons.
- Keyboard shortcuts: **Ctrl/Cmd + Z** for Undo, **Ctrl/Cmd + Shift + Z** or **Ctrl/Cmd + Y** for Redo.
- Live word and character counts.
- Visual displays of the Undo and Redo stacks.
- Clear text with the option to undo the clear.
- Light/dark theme toggle.
- Accessible labels and helpful messages.
- No package installation or build tools required.

## Run the application

1. Open this repository on GitHub and download the ZIP, or clone it.
2. Keep `index.html`, `styles.css`, and `script.js` in the same folder.
3. Open `index.html` in a modern web browser.

You can also use the VS Code **Live Server** extension to preview the app locally. The app runs entirely in your browser.

## Project structure

```text
undo-redo-text-editor/
├── index.html   # Page structure and accessible controls
├── styles.css   # Responsive styling and light/dark themes
├── script.js    # Undo/redo stack logic and interface behaviour
├── README.md    # Project overview and instructions
└── .gitignore
```

## How stacks are used

The JavaScript application uses two arrays as stacks:

- **Undo stack:** stores earlier text states.
- **Redo stack:** stores states that were undone and may be restored.

When the text changes, the previous state is pushed onto the Undo stack and the Redo stack is cleared. Undo pushes the current text onto the Redo stack, then pops the latest state from the Undo stack. Redo does the reverse.

The arrays' `push()` and `pop()` methods implement the LIFO behaviour. The interface visualises the most recent states at the top of each stack.

## Complexity

Stack push and pop operations are O(1) amortised and O(1), respectively. These estimates apply to the stack operations; handling and displaying text takes time proportional to the text length.

## Limitations and possible improvements

This is an educational project that stores text states in the browser session. Refreshing the page clears the editing history. Future improvements could include saving documents, persisting history with local storage, limiting the history size, and adding automated browser tests.

## Learning objectives

- Explain the stack and the LIFO principle.
- Demonstrate push and pop operations.
- Apply stacks to a practical Undo/Redo feature.
- Connect data-structure logic to a user-friendly web interface.

## License

Provided for educational use. Add a license file if you plan to distribute the project under specific terms.
