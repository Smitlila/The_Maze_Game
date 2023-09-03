class Maze:

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.__init__()
        return cls.instance

    def __init__(self):
        self.maze = []
        with open("maze.txt", "r") as f:
            for line in f:
                self.maze.append(list(line.strip()))

    def __getitem__(self, row):
        return self.maze[row]

    def __len__(self):
        return len(self.maze)

    def __str__(self):
        return "\n".join("".join(row) for row in self.maze)

    def find_start(self):
        for i, row in enumerate(self.maze):
            if 's' in row:
                return i, row.index('s')