import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        attack_value = random.randint(1, self.attack_power) #случайна сила аттаки
        other.health -= attack_value
        print(f"{self.name} атакует {other.name} на {attack_value} урона.")

    def is_alive(self):
        return self.health > 0

    def display(self):
        print(f"{self.name} (Здоровье: {self.health})")


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Terminator", health=100, attack_power=20)

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if self.computer.is_alive():
                self.computer_turn()

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

    def player_turn(self):
        input("Нажмите Enter, чтобы атаковать...")
        self.player.attack(self.computer)
        self.computer.display()

    def computer_turn(self):
        print("Ход компьютера...")
        self.computer.attack(self.player)
        self.player.display()

player_name = input("Введите имя героя: ")
game = Game(player_name)
game.start()