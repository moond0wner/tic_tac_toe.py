# 1. Функция вывода поля
# 2. Выбор пользователя
# 3. Выбор компьютера (модуль рандом)
# 4. Заменить позиции пользователя и компьютера подчеркивания X и O
# 5. Выявление победителя

import random
game_map = [
    ['_', "_", "_"],
    ['_', '_', '_'],
    ['_', '_', '_']
]

def print_map():
    for i in game_map:
        for j in i:
            print(j, end='')
        print()
        
        
        
def game():
    isFullX = False
    isFullO = False
    print_map()
    while (not(isFullX) or not(isFullO)):
        choose_pos()
        check_winner()
        

def choose_pos():
    player_row, player_el = int(input("Введите номер строчки (от 1 до 3): ")), int(input("Введите номер клетки в строчке (от 1 до 3): "))
    computer_row, computer_el = random.randint(0, 2), random.randint(0, 2)
    if 1 <= player_row <= 3 and 1 <= player_el <= 3:
        if (player_row - 1 + player_row - 1) == (computer_row + computer_el):
            print("Пользователь и компьютер выбрали одинаковую позицию. Вам нужно выбрать позицию ещё раз.")
            choose_pos()
        else:
            if game_map[computer_row][computer_el] == "_":
                game_map[player_row - 1][player_el - 1] = "X"
                game_map[computer_row][computer_el] = "O"
                print_map()
                return
            else:
                print("Компьютер занял эту клетку, выберите другую.")
                choose_pos()
    else:
        print("Неправильный ввод!")
        choose_pos()


def check_winner():
    global isFullX, isFullO
    for row in range(len(game_map)):
        isFullX = True
        isFullO = True
        
        for element in range(len(game_map[row])):
            if game_map[row][element] != "X":
                isFullX = False
            if game_map[row][element] != "O":
                isFullO = False
                        
    if game_map[0][0] == "X" and game_map[1][1] == "X" and game_map[2][2] == "X":
        print("Ничего себе, Вы заполнили главную диагональ. Вы выиграли!")
        print_map()

    if game_map[0][2] == "X" and game_map[1][1] == "X" and game_map[2][0] == "X":
        print("Ничего себе, Вы заполнили побочную диагональ. Вы выиграли!")
        print_map()

    if game_map[0][0] == "O" and game_map[1][1] == "O" and game_map[2][2] == "O":
        print("Ничего себе, компьютер заполнил главную диагональ. Вы проиграли.")
        print_map()

    if game_map[0][2] == "O" and game_map[1][1] == "O" and game_map[2][0] == "O":
        print("Ничего себе, компьютер заполнили побочную диагональ. Вы проиграли.")
        print_map()
        
                                    
game()
