class Consolas:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Modalidad(Consolas):
    def __init__(self, marca, modelo, modalidad):
        super().__init__(marca, modelo)
        self.modalidad = modalidad
        
class Consola_completa(Modalidad):
    def mostrar_info(self):
        print(f"Consola: {self.marca} {self.modelo}")
        print(f"Modalidad: {self.modalidad}")
        
consola1 = Consola_completa("Sony", "PlayStation 5", "Consola de mesa")
consola1.mostrar_info()