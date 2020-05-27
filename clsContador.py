class Contador():    

    #Constructor por defecto
    def __init__(self): 
        self.incrementar = 0
        self.decrementar = 0.0

    #Constructor con parametros

    # def __init__(self, incrementar, decrementar):
    #     self.incrementar = incrementar
    #     self.decrementar = decrementar

#Metodo Get

    def get_incrementar(self):
        return self.incrementar

    def get_decrementar(self):
        return self.decrementar

#Metodo Set

    def set_incrementar(self, NewIncrementar):
        self.incrementar = NewIncrementar

    def set_decrementar(self, NewDecrementar):
        self.decrementar = NewDecrementar