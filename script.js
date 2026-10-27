(() => {
  'use strict';
  const editor = document.getElementById('editor');
  const undoBtn = document.getElementById('undoBtn');
  const redoBtn = document.getElementById('redoBtn');
  const clearBtn = document.getElementById('clearBtn');
  const undoCount = document.getElementById('undoCount');
  const redoCount = document.getElementById('redoCount');
  const undoVisual = document.getElementById('undoVisual');
  const redoVisual = document.getElementById('redoVisual');
  const wordCount = document.getElementById('wordCount');
  const charCount = document.getElementById('charCount');
  const saveStatus = document.getElementById('saveStatus');
  const toast = document.getElementById('toast');
  const themeToggle = document.getElementById('themeToggle');
  // Arrays are used as stacks: push adds a state and pop removes the newest one.
  const undoStack = [];
  const redoStack = [];
  let previousValue = editor.value;
  let ignoreNextInput = false;
  let toastTimer;

  function updateStats() {
    const text = editor.value;
    const trimmed = text.trim();
    const words = trimmed ? trimmed.split(/\s+/).length : 0;
    wordCount.textContent = words + (words === 1 ? ' word' : ' words');
    charCount.textContent = text.length + (text.length === 1 ? ' character' : ' characters');
  }

  function renderStack(stack, container, emptyMessage) {
    container.replaceChildren();
    if (!stack.length) {
      const empty = document.createElement('span');
      empty.className = 'empty-stack';
      empty.textContent = emptyMessage;
      container.appendChild(empty);
      return;
    }
    stack.slice(-5).forEach((state, index, visible) => {
      const block = document.createElement('div');
      block.className = 'stack-block' + (index === visible.length - 1 ? ' top-block' : '');
      const tag = document.createElement('small');
      tag.textContent = index === visible.length - 1 ? 'TOP' : String(index + 1).padStart(2, '0');
      const preview = document.createElement('span');
      preview.textContent = state.replace(/\s+/g, ' ').trim() || '(empty text state)';
      block.title = state || '(empty text state)';
      block.append(tag, preview);
      container.appendChild(block);
    });
  }

  function updateUI() {
    undoBtn.disabled = undoStack.length === 0;
    redoBtn.disabled = redoStack.length === 0;
    undoCount.textContent = undoStack.length + (undoStack.length === 1 ? ' state' : ' states');
    redoCount.textContent = redoStack.length + (redoStack.length === 1 ? ' state' : ' states');
    renderStack(undoStack, undoVisual, 'Your history starts here');
    renderStack(redoStack, redoVisual, 'Nothing to redo yet');
    updateStats();
  }

  function notify(message) {
    toast.textContent = message;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 1900);
  }

  function restoreState(value) {
    ignoreNextInput = true;
    editor.value = value;
    previousValue = value;
    editor.focus();
    editor.setSelectionRange(value.length, value.length);
    saveStatus.textContent = 'Changes in this session';
    updateUI();
  }

  editor.addEventListener('input', () => {
    if (ignoreNextInput) {
      ignoreNextInput = false;
      previousValue = editor.value;
      updateUI();
      return;
    }
    if (editor.value !== previousValue) {
      undoStack.push(previousValue);
      previousValue = editor.value;
      redoStack.length = 0;
      saveStatus.textContent = 'Changes in this session';
      updateUI();
    }
  });

  function undo() {
    if (!undoStack.length) return notify('Nothing to undo');
    redoStack.push(editor.value);
    restoreState(undoStack.pop());
    notify('Last edit undone');
  }

  function redo() {
    if (!redoStack.length) return notify('Nothing to redo');
    undoStack.push(editor.value);
    restoreState(redoStack.pop());
    notify('Edit restored');
  }

  undoBtn.addEventListener('click', undo);
  redoBtn.addEventListener('click', redo);
  clearBtn.addEventListener('click', () => {
    if (!editor.value) return notify('The document is already empty');
    undoStack.push(editor.value);
    redoStack.length = 0;
    restoreState('');
    notify('Text cleared — you can undo this');
  });

  document.addEventListener('keydown', event => {
    if (!(event.ctrlKey || event.metaKey)) return;
    if (event.key.toLowerCase() === 'z' && event.shiftKey) {
      event.preventDefault(); redo();
    } else if (event.key.toLowerCase() === 'z') {
      event.preventDefault(); undo();
    } else if (event.key.toLowerCase() === 'y') {
      event.preventDefault(); redo();
    }
  });

  themeToggle.addEventListener('click', () => {
    const dark = document.body.classList.toggle('dark');
    themeToggle.textContent = dark ? '☾' : '☼';
    themeToggle.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
  });

  updateUI();
})();