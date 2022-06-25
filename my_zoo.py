# make class Animal which has name and category
class Animal:
    name = ''
    category = ''
    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category
        
# make class Turtle which belongs to reptile   
class Turtle(Animal):
    category = 'reptile'
    
# make class Snake which belongs to reptile    
class Snake(Animal):
    category = 'reptile'

# make class Zoo, where we can add animals and return count current animals in the zoo
class Zoo:
    # init count current animals
    def __init__(self):
        self.current_animals = {}
        
    # function where we add animals in the zoo
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    # function where count total of category animal
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return (f'There are {result} {category}s in our zoo!')
    
# testing Zoo 
zoo = Zoo()
jonny = Turtle('Jonny')
lanny = Snake('Lanny')
zoo.add_animal(jonny)
zoo.add_animal(lanny)
print(zoo.total_of_category('reptile'))