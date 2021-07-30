class Greet:
	def hello():
		print("Это игра крестики-нолики!")
		print("Игроку будет предложено выбрать клетку в формате \"x y\", где x - это номер строки, а y - номер столбца.")
		print("Игра начинается!", end="\n\n")

class Field:
	main = [

	[" ", 1, 2, 3],
	[1, "_", "_", "_"],
	[2, "_", "_", "_"],
	[3, "_", "_", "_"]

	]

	finish = [

	[5, 5, 5],
	[5, 5, 5],
	[5, 5, 5]

	]

	def show():
		for x in Field.main:
			for y in x:
				print(y, end=" ")
			print()
		print()

	def end():
		step = 0
		while step < 9:
			a, b = 0, 2
			count, count_2, count_3, count_a, count_b = 0, 0, 0, 0, 0
			for x in Field.finish:
				if sum(x) == 3 or not sum(x):
					return False

				count += x[0]
				count_2 += x[1]
				count_3 += x[2]
				count_a += x[a]
				count_b += x[b]

				a += 1
				b -= 1

			if count == 3 or not count:
				return False
			if count_2 == 3 or not count_2:
				return False
			if count_3 == 3 or not count_3:
				return False
			if count_a == 3 or not count_a:
				return False
			if count_b == 3 or not count_b:
				return False

			step += 1

			return True
		else:
			return False


class Choice:
	count = 1
	def player_choice():
		if Choice.count % 2:
			a, b = map(int, input("Игрок №1, выберите клетку: ").split())
			print()
		else:
			a, b = map(int, input("Игрок №2, выберите клетку: ").split())
			print()
		Choice.count += 1
		return a, b, Choice.count % 2

class Update_field:
	def update(x, y, circle):
		if not circle:
			Field.main[x][y] = "X"
			Field.finish[x - 1][y - 1] = 1
		else:
			Field.main[x][y] = "O"
			Field.finish[x - 1][y - 1] = 0


class Main:
	Greet.hello()
	while Field.end():
		Field.show()
		a, b, c = Choice.player_choice()
		Update_field.update(a, b, c)
	else:
		Field.show()
		print("Игра окончена!")