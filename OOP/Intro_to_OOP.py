class Animal():
    total_animal_counter = 0
    def __init__(self, name, species, age):
        self._name = name          # the leading underscore marks the attribute as private (IB convention)
        self._species = species
        self._age = age
        self._vaccinated = False

    def vaccinate(self):
        self._vaccinated = True

    def is_vaccinated(self):
        return self._vaccinated

    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age

    def set_age(self):
        self._age = self._age + 1

    def set_age(self, new_age):
        self._age = new_age

    def set_name(self, new_name):
        self._name = new_name

animal1 = Animal("Flox", 1, 2)
animal2 = Animal("Bella", "Cat", 5)
animal3 = Animal("Mitsos", "Dog", 10)
# print(type(animal1))

animal3.set_age(12)
print(animal3.get_age())
animal3.set_age(23)
print(animal3.get_age())


print(animal2.get_name(), " is renamed to....")
animal2.set_name("Maria")
print(animal2.get_name())

# print(animal2.get_species())
# print(animal2.get_age())
#
# animal2.set_age() #Bella has brirthday
# print("Bella has birthday")
# print(animal2.get_age())





# bella.vaccinate()
# print(animal2.get_name(), "vaccinated:", bella.is_vaccinated())
# # Python prints the boolean as "True" (capital T); Java prints "true"
# mitsos.vaccinate()
# print(mitsos.get_name(), "vaccinated:", mitsos.is_vaccinated())