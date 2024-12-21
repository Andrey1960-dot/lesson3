from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name:str, power:int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        for i in range(enemies):
            if enemies > 0:
                time.sleep(1)
                day += 1
                enemies -= self.power
                print(f'{self.name} сражается {day}... дней, осталось {enemies} воинов.')
                if enemies == 0:
                    print(f'{self.name} одержал победу спустя {day} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

