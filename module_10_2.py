import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days_of_the_war = 0
        while enemies:
            days_of_the_war += 1
            enemies = enemies - self.power
            time.sleep(1)
            print(f"{self.name} сражается {days_of_the_war}..., осталось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {days_of_the_war}")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()