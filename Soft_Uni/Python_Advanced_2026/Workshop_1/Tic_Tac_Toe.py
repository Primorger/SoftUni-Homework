import sys

#------Function Definision------#

def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    sys.stdout.flush()

def print_board_matrix():
    pass

#------Variable Definition------#

player_symbols = ("X", "O")
board_matrix = []

#-------Get Initial Input-------#

player_1_name = input("Player one name: ")
player_2_name = input("Player two name: ")

#----Symbol Allocation Block----#

player_1_symbol = input(f"{player_1_name} choose from 'X' or 'O': ").upper()
if player_1_symbol not in player_symbols:

    while True:  
        player_1_symbol = input(f"Input a valid symbol: ").upper()
        if player_1_symbol in player_symbols:
            break
        delete_last_line()

if player_1_symbol == "X":
    player_2_symbol = "O"
else:
    player_2_symbol = "X"

#-----Print Cell Numeration-----#

print("This is the numeration of the board: ")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")
print(f"{player_1_name} starts first!")

#-----------Game Loop-----------#



#-------------------------------#