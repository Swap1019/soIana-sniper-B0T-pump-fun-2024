from oop import (
    Board,
    Player,
)

game = Board()
game.print_board()

player1 = Player(letter = 'x')
player2 = Player(letter = 'o')

while True:

    player1.get_data()
    player1.update_board(player=player1,game=game)
    game.print_board()

    if game.win_check():
        print(*'player has won')
        break

    player2.get_data()
    player2.update_board(player=player2,game=game)
    game.print_board()

    if game.win_check():
        print(*'player has won')
        break
