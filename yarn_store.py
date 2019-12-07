

## The goal is to have a store the sells yarn, has patterns, and people who buy stuff

class Knitter():
    
    spent = 0
    owns = []
    name = ''
    skill_level = None

    def __init__(self, name, skill_level):
        self.name = name
        self.skill_level = skill_level

    def buy_stuff(self, item, cost):
        self.spent =+cost
        self.owns.append(item)

class Products():
    items_sold = 0
    moolah_made = 0

    def __init__(self, patterns=[], new_color=False):
       
        self.yarn_balls = ['big', 'medium', 'little', 'little', 'little']
        self.yarn_colors = ['blue', 'mauve', 'black', 'pea soup']
        if new_color:
            self.yarn_colors.append(new_color)
        self.patterns = patterns
        self.inventory = {
            'yarn_balls': self.yarn_balls,
            'patterns': self.patterns
        }

    def sold_stuff(self, item, cost):
        self.inventory['new'] = item # pop(item)
        self.items_sold =+ 1
        self.moolah_made =+ cost

    def stock(self):
        return self.items, self.yarn_colors, self.patterns

# next goal is to have the person buy the items and have the stock decrease

def purchase(store, person, thing, cost):

    person.buy_stuff(thing, cost)  # track individual's inventory
    store.sold_stuff(thing, cost)  # track store's inventory
    # print(store.stock) 
