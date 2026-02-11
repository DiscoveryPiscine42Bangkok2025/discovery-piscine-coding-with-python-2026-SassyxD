def checkmate(board):
	# --- validation ---
	if not isinstance(board, str) or not board:
		return "Error"

	rows = [row.strip() for row in board.split('\n')]
	n = len(rows)
	if n == 0:
		return "Error"

	for row in rows:
		if len(row) != n:
			return "Error: The board is not a square."

	# --- find king ---
	pieces = set("KPBRQ")
	king_pos = None
	king_count = 0

	for r in range(n):
		for c in range(n):
			if rows[r][c] == 'K':
				king_count += 1
				king_pos = (r, c)

	if king_count == 0:
		return "Error: No King on the board."
	if king_count > 1:
		return "Error: More than one King on the board."

	kr, kc = king_pos

	# --- pawn check (pawn attacks diagonally upward) ---
	for dc in [-1, 1]:
		pr, pc = kr + 1, kc + dc
		if 0 <= pr < n and 0 <= pc < n and rows[pr][pc] == 'P':
			return "Success"

	# --- rook / queen check (straight lines) ---
	for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		r, c = kr + dr, kc + dc
		while 0 <= r < n and 0 <= c < n:
			ch = rows[r][c]
			if ch in pieces:
				if ch in ('R', 'Q'):
					return "Success"
				break
			r += dr
			c += dc

	# --- bishop / queen check (diagonals) ---
	for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
		r, c = kr + dr, kc + dc
		while 0 <= r < n and 0 <= c < n:
			ch = rows[r][c]
			if ch in pieces:
				if ch in ('B', 'Q'):
					return "Success"
				break
			r += dr
			c += dc

	return "Fail"
