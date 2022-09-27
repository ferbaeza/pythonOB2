def main():
    nombre=[]
    agenda ={
        "nombre":"",
        "telefono":""
    }
    stop = True
    while stop:
        print("****************************")
        print("****************************")
        print(f"Ejercicio Dos")
        print("----------------------------")
        print("-Agenda de Contactos--------")
        print("-1---Ver agenda completa----")
        print("-2---Introducir contacto----")
        print("-3---Buscar un contacto-----")
        print("----------------------------")
        print("-0---Salir------------------\n")
        print("****************************")
        print("****************************")
        option=int(input("Selecciona una opcion: "))
        if option ==0:
            stop = False
        elif option ==1:
            print("\n")
            print("Agenda")
            print("Nombres--Telefonos")
            for i in nombre:
                print(i)
            print("\n\n")
        elif option ==2:
            print("\n")
            name= str(input("Nombre: "))
            num= str(input("Numero: "))
            entry = name +"  --  "+num
            nombre.append(entry)
        elif option ==3:
            find = str(input("Introduce el nombre que quieres buscar: "))
            print("\n")
            for i in nombre:
                if i.lower().startswith(find):
                    print(i)
            print("\n")



if __name__=="__main__":
    main()