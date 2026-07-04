class Drink:

    name: str
    _size: str
    __price: int

    def __init__(self, name, price, size = "5 dl"):
        self.name = name
        self._size = size
        self.__price = price

    @property
    def size(self):
        return self._size

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __repr__(self):
        return "{0}, {1}, {2}"\
            .format(self.name, self._size, self.__price)

    def __str__(self):
        return "{0}, {1}, {2} Ft"\
            .format(self.name, self._size, self.__price)

    def __eq__(self, other):
        return self.__price == other.__price \
        and self._size == other.size \
        and self.name == other.name

    def __lt__(self, other):
        return self.__price < other.price \
            or self._size > other.size \
            and self.name > other.name

    @staticmethod
    def task_8(drinks: list["Drink"], name: str):
        for drink in drinks:
            if drink.name == name:
                return drink.size

        return "Nincs ilyen"

    @staticmethod
    def task_9(drinks: list["Drink"]):
        uniqueList = []
        for drink in drinks:
            if drink.size not in uniqueList:
                uniqueList.append(drink.size)

        return uniqueList

    @staticmethod
    def task_13(drinks: list["Drink"]):
        dictionary = dict()
        for drink in drinks:
            if drink.size in dictionary.keys():
                dictionary[drink.size] += 1
            else :
                dictionary[drink.size] = 1

        return dictionary

