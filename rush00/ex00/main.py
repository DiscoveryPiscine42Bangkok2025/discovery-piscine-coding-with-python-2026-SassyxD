from checkmate import checkmate

def main():
	board1 = """\
R...
.K..
..P.
....\
"""
	board2 = """\
..
.K\
"""
	board3 = """\
.........
.........
.........
.....R...
.....K...
.........
.........
.........
.........\
"""
	board4 = """\
R...
.K......
..P.
....\
"""
	board5 = """\
R...
....
..P.
....\
"""
	board6 = """\
R...
.K..
..P.
..K.\
"""

	# --- Bishop check ---
	board7 = """\
B...
....
..K.
....\
"""
	# --- Queen check (straight) ---
	board8 = """\
.Q..
....
.K..
....\
"""
	# --- Queen check (diagonal) ---
	board9 = """\
Q...
....
..K.
....\
"""
	# --- Piece blocking (Bishop blocked by Pawn) ---
	board10 = """\
B...
.P..
....
...K\
"""
	# --- Invalid input: None ---
	board11 = None
	# --- Invalid input: int ---
	board12 = 42
	# --- 1x1 board with only King ---
	board13 = "K"
	# --- Empty string ---
	board14 = ""

	print("board1  (Pawn check)      :", checkmate(board1))   # Success
	print("board2  (no enemies)      :", checkmate(board2))   # Fail
	print("board3  (Rook check 9x9)  :", checkmate(board3))   # Success
	print("board4  (not square)      :", checkmate(board4))   # Error
	print("board5  (no King)         :", checkmate(board5))   # Error
	print("board6  (2 Kings)         :", checkmate(board6))   # Error
	print("board7  (Bishop check)    :", checkmate(board7))   # Success
	print("board8  (Queen straight)  :", checkmate(board8))   # Success
	print("board9  (Queen diagonal)  :", checkmate(board9))   # Success
	print("board10 (Bishop blocked)  :", checkmate(board10))  # Fail
	print("board11 (None input)      :", checkmate(board11))  # Error
	print("board12 (int input)       :", checkmate(board12))  # Error
	print("board13 (1x1 only King)   :", checkmate(board13))  # Fail
	print("board14 (empty string)    :", checkmate(board14))  # Error

if __name__ == "__main__":
	main()
