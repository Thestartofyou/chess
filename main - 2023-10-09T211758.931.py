import chess
import chess.engine

def get_best_move(fen_position):
    with chess.engine.SimpleEngine.popen_uci("path/to/stockfish") as engine:
        board = chess.Board(fen_position)
        result = engine.play(board, chess.engine.Limit(time=1.0))
        return result.move.uci()

if __name__ == "__main__":
    fen_position = input("Enter the FEN position: ")
    best_move = get_best_move(fen_position)
    print(f"The best move is: {best_move}")
