from Cook import Cook
from MenuItem import MenuItem
from Serving import Serving as Plates

def main():
    cooking = Cook()
    plates = Plates()

    total_needed = 5

    while total_needed > 0:
        print("main: inside while loop")
        menu_item = MenuItem("fries")
        # returns a list of menu objects
        cooked = cooking.make(menu_item) 
        plates.add(cooked)
        total_needed -= 1
        
if __name__ == "__main__":
    main()