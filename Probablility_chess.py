#Probability of winning a chess game

#pip install python-chess stockfish


def evaluate_position(board):
    piece_values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 10}
    white_value = 0
    black_value = 0
    for row in board:
        for piece in row:
            if piece.isupper():  # White piece
                white_value += piece_values.get(piece.upper(), 0)
            elif piece.islower():  # Black piece
                black_value += piece_values.get(piece.upper(), 0)
    return white_value - black_value

def calculate_probability(board):
    evaluation = evaluate_position(board)
    total_value = sum([abs(piece_values[piece.upper()]) for row in board for piece in row if piece.upper() in piece_values])
    probability = 0.5 + (evaluation / total_value) * 0.5  # Assuming a linear relationship between evaluation and probability
    return probability

# Example board, you can replace it with the actual board state
board = [
    [' ', 'n', 'k', ' ', ' ', 'q', ' ', ' '],
    [' ', ' ', 'p', 'p', 'p', ' ', ' ', ' '],
    [' ', 'B', ' ', ' ', ' ', ' ', ' ', 'p'],
    [' ', ' ', 'p', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'R'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B'],
    ['P', 'P', 'P', ' ', ' ', 'P', 'P', ' '],
    ['R', 'N', 'B', ' ', 'K', 'B', ' ', 'R']
]

piece_values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 10}

probability = calculate_probability(board)
print("Probability of White Winning:", probability)
print("Probability of Black Winning:", 1 - probability)







#  r n b q k b n r
#  p p p p p . . .
#  . . . . . . . p
#  . . . . . p p .
#  . . . P P . . P
#  . . . . . . . N
#  P P P . . P P .
#  R N B Q K B . R

# 8  r n b q k b n r
# 7  p p p p . . p p
# 6  . . . . . . . .
# 5  . . . P p . . .
# 4  . . . P . . . .
# 3  . . . . . . . .
# 2  P P P . . P P P
# 1  R N B Q K B N R
#    a b c d e f g h