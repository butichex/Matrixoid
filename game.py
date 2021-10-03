# Дютин Тимур, ПИ-2-21

from pynput.keyboard import Key, Listener
import os 
from random import choice 

# Все зависимости можно установить через команду: pip install -r requirements.txt

def create_matrix(): 
    matrix = [["0" for i in range(10)] for j in range(10)]
    matrix[0][0] = "*"
    return matrix 

def fill_matrix_with_bombs(matrix): 


class Game: 
    def __init__(self): 
        self.x, self.y = [0, 0]
        self.matrix = create_matrix()
        self.moves = {Key.up: self.up_move, Key.down: self.down_move, Key.left: self.left_move, Key.right: self.right_move}
        self.print_matrix()
        self.start_game()

    def on_press(self, key):
        if key in self.moves.keys(): 
            self.moves[key]()
            self.print_matrix()

    def on_release(self, key):
        if key == Key.esc:
            return False

    def start_game(self): 
        with Listener(
        on_press=self.on_press,
        on_release=self.on_release) as listener: listener.join()


    def right_move(self):
        if self.y + 1 == len(self.matrix): 
            self.matrix[self.x][self.y] = "0"
            self.matrix[self.x][0] = "*"
            self.y = 0 
        else: 
            self.matrix[self.x][self.y] = "0"
            self.matrix[self.x][self.y + 1] = "*"
            self.y += 1

    def left_move(self):
        if self.y - 1 == -1: 
            self.matrix[self.x][self.y] = "0"
            self.matrix[self.x][len(self.matrix) - 1] = "*"
            self.y = len(self.matrix) - 1
        else: 
            self.matrix[self.x][self.y] = "0"
            self.matrix[self.x][self.y - 1] = "*"
            self.y -= 1

    def up_move(self):
        if self.x - 1 == -1: 
            self.matrix[self.x][self.y] = "0"
            self.matrix[len(self.matrix) - 1][self.y] = "*"
            self.x = len(self.matrix) - 1
        else: 
            self.matrix[self.x][self.y] = "0"
            self.matrix[self.x - 1][self.y] = "*"
            self.x -= 1

    def down_move(self):
        if self.x + 1 == len(self.matrix): 
            self.matrix[self.x][self.y] = "0"
            self.matrix[0][self.y] = "*"
            self.x = 0
        else: 
            self.matrix[self.x][self.y] = "0"
            self.matrix[self.x + 1][self.y] = "*"
            self.x += 1

    def print_matrix(self):
        os.system("cls")
        for row in self.matrix: 
            print(*row)
    

if __name__ == "__main__": 
    game = Game()
    game.start_game()