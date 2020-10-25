import random
bag = [i for i in range(1, 91)]


def gen_num(my_list):
    x = random.choice(my_list)
    my_list.remove(x)
    yield x


def check_win(card):
    n = 0
    for el in card:
        for i in el:
            if i == '-':
                n += 1
    return n


class LotoCard:
    def __init__(self):
        self.mtrx = [[' ' for i in range(9)] for el in range(3)]
        numbers = [i for i in range(1, 91)]
        for el in self.mtrx:
            indexes = [z for z in range(9)]
            for i in range(5):
                el[next(gen_num(indexes))] = str(next(gen_num(numbers)))

    def __str__(self):
        return '\n'.join(' '.join(el) for el in self.mtrx)


class LotoGame:
    def __init__(self, human, computer):
        self.human = human
        self.computer = computer

    def start(self):
        count = 0
        while count <= 90:
            if check_win(self.human.mtrx) == 15:
                print('Вы выиграли!')
                break
            if check_win(self.computer.mtrx) == 15:
                print('Компьютер выиграл')
                break
            my_num = next(gen_num(bag))
            count += 1
            print(f'{my_num} (Осталось {90 - count} бочонков)')
            print('-----Ваша карточка-----')
            print(hum)
            print('--Карточка компьютера--')
            print(comp)
            ans = input('Выберете y/n: ')

            if ans == 'y':
                n = 0
                for el in self.human.mtrx:
                    if str(my_num) in el:
                        el[el.index(str(my_num))] = '-'
                        n = 1
                if n == 0:
                    print('Вы проиграли')
                    break
            else:
                for el in self.human.mtrx:
                    if str(my_num) in el:
                        print('Вы проиграли')
                        break
            for el in self.computer.mtrx:
                if str(my_num) in el:
                    el[el.index(str(my_num))] = '-'
        return 'Конец игры'


hum = LotoCard()
comp = LotoCard()
game = LotoGame(hum, comp)
print(game.start())
