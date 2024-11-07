class Nikola:
    def __init__(self, name, age):
        if name == "Николай":
            self._name = "Николай"
        else:
            self._name = f"Я не {name}, а Николай"
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    def __setattr__(self, key, value):
        if key not in self.__dict__ and key not in ['_name', '_age']:
            raise AttributeError(f"Нельзя добавлять атрибуты, кроме 'name' и 'age'")
        super().__setattr__(key, value)
    
person1 = Nikola("Максим", 30)
print(person1.name)
print(person1.age)

person2 = Nikola("Николай", 25)
print(person2.name)
print(person2.age)

    