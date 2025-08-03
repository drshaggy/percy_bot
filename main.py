from chesscog.recognition import ChessRecognizer
from chesscog.recognition import ChessRecognizer
from chesscog.recognition import ChessRecognizer
from pydantic import BaseModel
import numpy as np
import cv2
from enum import Enum
from pathlib import Path
import typing
from stockfish import Stockfish

stockfish_path = '/opt/homebrew/bin/stockfish'
stockfish = Stockfish(path=stockfish_path)

classifiers_folder = Path('/Users/connor/Documents/00_projects/01_percy_bot/chesscog/models')
recognizer = ChessRecognizer(classifiers_folder=classifiers_folder)
with open('/Users/connor/Documents/00_projects/01_percy_bot/position1.png', 'rb') as f: 
    file = f.read()

class Turn(str, Enum):
    WHITE = "white"
    BLACK = "black"

class Prediction(BaseModel):
    fen: str
    corners: typing.List[typing.List[int]]

buffer = np.frombuffer(file, np.uint8)
img = cv2.imdecode(buffer, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
turn = Turn.WHITE
board, corners = recognizer.predict(img, turn == Turn.WHITE)
fen = board.board_fen()
print(board)

stockfish.set_fen_position(fen)
best_move = stockfish.get_best_move()

print(fen)
print(best_move)
