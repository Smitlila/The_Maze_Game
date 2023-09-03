from maze import Maze

class Hero:
    def __init__(self):
        self.row, self.col = Maze().find_start()
        Maze()[self.row][self.col] = 'H'

    def go_up(self):
        if self.row > 0 and Maze()[self.row - 1][self.col] != '*':
            old_char = Maze()[self.row][self.col]
            Maze()[self.row][self.col] = ' '
            self.row -= 1
            Maze()[self.row][self.col] = 'H'
            return old_char
        return '*'

    def go_down(self):
        if self.row < len(Maze()) - 1 and Maze()[self.row + 1][self.col] != '*':
            old_char = Maze()[self.row][self.col]
            Maze()[self.row][self.col] = ' '
            self.row += 1
            Maze()[self.row][self.col] = 'H'
            return old_char
        return '*'

    def go_left(self):
        if self.col > 0 and Maze()[self.row][self.col - 1] != '*':
            old_char = Maze()[self.row][self.col]
            Maze()[self.row][self.col] = ' '
            self.col -= 1
            Maze()[self.row][self.col] = 'H'
            return old_char
        return '*'

    def go_right(self):
        if self.col < len(Maze()[0]) - 1 and Maze()[self.row][self.col + 1] != '*':
            old_char = Maze()[self.row][self.col]
            Maze()[self.row][self.col] = ' '
            self.col += 1
            Maze()[self.row][self.col] = 'H'
            return old_char
        return '*'
