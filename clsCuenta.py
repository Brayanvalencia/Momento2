from datetime import date
from datetime import datetime

class Cuenta:
    cedula = 0
    nombre = ''
    fecha = ''
    cantidad = 0.0
    resta = 0

#Contructor
    def __init__(self,cedula,nombre,fecha):
        self.cedula = cedula
        self.nombre = nombre
        self.fecha = fecha
        self.cantidad

    def __str__(self):        
        return """
cedula: {}
nombre: {}
fecha: {}
cantidad: {}""".format(self.cedula,self.nombre,self.fecha,self.cantidad)

#Método Ingresar y Retirar
    def ingresar(self, cantidad):
        self.cantidad = self.cantidad + cantidad
        if self.cantidad < 0:
            print("Ingrese una cantidad positiva")
        else:            
            print("Se ingreso una nueva cantidad a tu cuenta: ",cantidad)

    
    def retirar(self, cantidad):
        self.cantidad = self.cantidad - cantidad
        if self.cantidad < cantidad:            
            print("Cantidad de la cuenta: ", self.resta)            
        else:
            print("Esto fue lo que ustde retiro de su cuenta: ", cantidad)

#Metodo get
    def get_Cedula(self):
        return self.cedula
    
    def get_Nombre(self):
        return self.nombre
    
    def get_Fecha(self):
        return self.fecha
    
    def get_Cantidad(self):
        return self.cantidad

        
    #Metodo set

    def set_Cedula(self, NewCedula):
        self.cedula = NewCedula

    def set_Nombre(self, NewNombre):
        self.nombre = NewNombre

    def set_Fecha(self, NewFecha):
        self.fecha = NewFecha

    def set_Cantidad(self, NewCantidad):
        self.cantidad = NewCantidad
