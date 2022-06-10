class Animal:
    name = ''
    category = ''
    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category
    
class Turtle(Animal):
    category = 'reptile'
    
class Snake(Animal):
    category = 'reptile'
  
class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return (f'There are {result} {category}s in our zoo!')
 
zoo = Zoo()
jonny = Turtle('Jonny')
lanny = Snake('Lanny')
zoo.add_animal(jonny)
zoo.add_animal(lanny)
print(zoo.total_of_category('reptile'))