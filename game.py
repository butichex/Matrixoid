# Дютин Тимур, ПИ-2-21

from pynput.keyboard import Key, Listener, Controller
from pynput import keyboard
import os 
import sys 
from random import choice 

# Все зависимости можно установить через команду: pip install -r requirements.txt

def create_matrix(): 
    matrix = [["0" for i in range(10)] for j in range(10)]
    matrix[0][0] = "*"
    return matrix 

def fill_matrix_with_bombs(matrix): 
    for row in matrix: 
        for index in [choice(range(1, 10)) for _ in range(choice(range(0, 6)))]: 
            row[index] = "💣"
    return matrix

def fill_matrix_with_points(matrix): 
    for row in matrix: 
        for index in [choice(range(10)) for _ in range(1)]: 
            row[index] = "💫"
    return matrix


class Game: 
    def __init__(self): 
        self.x, self.y = [0, 0]
        self.points = 0
        self.matrix = create_matrix()
        self.matrix = fill_matrix_with_bombs(self.matrix)
        self.matrix = fill_matrix_with_points(self.matrix)
        self.moves = {Key.up: self.up_move, Key.down: self.down_move, Key.left: self.left_move, Key.right: self.right_move}
        self.print_matrix()
        self.start_game()

    def on_press(self, key):
        if key in self.moves.keys(): 
            self.moves[key]()
            self.check_bomb_position()
            self.check_point_position()
            self.print_matrix()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            exit()

    def start_game(self): 
        with Listener(
        on_press=self.on_press,
        on_release=self.on_release) as listener: listener.join()

    def check_point_position(self): 
        if self.matrix[self.x][self.y] == "💫": 
            self.points += 1 
            if self.points == 10: 
                self.print_matrix(with_exitcode="success")
            self.matrix[self.x][self.y] = "0"
            self.print_matrix()

    def check_bomb_position(self): 
        if self.matrix[self.x][self.y] == "💣": 
            self.matrix[self.x][self.y] = "💥"
            self.print_matrix(with_exitcode="failure")


    def right_move(self):
        if self.y + 1 == len(self.matrix): 
            self.matrix[self.x][self.y] = "0"
            if self.matrix[self.x][0] not in ["💣", "💫"]: 
                self.matrix[self.x][0] = "*"
            self.y = 0 
        else: 
            self.matrix[self.x][self.y] = "0"
            if self.matrix[self.x][self.y + 1] not in ["💣", "💫"]: 
                self.matrix[self.x][self.y + 1] = "*"
            self.y += 1

    def left_move(self):
        if self.y - 1 == -1:  
            self.matrix[self.x][self.y] = "0"
            if self.matrix[self.x][len(self.matrix) - 1] not in ["💣", "💫"]: 
                self.matrix[self.x][len(self.matrix) - 1] = "*"
            self.y = len(self.matrix) - 1
        else: 
            self.matrix[self.x][self.y] = "0"
            if self.matrix[self.x][self.y - 1] not in ["💣", "💫"]: 
                self.matrix[self.x][self.y - 1] = "*"
            self.y -= 1

    def up_move(self):
        if self.x - 1 == -1: 
            self.matrix[self.x][self.y] = "0"
            if  self.matrix[len(self.matrix) - 1][self.y] not in ["💣", "💫"]: 
                self.matrix[len(self.matrix) - 1][self.y] = "*"
            self.x = len(self.matrix) - 1
        else: 
            self.matrix[self.x][self.y] = "0"
            if  self.matrix[self.x - 1][self.y] not in ["💣", "💫"]: 
                self.matrix[self.x - 1][self.y] = "*"
            self.x -= 1

    def down_move(self):
        if self.x + 1 == len(self.matrix): 
            self.matrix[self.x][self.y] = "0"
            if self.matrix[0][self.y] not in ["💣", "💫"]: 
                self.matrix[0][self.y] = "*"
            self.x = 0
        else: 
            self.matrix[self.x][self.y] = "0"
            if self.matrix[self.x + 1][self.y] not in ["💣", "💫"]: 
                self.matrix[self.x + 1][self.y] = "*"
            self.x += 1

    def print_matrix(self, with_exitcode=None):
        os.system("cls")
        for row in self.matrix: 
            print(row)
        if with_exitcode == "failure": 
            print(f"Вы проиграли!. Ваш счёт: {self.points}")
            self.on_release(keyboard.Key.esc)
        elif with_exitcode == "success":
            print(f"Вы выиграли! Ваш счёт: {self.points}")
            self.on_release(keyboard.Key.esc)
        else: 
            print(f"Ваш счёт: {self.points}")




    

if __name__ == "__main__": 
    game = Game()
    game.start_game()