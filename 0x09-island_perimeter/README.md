# ISLAND PERIMETER
- A function island_perimeter(grid) that returns the perimeter of the island described in grid
	* grid is a list of intergers:
		* 0 represents water
		* 1 represents land 
		* Cells are connected horizontally/vertically ( not diagonally).
		* grid is rectangular with its width and height not exceeding 100
	* The grid is compeletely surrounded by water
	* The is only one island(or nothing)
	* The island doesn't have lakes (water inside that isn't connected to the water surrounding the island)
# SAMPLE GRID
	grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
# OUTPUT
    12
