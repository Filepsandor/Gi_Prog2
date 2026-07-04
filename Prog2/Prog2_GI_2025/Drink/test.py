import sys

def main():
    if(len(sys.argv) != 1 and type(sys.argv[1]) != int):
        raise Exception("Invalid argument")
    no_of_drinks = sys.argv[1]

    for i in range(int(no_of_drinks)):
        inpt = input()
        inpt_list = inpt.split(";")
        if(len(inpt_list) == 3):
            #sima Drink
            pass
        else:
            #Spirit szeszes ital
            pass

    with open("testfile.txt","r") as f:
        lines = f.readline()


if __name__ == '__main__':
    main()