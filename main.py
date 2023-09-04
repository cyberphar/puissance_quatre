import random

playerone = 'r'
playertwo = 'y'

from colorama import Fore, Style

len_grid = (6,7)

def init(len_grid):
    grid = []
    for i in range(len_grid[0]):
        grid.append([])
        for j in range(len_grid[1]):
            grid[i].append('0')
    return grid

def print_grid(grid):
    for line in grid:
        for case in line:
            if case == 'r':
                print(Fore.RED + '0', end='  ')
            elif case == 'y':
                print(Fore.YELLOW + '0', end='  ')
            else:
                print(Fore.WHITE + '.', end='  ')
        print()
    print(Style.RESET_ALL)

def verif_line_bis(grid, col, row):
    win = 4
    cpt = 1
    temp = grid[row][col]
    if temp == '0':
        return 0
    
    # Vérification horizontale
    col_temp = col
    while (col_temp > 0 and grid[row][col_temp-1] == temp):
        cpt += 1
        col_temp -= 1
    col_temp = col
    while (col_temp < len(grid[0])-1 and grid[row][col_temp+1] == temp):
        cpt += 1
        col_temp += 1
    
    if cpt >= win:
        return 1
    
    # Vérification verticale
    cpt = 1
    row_temp = row
    while (row_temp > 0 and grid[row_temp-1][col] == temp):
        cpt += 1
        row_temp -= 1
    row_temp = row
    while (row_temp < len(grid)-1 and grid[row_temp+1][col] == temp):
        cpt += 1
        row_temp += 1
    
    if cpt >= win:
        return 1
    
    return 0

def verif_line(grid):
    col = 3
    for row in range(len(grid)):
        if verif_line_bis(grid, col, row) == 1:
            return 1
    return 0

def verif_col(grid):
    row = 3
    for col in range(len(grid[0])):
        if verif_line_bis(grid, col, row) == 1:
            return 1
    return 0

def verif_diag_bis(grid, row, col):
    if grid[row][col] == '0':
        return 0
    win = 4
    cpt = 1
    row_temp = row
    col_temp = col
    temp = grid[row][col]
    while (row_temp > 0 and col_temp > 0 and grid[row_temp-1][col_temp-1] == temp):
        cpt += 1
        row_temp -= 1
        col_temp -= 1
    row_temp = row
    col_temp = col
    while (col_temp < len(grid)-1 and row_temp < len(grid)-1 and grid[row_temp+1][col] == temp):
        cpt += 1
        row_temp += 1
        col_temp -= 1
    
    if cpt >= win:
        return 1
    return 0

def verif_diag(grid):
    for col in range(len(grid)):
        if (verif_diag_bis(grid, 3, col)):
            return 1
    return 0


def complete_verif(grid):
    return verif_line(grid) or verif_col(grid) or verif_diag(grid)


def play(grid, col, player):
    if (grid[0][col] != '0'):
        return 0
    else:
        i = len_grid[0] - 1
        while i > 0 and grid[i][col] != '0':
            i -= 1
        grid[i][col] = player
        return 1

def refresh(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = '0'
    return 1

def is_not_full(grid):
    for i in range(9):
        if grid[0][i] == '0':
            return 1
    else:
        return 0

grid = init(len_grid)
while 1:
    tour = random.randint(0,1)
    while not complete_verif(grid) and is_not_full(grid):
        if tour % 2 == 0:
            print("Player 1:")
            print_grid(grid)
            col = int(input("Quelle colonne: "))
            col -= 1
            while (play(grid, col, playerone) != 1):
                print("Coup invalide. Rejouer.")
                print("Player 1:")
                print_grid(grid)
                col = int(input("Quelle colonne: "))
                col -= 1
        else:
            print("Player 2:")
            print_grid(grid)
            col = int(input("Quelle colonne: "))
            col -= 1
            while (play(grid, col, playertwo) != 1):
                print("Player 2:")
                print_grid(grid)
                print("Coup invalide. Rejouer.")
                col = int(input("Quelle colonne: "))
                col -= 1
            
        tour += 1
    if (complete_verif and tour % 2 == 0):
        print("Le joueur 2 a gagne !")
    elif (complete_verif and tour % 2 == 1):
        print("Le joueur 1 a gagne !")
    else:
        print("Match nul !")
    print_grid(grid)
    choose = input("Nouvelle partie [o/n] : ")
    tour = 0
    if choose != 'o':
        break
    refresh(grid)

    
    
