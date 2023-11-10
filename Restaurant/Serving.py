class Serving:

    def __init__(self):
        self.foods = []
        print("Serving: Creating Serving Object")
    
    def add(self, items):
        self.foods += items
        print("Serving: Adding menu items to be served")