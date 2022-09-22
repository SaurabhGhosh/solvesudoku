import copy
import os
import time


class Recursion:
    """ This class contains all the methods and attributes for solving the popular puzzle - Sudoku!!
        There are many ways to implement a code for solving Sudoku. This class uses the recursive method."""
    # This is the puzzle board with blank places marked as '0' (zero)
    board = [[3, 4, 0, 0, 6, 0, 2, 0, 9],
             [2, 0, 8, 4, 9, 0, 0, 0, 6],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 2, 0, 3, 1, 0, 0, 0, 0],
             [0, 0, 4, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 2, 5, 0, 4, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [9, 0, 0, 0, 5, 1, 4, 0, 3],
             [4, 0, 3, 0, 7, 0, 0, 6, 8]]

    # Temporary board which will get updated throughout the program towards solving the puzzle
    temp_board = [[] * 3] * 3

    def check_in_row(self, row, val):
        """This method takes the row index and a value as input.
        Returns True if the value is present in the row of the solving board. Otherwise, returns False."""
        return val in self.temp_board[row]

    def check_in_column(self, col, val):
        """This method takes the column index and a value as input.
        Returns True if the value is present in the column of the solving board.
        Otherwise, returns False."""
        # Using list comprehension to prepare a temporary list of the column values and checking presence in it
        return val in [x[col] for x in self.board]

    def check_in_cube(self, row, col, val):
        """This method takes the row and column indexes and a value as input.
        It determines the starting row, column indexes for the smaller matrix (3x3) within board to check.
        Returns True if the value is present in the smaller matrix of the solving board.
        Otherwise, returns False."""
        # Determines the starting row and column indexes by subtracting the remainder (division by 3) from
        # the row and column values
        cube_start_row = row - row % 3
        cube_start_col = col - col % 3
        # Prepares a temporary list of 9 places from the (3x3) matrix by using list comprehension.
        # Checks if the value is present in the temporary list.
        return val in [y for x in self.board[cube_start_row:(cube_start_row + 3)] for y in
                       x[cube_start_col:(cube_start_col + 3)]]

    def is_allowed(self, row, col, val):
        """This method takes the row and column indexes and a value as input.
        It internally calls the other methods to check whether the value appears in the row, column or the (3x3) matrix around the position.
        Returns True if the value is present. Otherwise, returns False."""
        return not (self.check_in_row(row, val) or self.check_in_column(col, val) or self.check_in_cube(row, col, val))

    def solve_board(self):
        """This method includes the recursive logic to solve the puzzle.
        For every position, it checks if the position is blank and assigns a possible number by calling is_allowed().
        The method makes recursive call to solve after this assignment. If all possible numbers are tried i.e. 1-9
        and no number is found as possible, it returns the call as False.
        When False is returned, the previous recursive instance tries to assign the next possible value from 1-9
        and rerun the recursive call again.
        This continues till last position. As the recursion progresses, number of possible values for a position
        reduces because most of the previous positions are filled already.
        When all the places are exhausted and no False is returned, method returns True indicating that the
        board is solved."""
        # Display the sudoku board
        self.display_board()
        # Iterate over the rows
        for row in range(9):
            # Iterate over the columns
            for col in range(9):
                # Check if the position is blank
                if self.temp_board[row][col] == 0:
                    # Iterate through the number 1 to 9 as possible value for the position
                    for val in range(1, 10):
                        # Check if the number is allowed
                        if self.is_allowed(row, col, val):
                            # Assign the value if allowed
                            self.temp_board[row][col] = val
                            # Return True if the recursive call returned True
                            if self.solve_board():
                                return True
                            else:
                                # If the recursive method returned False (meaning that assigned value did not work),
                                # make the position blank again before trying to reassign another value or before
                                # moving back to the previous position
                                self.temp_board[row][col] = 0
                    # Return False if none of the values worked - program will move to the next position and try the
                    # recursion again
                    return False
        # Return true when all the positions are exhausted meaning all positions successfully passed the rule check
        # through is_allowed() method and got a number assigned
        return True

    def display_board(self):
        """This method prints the sudoku board"""
        # Used sleep() to give a visual idea while the recursion progresses
        time.sleep(0.1)
        # Clear the screen to print on same place
        os.system('cls')
        print()
        # Print all the positions in a row with *
        for i in range(9):
            print(*self.temp_board[i])


# Check whether the game is executed from command
if __name__ == '__main__':
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
