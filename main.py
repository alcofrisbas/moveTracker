import sys, os


class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.order = 0
    def __str__(self):
        return "{:20}\t{}".format(self.name, self.hp)

class Board:
    def __init__(self):
        self.players = {}
    
    def add(self, name, hp):
        if not self.players.get(name, False):
            self.players[name] = Character(name, hp)
        else:
            print("character already exists")
    def del_(self, name):
        del self.players[name]
    def load(self):
        pass

    def show(self):
        for player in sorted(list(self.players.values()), key = lambda k:k.order,reverse=True):
            print(player)
    
    def init_(self, name, order):
        try:
            self.players[name].order = int(order)
        except KeyError:
            print("{} is not a character. Add {}? y/n".format(name, name))
            if input("-- ") == "y":
                hp = int(input("hp(default:10)-- ") or "10")
                self.add(name, hp)
    def mod(self, name, num):
        self.players[name].hp += int(num)

    def play(self):
        ans = input(">. ")
        while ans != ":q":
            words = ans.split()
            if len(words) == 0:
                self.show()
            elif words[0] == "add":
                self.add(words[1], words[2])
            elif words[0] == "show":
                self.show()
            elif words[0] == "init":
                self.init_(words[1], words[2])
            elif words[0] in list(self.players.keys()):
                self.mod(words[0], words[1])
            ans = input(">. ")


def main():
    b = Board()
    b.play()
            

if __name__ == "__main__":
    main()
