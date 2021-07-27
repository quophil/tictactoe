from os import system
import math

#function for clearing the terminal, displaying certain strings and for resetting the grid to its default state

def title_display():
    system('cls')
    print('\t###############')
    print('\t# Tic  O   X  #')
    print('\t#  O  Tac  X  #')
    print('\t#  X   O  Toe #')
    print('\t###############')

def grid_reset():
    global tictactoe_grid
    tictactoe_grid = """\n\t     |     |     
\t  1  |  2  |  3  
\t_____|_____|_____
\t     |     |     
\t  4  |  5  |  6  
\t_____|_____|_____
\t     |     |     
\t  7  |  8  |  9  
\t     |     |     """

def grid_display():
    system('cls')
    print(tictactoe_grid)

#class for the two players to store information in

class Player():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

#class for the seperate gridfields to make analysing the win condition easier

class Field():
    def __init__(self, pos, index):
        self.pos = pos
        self.index = index
        self.value = tictactoe_grid[self.index]

#function for updating the value of each Field

def field_update():
    for i in field_list:
        i.value = tictactoe_grid[i.index]


#function for resetting most of the game variables to their default state

def game_reset():
    global gamestatus
    gamestatus = True
    grid_reset()
    global chosen_numbers
    chosen_numbers = []
    global active_player
    active_player = Player_1
    global valid_numbers
    valid_numbers = []

#function for displaying the winner screen

def postwin_print(num):
    title_display()
    print(tictactoe_grid)
    print(f'\tPlayer {num} has won!')
    global gamestatus
    gamestatus = False

#main codeblock
quitstatus = True
Player_1 = Player('Player 1', 'X')
Player_2 = Player('Player 2', 'O')


#main menu
title_display()
while quitstatus:
    game_reset()
    start_question = input("\n\n\n\nType 's' to start a new game and 'q' to Quit: ")
    if start_question == 's':
        Field_1 = Field(1, 23)
        Field_2 = Field(2, 29)
        Field_3 = Field(3, 35)
        Field_4 = Field(4, 80)
        Field_5 = Field(5, 86)
        Field_6 = Field(6, 92)
        Field_7 = Field(7, 137)
        Field_8 = Field(8, 143)
        Field_9 = Field(9, 149)
        field_list = [Field_1, Field_2, Field_3, Field_4, Field_5, Field_6, Field_7,Field_8, Field_9]
        grid_width = int(math.sqrt(len(field_list)))
        for i in range(1, (len(field_list)+1)):
            valid_numbers.append(str(i))
        grid_display()
# menu once in game 
        while gamestatus:
#win conditions
            horizontal_counter = 0
            for index, field  in enumerate(field_list):
                while (index + 1) > horizontal_counter:
                    horizontal_counter += grid_width
                if field.value == 'X':
                    if horizontal_counter - (index + 1) >= 2 and field_list[index + 1].value == 'X' and field_list[index + 2].value == 'X':
                        postwin_print(1)
                    elif (index + 1) <= (len(field_list)) - (2*grid_width) and field_list[index + grid_width + grid_width].value == 'X' and field_list[index + grid_width].value == 'X':
                        postwin_print(1)
                    elif grid_width - (index + 1) >= 2 and field_list[index + (grid_width + 1)].value == 'X' and field_list[(index + (grid_width + 1)) + (grid_width + 1)].value == 'X':
                        postwin_print(1)
                elif field.value == 'O':
                    if horizontal_counter - (index + 1) >= 2 and field_list[index + 1].value == 'O' and field_list[index + 2].value == 'O':
                        postwin_print(2)
                    elif (index + 1) <= (len(field_list)) - (2*grid_width) and field_list[index + grid_width + grid_width].value == 'O' and field_list[index + grid_width].value == 'O':
                        postwin_print(2)
                    elif grid_width - (index + 1) >= 2 and field_list[index + (grid_width + 1)].value == 'O' and field_list[(index + (grid_width + 1)) + (grid_width + 1)].value == 'O':
                        postwin_print(2)

#draw condition
            draw_counter = 0
            for i in field_list:
                if i.value not in valid_numbers:
                    draw_counter += 1
                elif draw_counter == len(field_list):
                    title_display()
                    print(tictactoe_grid)
                    print('\n\tIt`s a draw!')
                    gamestatus = False

#player input checker 
            if gamestatus:
                    chosen_num_index = ''
                    number_input = input(f"\n\n{active_player.name}, input the number of the field you want to mark or type 'q' to Quit: ")
                    if number_input in chosen_numbers:
                        grid_display()
                        print('\n\nPlease enter a number that has not been taken already')

                    elif number_input in valid_numbers:
                        chosen_num_index = tictactoe_grid.find(number_input)
                        tictactoe_grid = tictactoe_grid[:chosen_num_index] + active_player.symbol + tictactoe_grid[chosen_num_index+1:]
                        chosen_numbers.append(number_input)
                        field_update()
                        if active_player == Player_1:
                            active_player = Player_2

                        elif active_player == Player_2:
                            active_player = Player_1
                            
                        grid_display()
            
                    elif number_input == 'q':
                        gamestatus = False
                        title_display()

                    else:
                        grid_display()
                        print('\n\nPlease enter a valid input')

    elif start_question == 'q':
        quitstatus = False

    else:
        title_display()
        print('\n\nPlease enter a valid input')
        
