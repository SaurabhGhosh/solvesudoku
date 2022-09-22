import copy

from .solvesudoku import Recursion

# Create instance
recurse = Recursion()
# Deep copy the original board to the temporary board so that the original board is not affected
recurse.temp_board = copy.deepcopy(recurse.board)
# Start the recursion
if recurse.solve_board():
    # Display the board finally
    recurse.display_board()
    print('Solved board!!')
else:
    print('Not solved')