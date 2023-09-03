import os
import maze
import hero
import minotaur 


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    maze = maze.Maze()
    hero = hero.Hero()
    minotaur = minotaur.Minotaur(maze)

    while True:
        clear_screen()
        print(maze),print(maze.Maze().find_start())
        direction = input("Enter a direction to move (WASD): ").upper()
        if direction == 'W':
            old_char = hero.go_up()
        elif direction == 'A':
            old_char = hero.go_left()
        elif direction == 'S':
            old_char = hero.go_down()
        elif direction == 'D':
            old_char = hero.go_left()    
        

        if old_char == 'f':
            print("Congratulations! You made it to the end!")
            break
        elif old_char == 'M':
            print("Oh no! The minotaur got you!")
            break
        elif old_char == '*':
            continue

        old_char = minotaur.move_minotaur()

        if old_char == 'X':
            print("Oh no! The minotaur got you!")
            break
    


if __name__ == '__main__':
    main()
    
