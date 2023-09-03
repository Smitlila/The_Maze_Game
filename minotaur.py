import random
from maze import Maze
from hero import Hero
class Minotaur:
    """
    A class representing the monster that guards the maze.
    Attributes:
    row: an integer representing the current row of the minotaur.
    col: an integer representing the current column of the minotaur.
    direction: a string representing the current direction of the minotaur.
    turns: an integer representing the number of turns since the last direction change.

    Methods:
    _init_(self): randomizes the starting location of the minotaur to any blank space in the maze. Place an 'M' at that spot. Set the direction to a random value and turns to 0.
    get_search_dir(self): chooses the direction that the minotaur will move in.
    move_minotaur(self): every third turn the minotaur will detect the hero's location in the maze and update its direction by calling _get_search_dir. Using the determined direction, update the minotaur's location (row and col attributes) if the space is not a wall ('*') or the finish ('f'). Overwrite the old 'M' with a space and place a new 'M' at the updated position. Return the character that was at that location so that main knows whether the minotaur captured the hero.
    """
    def __init__(self,maze):
        maze = Maze()
        while True:
            row = random.randint(0, len(Maze()) - 1)
            col = random.randint(0, len(Maze()[0]) - 1)
            if Maze()[row][col] == ' ':
                self.row = row
                self.col = col
                break
        Maze()[self.row][self.col] = 'M'
        self.direction = random.choice(['U', 'D', 'L', 'R'])
        self.turns = 0

    def get_search_dir(self):
        if self.turns % 3 == 0:
            hero_row, hero_col = Hero().row, Hero().col
            minotaur_row, minotaur_col = self.row, self.col
            if hero_row < minotaur_row and Maze()[minotaur_row - 1][minotaur_col] != '*':
                self.direction = 'U'
            elif hero_row > minotaur_row and Maze()[minotaur_row + 1][minotaur_col] != '*':
                self.direction = 'D'
            elif hero_col < minotaur_col and Maze()[minotaur_row][minotaur_col - 1] != '*':
                self.direction = 'L'
            elif hero_col > minotaur_col and Maze()[minotaur_row][minotaur_col + 1] != '*':
                self.direction = 'R'
            else:
                self.direction = random.choice(['U', 'D', 'L', 'R'])
        else:
            self.direction = random.choice(['U', 'D', 'L', 'R'])

    def move_minotaur(self):
        self.turns += 1
        self.get_search_dir()
        old_char = Maze()[self.row][self.col]
        if self.direction == 'U' and self.row > 0 and Maze()[self.row - 1][self.col] not in ['*', 'f']:
            Maze()[self.row][self.col] = ' '
            self.row -= 1
            Maze()[self.row][self.col] = 'M'
        elif self.direction == 'D' and self.row < len(Maze()) - 1 and Maze()[self.row + 1][self.col] not in ['*', 'f']:
            Maze()[self.row][self.col] = ' '
            self.row += 1
            Maze()[self.row][self.col] = 'M'
        elif self.direction == 'L' and self.col > 0 and Maze()[self.row][self.col - 1] not in ['', 'f']:
            Maze()[self.row][self.col] = ' '
            self.col -= 1
            Maze()[self.row][self.col] = 'M'
        elif self.direction == 'R' and self.col < len(Maze()[0]) - 1 and Maze()[self.row][self.col + 1] not in ['', 'f']:
            Maze()[self.row][self.col] = ' '
            self.col += 1
            Maze()[self.row][self.col] = 'M'
        else:
            return old_char
        if Maze()[self.row][self.col] == 'H':
            return 'X'
        else:
            return Maze()[self.row][self.col]