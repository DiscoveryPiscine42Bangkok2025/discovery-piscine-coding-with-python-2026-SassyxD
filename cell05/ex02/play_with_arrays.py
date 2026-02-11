def main():
	original = [2, 8, 9, 48, 8, 22, -12, 2]
	new = []
	for v in original:
		if v > 5:
			new.append(v + 2)

	print(f"Original array: {original}")
	print(f"New array: {new}")

main()

