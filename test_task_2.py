import unittest
from task_2 import task

class TestTask1(unittest.TestCase):
    def test_task_2(self):
        self.assertEquals(task(1, 1, 2, 2, 3, 3, 4, 4), 'Rectangles do not intersect')
        self.assertEquals(task(1, 1, 2, 2, 0, 0, 3, 3), 'Rectangles intersect. Square of intersection: 1')
        self.assertEquals(task(1, 1, 2, 2, 3, 3, 0, 0), 'Rectangles intersect. Square of intersection: 1')
        self.assertRaises(ValueError, task, *[1, 1, 3, 3, 2, 2, 2, 2])
