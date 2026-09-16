import Intro_to_OOP as oop

leo = oop.Animal("Leo", "Dog", 7)
print(leo.get_name(), "vaccinated:", leo.is_vaccinated())
leo.vaccinate()
print(leo.get_name(), "vaccinated:", leo.is_vaccinated())
