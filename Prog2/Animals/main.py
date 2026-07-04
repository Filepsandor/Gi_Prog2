from Fox import Fox
from frog import Frog
from color import Color
from Habitat import Habitat

def main():
    vulpes = Fox(Habitat.GROUND, 10, 200)
    print(vulpes)
    
    rana = Frog([Habitat.GROUND, Habitat.FRESHWATER])
    
    print(rana.habitat)
    
    # print(Color.BLUE.value)
    # print(Color.RED.value)
    # print(Color.GREEN.value)
    

if __name__ == '__main__':
    main()