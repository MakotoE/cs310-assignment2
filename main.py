from typing import List, Tuple

CELL_EMPTY = 0
CELL_DOWN_RIGHT = -1
CELL_UP_RIGHT = 1

DIRECTION_RIGHT = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_UP = 3


def maze_solver(maze: List[List[int]]) -> List[Tuple[int, int]]:
	validate_maze(maze)

	coordinate = (0, 0)
	direction = DIRECTION_RIGHT

	path: List[Tuple[int, int]] = []

	while True:
		if 0 <= coordinate[1] < len(maze) and 0 <= coordinate[0] < len(maze[0]):
			path.append(coordinate)
			direction = next_direction(direction, maze[coordinate[1]][coordinate[0]])
			coordinate = next_coordinate(coordinate, direction)
		else:
			return path


def validate_maze(maze: List[List[int]]):
	if len(maze) == 0:
		return

	columns = len(maze[0])
	for row in maze:
		if len(row) != columns:
			raise Exception('row length is not equal')

		for cell in row:
			if cell not in [CELL_EMPTY, CELL_DOWN_RIGHT, CELL_UP_RIGHT]:
				raise Exception('invalid cell')


def next_direction(current_direction: int, cell: int) -> int:
	if cell == CELL_EMPTY:
		return current_direction

	return {
		DIRECTION_RIGHT: {
			CELL_DOWN_RIGHT: DIRECTION_DOWN,
			CELL_UP_RIGHT: DIRECTION_UP,
		},
		DIRECTION_DOWN: {
			CELL_DOWN_RIGHT: DIRECTION_RIGHT,
			CELL_UP_RIGHT: DIRECTION_LEFT,
		},
		DIRECTION_LEFT: {
			CELL_DOWN_RIGHT: DIRECTION_UP,
			CELL_UP_RIGHT: DIRECTION_DOWN,
		},
		DIRECTION_UP: {
			CELL_DOWN_RIGHT: DIRECTION_LEFT,
			CELL_UP_RIGHT: DIRECTION_RIGHT,
		},
	}[current_direction][cell]


def next_coordinate(coordinate: Tuple[int, int], direction: int) -> Tuple[int, int]:
	if direction == DIRECTION_RIGHT:
		return coordinate[0] + 1, coordinate[1]
	elif direction == DIRECTION_DOWN:
		return coordinate[0], coordinate[1] + 1
	elif direction == DIRECTION_LEFT:
		return coordinate[0] - 1, coordinate[1]
	elif direction == DIRECTION_UP:
		return coordinate[0], coordinate[1] - 1
	else:
		assert False
