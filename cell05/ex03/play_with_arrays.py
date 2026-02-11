def main():
	original = [2, 8, 9, 48, 8, 22, -12, 2]
	unique = {v + 2 for v in original if v > 5}

	print(original)
	print(unique)

main()

