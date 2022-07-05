import unittest
from task_1 import task


class TestTask1(unittest.TestCase):
    def test_task_1(self):
        self.assertEqual(task([1, 1, 1, 0, 0]), 2)
        self.assertEqual(task("111000"), 2)
        self.assertEqual(task("111111111110000000000000000"), 10)
        self.assertRaises(ValueError, task, [1])
        self.assertRaises(ValueError, task, [1, 1, 1, 1, 1])
        self.assertRaises(ValueError, task, [0, 1, 1, 1, 1, 1])
        self.assertRaises(ValueError, task, ["some_text"])
        self.assertRaises(ValueError, task, [[1], [1], [1], [0], [0]])
