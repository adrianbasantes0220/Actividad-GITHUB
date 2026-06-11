class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        return f"{self.nombre} el {self.raza} está ladrando."
    
perro1 = Perro("Rex", "Labrador")
print(perro1.ladrar())  