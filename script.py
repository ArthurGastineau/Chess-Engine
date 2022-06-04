import chess
import random

class ChessPlayer:
    #define constructor
    def __init__(self, name, color):
        self.name = name
        if color == 'white':
            self.color = chess.WHITE
        else:
            self.color = chess.BLACK

class ChessGame:
    #define constructor
    def __init__(self, white_player, black_player):
        self.board = chess.Board()
        self.white_player = white_player
        self.black_player = black_player
        self.move_number = 0
        self.winner = None
    #define method to print board
    def print_board(self):
        print(self.board)
    #define method to get valid moves
    def get_valid_moves(self, player):
        return self.board.legal_moves
    #define method to make a move
    def make_move(self, move):
        #if the move is valid, make the move
        if move in self.get_valid_moves(self.board.turn):
            self.board.push(move)
            self.move_number += 1
            #if the move is a checkmate, set the winner
            if self.board.is_checkmate():
                if self.board.turn == chess.WHITE:
                    self.winner = self.black_player
                else:
                    self.winner = self.white_player
            #if the move result into a draw print the type of draw
            else:
                if self.board.is_insufficient_material():
                    print('insufficient material')
                    self.winner = "Draw"
                elif self.board.is_stalemate():
                    print('stalemate')
                    self.winner = "Draw"
                elif self.board.is_seventyfive_moves():
                    print('seventyfive moves')
                    self.winner = "Draw"
                elif self.board.is_fivefold_repetition():
                    print('fivefold repetition')
                    self.winner = "Draw"
        else:
            print('Invalid move')
            
#create a chess game where the move are done randomly from the valid moves
def main():
    #create a player
    player1 = ChessPlayer('player1', 'white')
    player2 = ChessPlayer('player2', 'black')
    #create a game
    game = ChessGame(player1, player2)
    #print the board
    game.print_board()
    #while the game is not over, make a random move
    while game.winner == None:
        move = random.choice(list(game.get_valid_moves(game.board.turn)))
        game.make_move(move)
        game.print_board()
    #print the result and number moves
    print(game.board.result() + ' in ' + str(game.move_number//2) + ' moves')

if __name__ == "__main__":
    main()
            
        
                


