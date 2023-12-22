# 写経13章 コンポジション

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner


class Person:
    def __init__(self, name):
        self.name = name


mick = Person(name="Mick jagger")
stan = Dog(name="Stanley", breed="Bulldog", owner=mick)
print(stan.owner.name)
