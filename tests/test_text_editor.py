import unittest

from main import TextEditor


class TestTextEditor(unittest.TestCase):
    def setUp(self):
        self.editor = TextEditor()

    def test_initial_state_is_empty(self):
        self.assertEqual(self.editor.current_text, "")
        self.assertEqual(self.editor.undo_stack, [])
        self.assertEqual(self.editor.redo_stack, [])

    def test_edit_and_undo(self):
        self.editor.edit("Hello")
        self.editor.edit("Hello World")

        self.assertEqual(self.editor.current_text, "Hello World")
        self.assertTrue(self.editor.undo())
        self.assertEqual(self.editor.current_text, "Hello")

    def test_redo_restores_undone_state(self):
        self.editor.edit("Hello")
        self.editor.edit("Hello World")

        self.assertTrue(self.editor.undo())
        self.assertTrue(self.editor.redo())
        self.assertEqual(self.editor.current_text, "Hello World")

    def test_multiple_undos_follow_lifo(self):
        self.editor.edit("A")
        self.editor.edit("AB")
        self.editor.edit("ABC")

        self.assertTrue(self.editor.undo())
        self.assertEqual(self.editor.current_text, "AB")
        self.assertTrue(self.editor.undo())
        self.assertEqual(self.editor.current_text, "A")

    def test_new_edit_clears_redo_history(self):
        self.editor.edit("A")
        self.editor.edit("AB")
        self.editor.undo()

        self.assertTrue(self.editor.redo())
        self.assertEqual(self.editor.current_text, "AB")

        self.editor.undo()
        self.editor.edit("AC")
        self.assertEqual(self.editor.current_text, "AC")
        self.assertFalse(self.editor.redo())

    def test_undo_when_stack_is_empty(self):
        self.assertFalse(self.editor.undo())
        self.assertEqual(self.editor.current_text, "")

    def test_redo_when_stack_is_empty(self):
        self.assertFalse(self.editor.redo())
        self.assertEqual(self.editor.current_text, "")

    def test_editing_same_text_does_not_add_history(self):
        self.editor.edit("Hello")
        self.assertFalse(self.editor.edit("Hello"))
        self.assertEqual(len(self.editor.undo_stack), 1)

    def test_clear_can_be_undone(self):
        self.editor.edit("Some text")
        self.assertTrue(self.editor.clear())
        self.assertEqual(self.editor.current_text, "")
        self.assertTrue(self.editor.undo())
        self.assertEqual(self.editor.current_text, "Some text")

    def test_clearing_empty_text_does_nothing(self):
        self.assertFalse(self.editor.clear())
        self.assertEqual(self.editor.undo_stack, [])


if __name__ == "__main__":
    unittest.main()
