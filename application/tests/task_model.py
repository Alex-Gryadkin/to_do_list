import unittest
from application.models import Task


class TestTaskModel(unittest.TestCase):

    def test_Task_WHEN_instance_created_with_a_description_THEN_the_description_is_an_instance_attribute(self):
        # GIVEN
        expected = 'to do #1'

        # WHEN
        task1 = Task(task_descr=expected)

        # THEN
        self.assertEqual(task1.task_descr, expected)