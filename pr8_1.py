class Soda:
    def __init__(self, addition=None):
        self.addition = addition

    def show_my_drink(self):
        if self.addition:
            print(f"Газировка с добавкой {self.addition}")
        else:
            print("Газировка без добавок")

apple_soda = Soda("apple")
apple_soda.show_my_drink()

soda = Soda()
soda.show_my_drink()