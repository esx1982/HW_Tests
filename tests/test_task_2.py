from task_2 import ya_disk
from unittest import TestCase
import pytest


class Test_for_Task_1(TestCase):
    def test_1(self):
        expected = 409
        result = ya_disk.create_folder("mymymy")
        self.assertEqual(result, expected)

@pytest.mark.parametrize(
    'folder_name,expected', (
        ["mymymy", 409],
        ["my_folder", 409],
        ["new_folder", 201],
        ["new_folder_2", 201],
        ["mymymy", 201],
        ["my_folder", 201],
        ["new_folder", 409],
        ["new_folder_2", 409]
    )
)
def test_2(folder_name, expected):
    result = ya_disk.create_folder(folder_name)
    assert result == expected