from os import system

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
    Field_1.value = tictactoe_grid[Field_1.index]
    Field_2.value = tictactoe_grid[Field_2.index]
    Field_3.value = tictactoe_grid[Field_3.index]
    Field_4.value = tictactoe_grid[Field_4.index]
    Field_5.value = tictactoe_grid[Field_5.index]
    Field_6.value = tictactoe_grid[Field_6.index]
    Field_7.value = tictactoe_grid[Field_7.index]
    Field_8.value = tictactoe_grid[Field_8.index]
    Field_9.value = tictactoe_grid[Field_9.index]

#function for resetting most of the game variables to their default state

def game_reset():
    global gamestatus
    gamestatus = True
    grid_reset()
    global chosen_numbers
    chosen_numbers = []
    global active_player
    active_player = Player_1
    field_update

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
valid_numbers = ['1','2', '3', '4', '5', '6', '7', '8', '9']

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
        grid_display()
#menu once in game
        while gamestatus:
#win conditions
            if Field_1.value == 'X' and Field_2.value == 'X' and Field_3.value == 'X':
                postwin_print(1)

            elif Field_1.value == 'X' and Field_4.value == 'X' and Field_7.value == 'X':
                postwin_print(1)

            elif Field_1.value == 'X' and Field_5.value == 'X' and Field_9.value == 'X':
                postwin_print(1)

            elif Field_2.value == 'X' and Field_5.value == 'X' and Field_8.value == 'X':
                postwin_print(1)

            elif Field_1.value == 'X' and Field_5.value == 'X' and Field_9.value == 'X':
                postwin_print(1)

            elif Field_3.value == 'X' and Field_5.value == 'X' and Field_7.value == 'X':
                postwin_print(1)

            elif Field_3.value == 'X' and Field_6.value == 'X' and Field_9.value == 'X':
                postwin_print(1)

            elif Field_4.value == 'X' and Field_5.value == 'X' and Field_6.value == 'X':
                postwin_print(1)
            
            elif Field_1.value == 'O' and Field_2.value == 'O' and Field_3.value == 'O':
                postwin_print(2)
                    
            elif Field_1.value == 'O' and Field_4.value == 'O' and Field_7.value == 'O':
                postwin_print(2)

            elif Field_1.value == 'O' and Field_5.value == 'O' and Field_9.value == 'O':
                postwin_print(2)

            elif Field_2.value == 'O' and Field_5.value == 'O' and Field_8.value == 'O':
                postwin_print(2)

            elif Field_1.value == 'O' and Field_5.value == 'O' and Field_9.value == 'O':
                postwin_print(2)

            elif Field_3.value == 'O' and Field_5.value == 'O' and Field_7.value == 'O':
                postwin_print(2)

            elif Field_3.value == 'O' and Field_6.value == 'O' and Field_9.value == 'O':
                postwin_print(2)

            elif Field_4.value == 'O' and Field_5.value == 'O' and Field_6.value == 'O':
                postwin_print(2)
#draw condition
            elif str(Field_1.pos) != Field_1.value and str(Field_2.pos) != Field_2.value and str(Field_3.pos) != Field_3.value and str(Field_4.pos) != Field_4.value and str(Field_5.pos) != Field_5.value and str(Field_6.pos) != Field_6.value and str(Field_7.pos) != Field_7.value and str(Field_8.pos) != Field_8.value and str(Field_9.pos) != Field_9.value:
                title_display()
                print(tictactoe_grid)
                print('\n\tIt`s a draw!')
                gamestatus = False
                
#player input checker
            else:
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
        
