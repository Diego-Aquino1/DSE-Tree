class Persona:
    def __init__(self, nombre_):
        self.nombre = nombre_
        self.padre = None
        self.madre = None
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padre = self

    def agregar_hija(self, hija):
        self.hijos.append(hija)
        hija.madre = self

    def buscar_padre(self):
        return self.padre.nombre if self.padre else None

    def buscar_madre(self):
        return self.madre.nombre if self.madre else None

    def buscar_tios(self):
        tios = []
        if self.padre:
            abuelo_paterno = self.padre.padre
            if abuelo_paterno:
                for hijo in abuelo_paterno.hijos:
                    if hijo != self.padre:
                        tios.append(hijo.nombre)
        if self.madre:
            abuela_materna = self.madre.madre
            if abuela_materna:
                for hijo in abuela_materna.hijos:
                    if hijo != self.madre:
                        tios.append(hijo.nombre)
        return tios

    def buscar_primos(self):
        primos = []
        if self.padre:
            abuelo_paterno = self.padre.padre
            if abuelo_paterno:
                for hijo in abuelo_paterno.hijos:
                    if hijo != self.padre:
                        primos.extend(hijo.hijos)
        if self.madre:
            abuela_materna = self.madre.madre
            if abuela_materna:
                for hijo in abuela_materna.hijos:
                    if hijo != self.madre:
                        primos.extend(hijo.hijos)
        return [primo.nombre for primo in primos]
    
    def mostrar_arbol(persona, nivel=0):
        prefijo = "   " * nivel
        print(prefijo + "|-- " + persona.nombre)
        for hijo in persona.hijos:
            mostrar_arbol(hijo, nivel + 1)



# Creación de las personas
bisabueloP = Persona("Bisabuelo Paterno")
bisabuelaP = Persona("Bisabuela Paterna")
bisabueloM = Persona("Bisabuelo Materno")
bisabuelaM = Persona("Bisabuela Materna")

abueloP = Persona("Julian")
abuelaP = Persona("Susana")
abueloM = Persona("Genaro")
abuelaM = Persona("Abuela Materna")

papa = Persona("Cesar")
mama = Persona("Gladys")

tio1 = Persona("Hugo")
tio2 = Persona("Alberto")

tio1 = Persona("Hugo")
tio2 = Persona("Alberto")
tio3 = Persona("Renzo")
tia1 = Persona("Susan")
tia2 = Persona("Yenny")

hijo = Persona("Diego")
primo = Persona("Jhostin")

persona6 = Persona("Tío")
persona7 = Persona("Primo")


bisabueloP.agregar_hijo(abuelaP)
bisabuelaP.agregar_hija(abuelaP)
bisabueloM.agregar_hijo(abuelaM)
bisabuelaM.agregar_hija(abuelaM)

abueloM.agregar_hijo(tio1)
abueloM.agregar_hijo(tio2)
abuelaM.agregar_hija(mama)

abueloP.agregar_hijo(papa)
abueloP.agregar_hijo(tio3)
abuelaP.agregar_hija(tia1)
abuelaP.agregar_hija(tia2)

papa.agregar_hijo(hijo)
tia1.agregar_hijo(primo)

# Ejemplo de uso
print(hijo.buscar_padre()) 
print(tia1.buscar_madre()) 
print(hijo.buscar_tios())  
print(hijo.buscar_primos())