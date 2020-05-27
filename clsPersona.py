import random
class Persona:

    nombre = ''
    edad = 0
    correo = ''
    DNI = 0
    sexo = 'Hombre'
    peso = 0.0
    altura = 0.0
    form_1 = -1
    form_2 = 0
    form_3 = 1

#Constructor por defecto
    def __init__(self):
        self.nombre = ''
        self.edad = 0
        self.correo  = ''
        self.DNI = 0
        self.sexo = ''
        self.peso = 0.0
        self.altura = 0.0

    def __str__(self):        
        return """
Nombre: {}
Edad: {}
Correo: {}
DNI: {}
Sexo: {}
Peso: {}
Altura: {}""".format(self.nombre,self.edad,self.correo,self.DNI,self.sexo,self.peso,self.altura)

#Métodos
    def calcularIMC(self):
        if self.peso < 20:
            self.peso = (self.peso / (self.altura*2))
            print(self.form_1)
        elif self.peso >= 20 and self.peso < 25:
            print("Estas por debajo de tu peso ideal: ",self.form_2)
        else:
            print("Cuida tu sobre peso: ",self.form_3)
        

    def esMayorDeEdad(self):
        if self.edad > 18:
            print(True)
        else:
            print(False)

    def comprobarSexo(self):
        if self.sexo == "Hombre":
            print("Es correto!")
        else:
            print("No seras visible al exterior")

    def generaDNI(self):
        print(random.uniform(0,8))

#Método Get

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self, ):
        return self.edad

    def get_correo(self):
        return self.correo
    
    def get_sexo(self):
        return self.sexo
    
    def get_peso(self):
        return self.peso

    def get_altura(self):
        return self.altura

#Métodos Set
    def set_nombre(self, NuevoNom):
        self.nombre = NuevoNom
    
    def set_edad(self, NuevaEdad):
        self.edad = NuevaEdad

    def set_correo(self, NuevoCorreo):
        self.correo = NuevoCorreo
    
    def set_sexo(self, NuevoSexo):
        self.sexo = NuevoSexo
    
    def set_peso(self, NuevoPeso):
        self.peso = NuevoPeso

    def set_altura(self, NuevaAltura):
        self.altura = NuevaAltura

# #Constructor con nombre edad y sexo 
class Constructor2(Persona):
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.correo
        self.DNI
        self.peso
        self.altura
    
    def __str__(self):        
        return """
Nombre: {}
Edad: {}
Correo: {}
DNI: {}
Sexo: {}
Peso: {}
Altura: {}""".format(self.nombre,self.edad,self.correo,self.DNI,self.sexo,self.peso,self.altura)

#Métodos
    def calcularIMC(self):
        if self.peso < 20:
            self.peso = (self.peso / (self.altura*2))
            print(self.form_1)
        elif self.peso >= 20 and self.peso < 25:
            print("Estas por debajo de tu peso ideal: ",self.form_2)
        else:
            print("Cuida tu sobre peso: ",self.form_3)
        

    def esMayorDeEdad(self):
        if self.edad > 18:
            print(True)
        else:
            print(False)

    def comprobarSexo(self):
        if self.sexo == "Hombre":
            print("Es correto!")
        else:
            print("No seras visible al exterior")

    def generaDNI(self):
        print(random.uniform(0,8))

#Método Get

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self, ):
        return self.edad

    def get_correo(self):
        return self.correo
    
    def get_sexo(self):
        return self.sexo
    
    def get_peso(self):
        return self.peso

    def get_altura(self):
        return self.altura

#Métodos Set
    def set_nombre(self, NuevoNom):
        self.nombre = NuevoNom
    
    def set_edad(self, NuevaEdad):
        self.edad = NuevaEdad

    def set_correo(self, NuevoCorreo):
        self.correo = NuevoCorreo
    
    def set_sexo(self, NuevoSexo):
        self.sexo = NuevoSexo
    
    def set_peso(self, NuevoPeso):
        self.peso = NuevoPeso

    def set_altura(self, NuevaAltura):
        self.altura = NuevaAltura

#Constructor con todos los atributos como parametro
class Constructor3(Persona):
    def __init__(self, nombre, edad, correo,DNI,sexo,peso,altura):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def __str__(self):        
        return """
Nombre: {}
Edad: {}
Correo: {}
DNI: {}
Sexo: {}
Peso: {}
Altura: {}""".format(self.nombre,self.edad,self.correo,self.DNI,self.sexo,self.peso,self.altura)
    
#Métodos

    def calcularIMC(self):
        if self.peso < 20:
            self.peso = (self.peso / (self.altura*2))
            print(self.form_1)
        elif self.peso >= 20 and self.peso < 25:
            print("Estas por debajo de tu peso ideal: ",self.form_2)
        else:
            print("Cuida tu sobre peso: ",self.form_3)
        

    def esMayorDeEdad(self):
        if self.edad > 18:
            print(True)
        else:
            print(False)

    def comprobarSexo(self):
        if self.sexo == "Hombre":
            print("Es correto!")
        else:
            print("No seras visible al exterior")

    def generaDNI(self):
        print(random.uniform(0,8))

#Método Get

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self, ):
        return self.edad

    def get_correo(self):
        return self.correo
    
    def get_sexo(self):
        return self.sexo
    
    def get_peso(self):
        return self.peso

    def get_altura(self):
        return self.altura

#Métodos Set
    def set_nombre(self, NuevoNom):
        self.nombre = NuevoNom
    
    def set_edad(self, NuevaEdad):
        self.edad = NuevaEdad

    def set_correo(self, NuevoCorreo):
        self.correo = NuevoCorreo
    
    def set_sexo(self, NuevoSexo):
        self.sexo = NuevoSexo
    
    def set_peso(self, NuevoPeso):
        self.peso = NuevoPeso

    def set_altura(self, NuevaAltura):
        self.altura = NuevaAltura