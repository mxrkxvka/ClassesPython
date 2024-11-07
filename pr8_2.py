class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not (isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)) and isinstance(self.c, (int, float))):
            print("Нужно вводить только числа!")
        elif self.a <= 0 or self.b <= 0 or self.c <= 0:
            print("С отрицательными числами ничего не выйдет!")
        elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print("Ура, можно построить треугольник!")
        else:
            print("Жаль, но из этого треугольник не сделать.")
        
correct_triangle = TriangleChecker(3, 4, 5)
correct_triangle.is_triangle()

incorrect_triangle_1 = TriangleChecker(-3, -4, -5)
incorrect_triangle_1.is_triangle()

incorrect_triangle_2 = TriangleChecker(1, 1, 3)
incorrect_triangle_2.is_triangle()
