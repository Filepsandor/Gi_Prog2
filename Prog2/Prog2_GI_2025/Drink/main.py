from drink import Drink


def main():
    cola = Drink('cola', 100)
    fanta = Drink('fanta', 100, "1 liter")
    mirinda = Drink(price = 100, name = 'mirinda')

    print(cola)
    print(fanta)
    print(mirinda)

    drinks = [cola, fanta, mirinda]

    print(Drink.task_8(drinks, "fanta"))
    print("*"*10)
    print(Drink.task_8(drinks, "hell"))

    print(Drink.task_9(drinks))

    print(Drink.task_13(drinks))


if __name__ == '__main__':
    main()