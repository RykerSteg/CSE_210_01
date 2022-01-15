"Tic-Tac-Toe"
"By Ryker Steglich"

def main():
  board = threeBythree()
  displayBoard(board)
  game = "play"
  turns(game, board)


def turns (game, board):
  while game != "win" or game != "tie":
    playerOne(board)
    displayBoard(board)
    game = winner(board)
    if game == "win" or game == "tie":
      break
    playerTwo(board)
    displayBoard(board)
    game = winner(board)
    if game == "win" or game == "tie":
      break
  print("Good game. Thanks for playing!")
  
def threeBythree():
  board = [1,2,3,4,5,6,7,8,9]
  return board

def displayBoard(board):
  row = "-+-+-"
  print()
  print(f"{board[0]}|{board[1]}|{board[2]}")
  print(f"{row}")
  print(f"{board[3]}|{board[4]}|{board[5]}")
  print(f"{row}")
  print(f"{board[6]}|{board[7]}|{board[8]}")

def playerOne(board):
  turn = input("x's turn to choose a square (1-9):")
  spot = int(turn) - 1
  while board[spot] == "X" or board[spot] == "O":
    turn = input("This spot has already been filled. Please select another.")
    spot = int(turn) -1
  else:
    board[spot] = ("X")
    return board
  
def playerTwo(board):
  turn = input("o's turnt to choose a sqaure (1-9):")
  spot = int(turn) - 1
  while board[spot] == "X" or board[spot] == "O":
    turn = input("This spot has already been filled. Please select another.")
    spot = int(turn)-1
  else: 
    board[spot] = "O"
  return board

def winner(board):
  tie = [1,2,3,4,5,6,7,8,9]
  if board[0] == board[1] == board[2] or board[0] == board[3] == board[6] or board[0] == board[4] == board[8] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[6] == board[4] == board[2]:
      winner = "win"
      return winner
  elif board[0] != tie[0] and board[1] != tie[1] and board[2] != tie[2] and board[3] != tie[3] and board[4] != tie[4] and board[5] != tie[5] and board[6] != tie[6] and board[7] != tie[7] and board[8] != tie[8]:
    stalemate = "tie"
    return stalemate
main()