import random


def display_board(current_positions):
    board = '''
    {top left} | {top center} | {top right}
    ----------
    {center left} | {center} | {center right}
    ----------
    {bottom left} | {bottom center} | {bottom right}
    '''.format(**current_positions)
    print board

def is_movable(current_positions):
    user_prompt="Please choose"
    possible_moves =[]
    for positions in current_positions:
        if(current_positions[positions]==" "):
            possible_moves.append(positions)
            user_prompt += "\n" + positions
    user_prompt +="\n"
    return possible_moves,user_prompt

def user_move(current_positions,current_player):
    possible_moves,user_prompt =is_movable(current_positions)
    user_choice = raw_input(user_prompt).lower()
    while(user_choice not in possible_moves):
        user_choice = raw_input("wrong input\n").lower()
    current_positions[user_choice] = current_player
    return current_positions

def AI_move(current_positions,computer_player):
    possible_moves,user_prompt =is_movable(current_positions)
    AI_choice = random.choice(possible_moves)
    print "AI chosed "+AI_choice
    current_positions[AI_choice] = computer_player
    return current_positions

def is_game_over(current_positions,current_player):
    #Assuming only one winner
    winners = [["top left", "top center", "top right"],
               ["center left", "center", "center right"],
               ["bottom left", "bottom center", "bottom right"],
               ["top left", "center left", "bottom left"],
               ["top center", "center", "bottom center"],
               ["top right", "center right", "bottom right"],
               ["top left", "center", "bottom right"],
               ["top right", "center", "bottom left"]]
    #Going through all of the winning combinations
    for winning_combo in winners:
        possible_winner = current_positions[winning_combo[0]]
        if possible_winner != " ":
            possbile_won = True
            for value in winning_combo:
                if(current_positions[value] != possible_winner):
                    possbile_won = False
                    break
            if possbile_won:
                if possible_winner == current_player:
                    return "You wins"
                else:
                    return "AI wins!"

    is_draw = True
    for position in current_positions:
        if current_positions[position] == " ":
            is_draw = False
            return False
    if is_draw:
        return "Draw!"

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = raw_input('Do you want to be X or O?').upper()
        if letter == 'X':
            return 'X','O'
        else:
            return 'O','X'

def who_goes_first():
    if random.randint(0,1):
        return 'computer'
    else:
        return 'player'



def play_game():
    current_positions ={"top left":" ","top center":" ","top right":" ",
                        "center left":" ","center":" ","center right":" ",
                        "bottom left":" ","bottom center":" ","bottom right":" "}
    current_player,computer_player = inputPlayerLetter()
    turn = who_goes_first()
    print 'the '+turn+' will go first'
    result = False
    while not result:
        display_board(current_positions)
        if(turn == 'player'):
            user_move(current_positions,current_player)
            turn = "computer";
        else:
            AI_move(current_positions,computer_player)
            turn = "player";
        result = is_game_over(current_positions,current_player)
    if(result):
        display_board(current_positions)
        print "Gamve Over!"
        print "Result: ",result


play_game()
