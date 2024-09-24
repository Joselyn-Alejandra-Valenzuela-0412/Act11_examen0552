print("EXAMEN JOSELYN VALENZUELA 0552")
print("CLASE EDITORIAL")

class Editorial:
# zona de atributos
    ID_edit=0
    nombre=0
    pais=0
    año_fundac=0
    fundador=0
    correo=0
    proyectos=0
#zona de funciones
    def mostrar_0552(self): 
        print(f"****************datos de la editorial*************")
    def lista_idedit0552(self):
        IDeditorial=["40060","10043","30987","44441","22321"]
        print(IDeditorial)
        for identificaciones in IDeditorial:
            print(identificaciones)
    def tupla_paised0552(self):
        paisEditor=("mexico","USA","rusia","francia","brasil")
        print(paisEditor)
        for paises in paisEditor:
            print(paises)
    def conjunto_añoedit0552(self):
        añoEditor={"1985","2000","2001","1999","2002"}
        print(añoEditor)
        for epoca in añoEditor:
            print(epoca)
    def dic_proyectos0552(self):
        obras={"obra 1: ": "jujutsu kaisen","obra 2: ":"shingeki no kyojin","obra 3: ":"chainsaw man","obra 4: ":"yuri on ice","obra 5: ":"free"}
        print(obras)
        for numero,titulos in obras.items():
            print(numero,titulos)
    def estado0552(self,n):
        print(f"{n} : editorial activa")

#zona de objetos
edit=Editorial()


#llamar funciones
print("*******************resultados de editorial****************************")
edit.ID_edit=45454
edit.nombre="PANINI MANGA"
edit.pais="MEXICO"
edit.año_fundac=1998
edit.fundador="HIRO MURATAWA"
edit.correo="paninin123@gmail.com"
edit.proyectos="jjk, yuri on ice, free "
print(f"id: {edit.ID_edit}")
print(f"nombre: {edit.nombre}")
print(f"pais de editorial: {edit.pais}")
print(f"año fundacion: {edit.año_fundac}")
print(f"nombre del fundador: {edit.fundador}")
print(f"correo editorial: {edit.correo}")
print(f"proyectos activos: {edit.proyectos}")
edit.estado0552("panini manga")
edit.mostrar_0552()
edit.lista_idedit0552()
edit.tupla_paised0552()
edit.conjunto_añoedit0552()
edit.dic_proyectos0552()


