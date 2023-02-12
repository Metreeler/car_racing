import unittest
import os
from src.main.python.editor import Editor
from src.main.python.wall import Wall
from src.main.python.gate import Gate


class EditorTest(unittest.TestCase):
    # This method is called to test the good initialization of the editor class
    def test_editor_initialization(self):
        editor = Editor()
        self.assertEqual(len(editor.wall_list), 0)
        self.assertEqual(len(editor.gate_list), 0)
        self.assertEqual(editor.car_position, (-1, -1))
        self.assertFalse(editor.walls)
        self.assertFalse(editor.gates)
        self.assertFalse(editor.car)
        self.assertEqual(editor.mouse_x1, 0)
        self.assertEqual(editor.mouse_y1, 0)
        self.assertEqual(editor.x1, -1)
        self.assertEqual(editor.x2, -1)
        self.assertEqual(editor.y1, -1)
        self.assertEqual(editor.y2, -1)
        self.assertEqual(editor.start_wall_x1, -1)
        self.assertEqual(editor.start_wall_y1, -1)
        self.assertFalse(editor.new_wall)
        self.assertFalse(editor.delete_last)
        del editor

    # This method is called to test the save method of the editor class
    def test_editor_save_method(self):
        editor = Editor()
        editor.wall_list.append(Wall(0, 0, 5, 5))
        editor.gate_list.append(Gate(10, 10, 5, 5))
        editor.car_position = (20, 20)
        file_path = "./assets/maps/map_for_test_editor"
        editor.save(file_path)
        f = open("./assets/maps/map_for_test_editor", "r")
        lines = []
        for line in f:
            lines.append(line)
        self.assertEqual(lines[0], "WALLS\n")
        self.assertEqual(lines[1], "0,0,5,5\n")
        self.assertEqual(lines[2], "GATES\n")
        self.assertEqual(lines[3], "10,10,5,5\n")
        self.assertEqual(lines[4], "CAR\n")
        self.assertEqual(lines[5], "20,20")
        del editor
        f.close()
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
