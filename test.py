import unittest

from main import *


class MyTestCase(unittest.TestCase):
	def test_maze_solver(self):
		tests = [
			(  # 0
				[],
				[],
			),
			(  # 1
				[[]],
				[],
			),
			(  # 2
				[[], []],
				[],
			),
			(  # 3
				[[CELL_EMPTY]],
				[(0, 0)],
			),
			(  # 4
				[[CELL_UP_RIGHT]],
				[(0, 0)],
			),
			(  # 5
				[[CELL_EMPTY, CELL_EMPTY]],
				[(0, 0), (0, 1)],
			),
			(  # 6
				[[CELL_UP_RIGHT, CELL_EMPTY]],
				[(0, 0)],
			),
			(  # 7
				[[CELL_DOWN_RIGHT], [CELL_EMPTY]],
				[(0, 0), (1, 0)],
			),
			(  # 8
				[[CELL_EMPTY, CELL_DOWN_RIGHT], [CELL_DOWN_RIGHT, CELL_UP_RIGHT]],
				[(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)],
			),
			(  # 9
				[[CELL_EMPTY, CELL_DOWN_RIGHT], [CELL_EMPTY, CELL_DOWN_RIGHT]],
				[(0, 0), (0, 1), (1, 1)],
			),
			(  # 10
				[[CELL_DOWN_RIGHT, CELL_UP_RIGHT], [CELL_DOWN_RIGHT, CELL_UP_RIGHT]],
				[(0, 0), (1, 0), (1, 1), (0, 1)],
			),
			(  # 11
				[[0, 0, 0, -1], [1, 0, 0, 1], [0, 0, 0, 0], [-1, 0, 0, 0]],
				[(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2),
					(3, 3)],
			),
		]

		for i, test in enumerate(tests):
			self.assertEqual(test[1], maze_solver(test[0]), i)

		with self.assertRaises(Exception):
			validate_maze([[2]])

	def test_validate_maze(self):
		validate_maze([])
		validate_maze([[]])

		with self.assertRaises(Exception):
			validate_maze([[2]])

		with self.assertRaises(Exception):
			validate_maze([[], [1]])


if __name__ == '__main__':
	unittest.main()
