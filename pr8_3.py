class KgToPounds:
    def __init__(self, kg):
        self.kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError("Килограммы задаются только числами")

    def to_pounds(self):
        return self.__kg * 2.205


kg1 = KgToPounds(10)
print(kg1.kg)
print(kg1.to_pounds())

kg1.kg = 20
print(kg1.kg)
print(kg1.to_pounds())