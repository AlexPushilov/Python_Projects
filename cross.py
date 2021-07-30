class Greet:
	def hello():
		print("Это игра крестики-нолики!")
		print("Игроку будет предложено выбрать клетку в формате \"x y\", где x - это ось Абсцис, а y - ось Ординат.")
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
	step = 0
	def end():
		while Field.step < 9:

			a, b = 0, 2
			count, count_2, count_3, count_a, count_b = 0, 0, 0, 0, 0

			for x in Field.finish:
				if sum(x) == 3:
					Choice.win = True
					return False
				elif not sum(x):
					Choice.win = False
					return False

				count += x[0]
				count_2 += x[1]
				count_3 += x[2]
				count_a += x[a]
				count_b += x[b]

				a += 1
				b -= 1

			if count == 3 or count_2 == 3 or count_3 == 3 or count_a == 3 or count_b == 3:
				Choice.win = True
				return False
			elif not count or not count_2 or not count_3 or not count_a or not count_b:
				Choice.win = False
				return False

			Field.step += 1

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
			Field.main[y][x] = "X"
			Field.finish[y - 1][x - 1] = 1
		else:
			Field.main[y][x] = "O"
			Field.finish[y - 1][x - 1] = 0


class Main:
	Greet.hello()
	while Field.end():
		Field.show()
		a, b, c = Choice.player_choice()
		Update_field.update(a, b, c)
	else:
		Field.show()
		if Field.step >= 9:
			print("Игра окончена!")
			print("Ничья!")
		elif Choice.win:
			print("Игра окончена!")
			print("Игрок №1 победил!")
		elif not Choice.win:
			print("Игра окончена!")
			print("Игрок №2 победил!")
		else:
			print("Игра оконена!")
