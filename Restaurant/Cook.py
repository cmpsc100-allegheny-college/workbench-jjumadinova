from MenuItem import MenuItem

class Cook:

    def __init__(self, item_num: int = 4):
        self.item_num = item_num
        print("Cook: Creating a Cook object")

    def cook(self, items: MenuItem = MenuItem()) -> [MenuItem]:
        print("Cook: inside cook method")
        items = []
        while(len(items) < self.item_num):
            item = MenuItem()
            items.append(item)
        return items

    def make(self, items: MenuItem = MenuItem()) -> [MenuItem]:
        return self.cook(items)