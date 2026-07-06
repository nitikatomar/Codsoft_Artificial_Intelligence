import math
import time

# Board setup: 1 se 9 tak ke spots ke liye ek list
board = [' ' for _ in range(9)]
AI = 'O'
HUMAN = 'X'


# 1. Board ko screen par acche se print karne ke liye function
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


# 2. Check karna ki koi jeeta ya nahi
def check_winner(b, player):
    # Jeetne ke saare combinations (Rows, Columns, Diagonals)
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for condition in win_conditions:
        if b[condition[0]] == b[condition[1]] == b[condition[2]] == player:
            return True
    return False


# 3. Check karna ki board full ho gaya ya nahi (Tie check)
def is_board_full(b):
    return ' ' not in b


# 4. THE MINIMAX ALGORITHM (AI ka dimaag)
def minimax(b, depth, is_maximizing):
    # Base cases: Score decide karna
    if check_winner(b, AI):
        return 10 - depth  # AI jeeta toh + positive score
    if check_winner(b, HUMAN):
        return depth - 10  # Human jeeta toh - negative score
    if is_board_full(b):
        return 0  # Tie hua toh 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = AI  # Move try karo
                score = minimax(b, depth + 1, False)
                b[i] = ' '  # Move undo karo
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = HUMAN  # Move try karo
                score = minimax(b, depth + 1, True)
                b[i] = ' '  # Move undo karo
                best_score = min(score, best_score)
        return best_score


# 5. AI ki best move find karne ka function
def get_ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


# --- MAIN GAME LOOP ---
print("🎮 Welcome to Unbeatable Tic-Tac-Toe AI! 🎮")
print("Positions are marked from 1 to 9 like this:")
print(" 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 ")
print("You are 'X' and AI is 'O'. Good Luck (You'll need it)!")

# Game tab tak chalega jab tak koi jeet na jaye ya tie na ho
while True:
    # --- HUMAN TURN ---
    print_board()
    try:
        move = int(input("Enter your move (1-9): ")) - 1
        if move < 0 or move > 8 or board[move] != ' ':
            print("❌ Invalid Move! Khali jagah dekh kar 1-9 ke beech chuno.")
            continue
    except ValueError:
        print("❌ Please enter a number between 1 and 9.")
        continue

    # Human ki move apply karo
    board[move] = HUMAN

    # Check if Human won (Practically impossible against this AI, but code rules are rules!)
    if check_winner(board, HUMAN):
        print_board()
        print("🎉 Wait... What?! You actually beat the AI! Impossible! 🏆")
        break

    if is_board_full(board):
        print_board()
        print("🤝 It's a TIE! You played brilliantly to hold off the AI.")
        break

    # --- AI TURN ---
    print("\n🤖 AI is analyzing all future possibilities...")
    time.sleep(1)  # Human touch: AI thoda break le raha hai sochne ke liye

    ai_move = get_ai_move()
    board[ai_move] = AI
    print(f"🤖 AI chose position {ai_move + 1}")

    # Check if AI won
    if check_winner(board, AI):
        print_board()
        print("💀 AI Wins! Don't worry, it's literally unbeatable. Better luck next time!")
        break

    if is_board_full(board):
        print_board()
        print("🤝 It's a TIE! Outstanding defense against the machine.")
        break