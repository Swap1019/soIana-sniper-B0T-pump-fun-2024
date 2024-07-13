from oop import (
    Board,
    Player,
)

def player1_func(player1,game):
    player1.get_data(game=game)
    player1.update_board(player=player1,game=game)
    game.print_board()

    if game.win_check():
        print(*'player1 has won')
        return True
    return False

def player2_func(player2,game):
    player2.get_data(game=game)
    player2.update_board(player=player2,game=game)
    game.print_board()

    if game.win_check():
        print(*'player2 has won')
        return True
    return False

def main():
    while True:
        if player1_func(game=game,player1=player1):
            break
        if player2_func(game=game,player2=player2):
            break

if __name__ == '__main__':

    game = Board()
    game.print_board()
    player1 = Player(letter = 'x')
    player2 = Player(letter = 'o')
    main()