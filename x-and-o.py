"Tic-Tac-Toe"
"By Ryker Steglich"

def main():
  board = newBoard()
  displayBoard(board)
  game = 0
  
  while game != 1 or game != 2:
    xturn = input("x's turn to choose a square (1-9):")
    playerOne(xturn, board)
    displayBoard(board)
    game = winner(board)
    if game == 1 or game == 2:
      break
    oturn = input("o's turnt to choose a sqaure (1-9):")
    playerTwo(oturn, board)
    displayBoard(board)
    game = winner(board)
    if game == 1 or game == 2:
      break
  print("Good game. Thanks for playing!")



  
def newBoard():
  board = [1,2,3,4,5,6,7,8,9]
  return board

def displayBoard(board):
  row = "--+-+--"
  print()
  print(f"|{board[0]}|{board[1]}|{board[2]}")
  print(f"{row}")
  print(f"|{board[3]}|{board[4]}|{board[5]}")
  print(f"{row}")
  print(f"|{board[6]}|{board[7]}|{board[8]}")

def playerOne(turn, board):
  spot = int(turn) - 1
  board[spot] = "x"
  return board
  
def playerTwo(turn, board):
  spot = int(turn) - 1
  board[spot] = "o"
  return board

def winner(board):
  if board[0] == board[1] == board[2] or board[0] == board[3] == board[6] or board[0] == board[4] == board[8] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[6] == board[4] == board[2]:
      winner = 1
      return winner
  
main()