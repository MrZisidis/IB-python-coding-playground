class Animal():
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

bella = Animal("Bella", "Cat", 5)
mitsos = Animal("Mitsos", "Dog", 10)
print(type(bella))

# bella.vaccinate()
print(bella.get_name(), "vaccinated:", bella.is_vaccinated())
# Python prints the boolean as "True" (capital T); Java prints "true"
mitsos.vaccinate()
print(mitsos.get_name(), "vaccinated:", mitsos.is_vaccinated())