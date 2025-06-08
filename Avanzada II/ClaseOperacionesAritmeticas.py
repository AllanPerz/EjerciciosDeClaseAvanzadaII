#Clase Operaciones Aritmeticas

class OperacionesAritmeticas:
    def __init__(self, a , b):
        self.a=a
        self.b=b

    def suma(self):
        return self.a + self.b
    
    def resta(self):
        return self.a - self.b
    
    def multiplicacion(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b