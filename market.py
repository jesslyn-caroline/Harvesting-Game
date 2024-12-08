class UpcomingItem:
    def __init__(self):
        self.items = [
            {'name': 'Corn',
             'icon': '🌽',
             'grow_time': 3,
             'quantity': 0,
             'price': 30,
             'unlocked_at_day': 1},

            {'name': 'Potato',
             'icon': '🥔',
             'grow_time': 4,
             'quantity': 0,
             'price': 50,
             'unlocked_at_day': 1},

            {'name': 'Tomato',
             'icon': '🍅',
             'grow_time': 4,
             'quantity': 0,
             'price': 60,
             'unlocked_at_day': 3},

            {'name': 'Carrot',
             'icon': '🥕',
             'grow_time': 4,
             'quantity': 0,
             'price': 50,
             'unlocked_at_day': 3}
        ]
    
    def check_unlocked_items(self, day):
        unlocked_items = []
        for i in self.items:
            if i['unlocked_at_day'] == day:
                unlocked_items.append(i)
        
        return unlocked_items


class Buy:
    def __init__(self):
        self.items = []
    
    def update_item(self, items):
        for i in items:
            print(i)
            self.items.append(i)
    
    def check_items(self):
        print('-' * 80)
        print(f'{'Market Items':^80}')
        print('-' * 80)
        for i in self.items:
            print(f'{i["icon"]} {i["name"]} - Price: {i["price"]}')
        print('-' * 80)
 
class Sell: 
    def __init__(self):
        self.corn_price = 0
        self.potato_price = 0
        self.tomato_price = 0
        self.carrot_price = 0
    
    def update_price(self, corn_price, potato_price, tomato_price, carrot_price):
        self.corn_price = corn_price
        self.potato_price = potato_price
        self.tomato_price = tomato_price
        self.carrot_price = carrot_price
    
    def check_price(self):
        print('-' * 80)
        print(f'{'💰Selling Price💰':^80}')
        print('-' * 80)
        print(f'🌽 Corn: {self.corn_price}')
        print(f'🥔 Potato: {self.potato_price}')
        print(f'🍅 Tomato: {self.tomato_price}')
        print(f'🥕 Carrot: {self.carrot_price}')
        print('-' * 80)


class Market:
    def __init__(self):
        self.buy = Buy()
        self.sell = Sell()