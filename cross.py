from os import system
import re

system("cls")


# Passed
class Greet:
    def hello():
        print("Это игра крестики-нолики!")
        print("Игроку будет предложено выбрать клетку в формате \"x y\", где x - это ось Абсцис, а y - ось Ординат.")
        print("Игра начинается!", end="\n\n")


# Passed
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


class ShowField:
    def show_main():
        for x in Field.main:
            for y in x:
                print(y, end=" ")
            print()
        print()


class Choice:
    def choice_for_player_one():
        flag = True
        while flag:
            s = input("Игрок №1, выберите клетку: ")
            if re.fullmatch("[1-3]\s[1-3]", s) is not None:
                x, y = map(int, s.split())
                if Field.main[y][x] == "_":
                    flag = False
                else:
                    print("Эта клетка уже занята! Попробуйте еще раз.", end="\n\n")
                    ShowField.show_main()
            else:
                print("Вы выбрали неправильную клетку!", end="\n\n")
                ShowField.show_main()
        print()

        return x, y

    def choice_for_player_two():
        flag = True
        while flag:
            s = input("Игрок №2, выберите клетку: ")
            if re.fullmatch("[1-3]\s[1-3]", s) is not None:
                x, y = map(int, s.split())
                if Field.main[y][x] == "_":
                    flag = False
                else:
                    print("Эта клетка уже занята! Попробуйте еще раз.", end="\n\n")
                    ShowField.show_main()
            else:
                print("Вы выбрали неправильную клетку!", end="\n\n")
                ShowField.show_main()
        print()

        return x, y


class UpdateField:
    def update_for_player_one(x, y):
        Field.main[y][x] = "X"
        Field.finish[y - 1][x - 1] = 1

    def update_for_player_two(x, y):
        Field.main[y][x] = "O"
        Field.finish[y - 1][x - 1] = 0

    def clear_field_main():
        Field.main = [

            [" ", 1, 2, 3],
            [1, "_", "_", "_"],
            [2, "_", "_", "_"],
            [3, "_", "_", "_"]

        ]

    def clear_field_finish():
        Field.finish = [

        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]

    ]


class EndGame:
    step = 0
    def condition():
        first_column_count = 0
        second_column_count = 0
        third_column_count = 0

        left_diagonal_count = 0
        right_diagonal_count = 0

        left_diagonal_index = 0
        right_diagonal_index = 2

        for x in Field.finish:
            if sum(x) == 3:
                EndGame.winner = True
                return False
            elif not sum(x):
                EndGame.winner = False
                return False

            first_column_count += x[0]
            second_column_count += x[1]
            third_column_count += x[2]

            left_diagonal_count += x[left_diagonal_index]
            right_diagonal_count += x[right_diagonal_index]

            left_diagonal_index += 1
            right_diagonal_index -= 1

        # win for first player
        if first_column_count == 3 or second_column_count == 3 or third_column_count == 3 or left_diagonal_count == 3 or right_diagonal_count == 3:
            EndGame.winner = True
            return False

        # win for second player
        if first_column_count == 0 or second_column_count == 0 or third_column_count == 0 or left_diagonal_count == 0 or right_diagonal_count == 0:
            EndGame.winner = False
            return False

        EndGame.step += 1
        a = EndGame.step // 9
        if EndGame.step // 9 > a:
            first_column_count = 0
            second_column_count = 0
            third_column_count = 0

            left_diagonal_count = 0
            right_diagonal_count = 0

            left_diagonal_index = 0
            right_diagonal_index = 2

        return True


class Loop:
    def another_one():
        if EndGame.step:
            answer = "y"
            while answer.lower() != "y" or answer.lower() != "n":
                answer = input("Сыграем еще раз? (y/n): ")
                if answer.lower() == "y":
                    system("cls")
                    return True
                elif answer.lower() == "n":
                    print("До свидания!", end="\n\n")
                    return False
                else:
                    print("Что Вы вводите?! Сказали же (y/n)!", end="\n\n")
        else:
            return True


class Main:
    Greet.hello()
    while Loop.another_one():

        UpdateField.clear_field_main()
        UpdateField.clear_field_finish()
        move = 0

        while EndGame.condition():

            ShowField.show_main()
            x, y = Choice.choice_for_player_one()
            UpdateField.update_for_player_one(x, y)

            if not EndGame.condition():
                break

            move += 1
            if move >= 9:
                break

            ShowField.show_main()
            x, y = Choice.choice_for_player_two()
            UpdateField.update_for_player_two(x, y)

            move += 1

        ShowField.show_main()
        print("Игра окончена!")

        if move != 9:
            if EndGame.winner == True:
                print("Победил игрок №1", end="\n\n")
            elif EndGame.winner == False:
                print("Победил игрок №2", end="\n\n")
        else:
            print("Ничья!", end="\n\n")
