from threading import Thread, Lock
import threading
import time
import random

class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            ref = random.randint(50, 500)
            self.balance += ref
            print(f'Пополнение: {ref}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            wit = random.randint(50, 500)
            print(f'Запрос на {wit}')
            if self.balance >= wit:
                self.balance -= wit
                print(f'Снятие: {wit}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()
                time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
