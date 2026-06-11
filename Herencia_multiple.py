class Dispositivos_Electronicos:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo

class Garantia:
    def __init__(self, duracion):
        self.duracion = duracion

class Consumo_energia:
    def __init__(self, consumo):
        self.consumo = consumo
    
class Precio:
    def __init__(self, precio):
        self.precio = precio
        
class Televisor(Dispositivos_Electronicos, Garantia, Consumo_energia, Precio):
    def __init__(self, nombre, modelo, duracion, consumo, precio):
        Dispositivos_Electronicos.__init__(self, nombre, modelo)
        Garantia.__init__(self, duracion)
        Consumo_energia.__init__(self, consumo)
        Precio.__init__(self, precio)
        
    def mostrar_info(self):
        print(f"Televisor: {self.nombre} {self.modelo}")
        print(f"Garantía: {self.duracion} años")
        print(f"Consumo: {self.consumo} kWh")
        print(f"Precio: ${self.precio}")
        
televisor1 = Televisor("Samsung", "QLED", 2, 150, 1200)
televisor1.mostrar_info()