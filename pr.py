 def card_hide(card):
#         return '*' * (len(card) - 4) + card[-4:]
#
#
# card="8754456321113213"
# print(card_hide)


# def reverse(s):
#         return s[::-1]
#
#
# def palindrome(s):
#         rev = reverse(s)
#
#         # проверка на совпадение 2х строк
#         if (s == rev):
#                 return True
#         return False
#
# s ="malayalam"
# ans = palindrome(s)

# class Tomato:
#
#     # Стадии созревания помидора
#     states = {0: 'начальная стадия', 1: 'цветок', 2: 'зеленый_плод', 3: 'бурый_томат'}
#
#     def __init__(self, index):
#         self._index = index
#         self._state = 0
#
#     # Переход к следующей стадии созревания
#     def grow(self):
#         self._change_state()
#
#     # Проверка, созрел ли томат
#     def is_ripe(self):
#         if self._state == 3:
#             return True
#         return False
#
#     # Защищенные(protected) методы
#
#     def _change_state(self):
#          if self._state < 3:
#             self._state += 1
#             self._print_state()
#
#     def _print_state(self):
#         print(f'Tomato {self._index} is {Tomato.states[self._state]}')
#
# class TomatoBush:
#
#     # Создаем список из объектов класса Tomato
#     def __init__(self, num):
#         self.tomatoes = [Tomato(index) for index in range(0, num)]
#
#     # Переводим все томаты из списка на следующий этап созревания
#     def grow_all(self):
#         for tomato in self.tomatoes:
#             tomato.grow()
#
#     # Проверяем, все ли помидоры созрели
#     def all_are_ripe(self):
#         return all([tomato.is_ripe() for tomato in self.tomatoes])
#
#     # Собираем урожай
#     def give_away_all(self):
#         self.tomatoes = []
#
# class Gardener:
#
#     # Выдаем садовнику растение для ухода
#     def __init__(self, name, plant):
#         self.name = name
#         self._plant = plant
#
#     # Ухаживаем за растением
#     def work(self):
#         print('Садовник работает...')
#         self._plant.grow_all()
#         print('Садовник закончил работу')
#
#     # Собираем урожай
#     def harvest(self):
#         print('Садовник собирает урожай...')
#         if self._plant.all_are_ripe():
#             self._plant.give_away_all()
#             print('Сбор урожая завершен')
#         else:
#             print('Слишком рано! Ваше растение зеленое и не созрело.')
#
#  # Статический метод
#     # Выводит справку по садоводству
#     @staticmethod
#     def knowledge_base():
#         print('''Томат в среднем растёт 42 дня, это около шести недель.
#         К концу шестой неделе плод становится тёмно-зелёного цвета.
#          В этот период снимать урожай самое не правильное решение,
#           так как он хоть и вырос, но еще не набрал витаминов,
#           сахаров и других полезных веществ.
#           Когда можно снимать урожай томатов на хранение и дозревание?
#         Стадия созревания бланжевая спелость.
#         Помидоры начинают приобретать более бурый цвет
#         именно в этот период плоды накапливают много сахара, витаминов и полезных микроэлементов.
#          Если у вас есть потребность собрать урожай, то сейчас это делать можно.
#           До конечного созревания пройдет примерно две недели''')
#
#
# # Тесты
# if __name__ == '__main__':
#     Gardener.knowledge_base()
#     great_tomato_bush = TomatoBush(4)
#     gardener = Gardener('Emilio', great_tomato_bush)
#     gardener.work()
#     gardener.work()
#     gardener.harvest()
#     gardener.work()
#     gardener.harvest()

