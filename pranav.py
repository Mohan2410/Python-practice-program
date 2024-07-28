class Rectangle:
    def set_data(self,l,b):
        self.L = l
        self.B = b

        def set_area(self):
            A = self.L * self.B
            print("Area is: ",A)

        def perimeter(self):
            P = 2(self.L + self.B)
            print("Perimeter is: ",P)

a = Rectangle()
a.set_data(5,6)
a.area()
a.perimeter()
