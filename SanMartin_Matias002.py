def validar(num):
    if num<0:
        print("Los puntos no pueden ser menor a 0")
        return False

    if num>150:
        print("Los puntos no pueden ser mayor a 150")
        return False
    else:
        lis=[id,nombre,ptos]
        lista.append(lis)

def promedio(a,b):
    total=a/b
    
acum_ptos=0    
contador=0
import csv
lista=[]
while(True):
    print(".-.-.-M E N U  R E G I S T R O S.-.-.-")
    print("")
    print("1.-Agregar equipo")
    print("2.-Listar equipo")
    print("3.-actualizar nombre de equipo por id")
    print("4.-Generar BBDD")
    print("5.-Cargar BBDD")
    print("6.-Estadisticas")
    print("0.-Salir")
    op=int(input("Ingrese una opcion : "))
    if op==1:
        print("----Agregar Equipo----")
        id=int(input("Ingrese ID del Equipo : "))
        nombre=input("Ingrese nombre del equipo : ")
        ptos=int(input("Ingrese puntos del equipo"))
        acum_ptos=acum_ptos+ptos
        validar(ptos)
        contador=contador+1
     
        #lis=[id,nombre,ptos]
        #lista.append(lis)
        
    elif op==2:
        for p in lista:
            print(f"ID : {p[0]} nombre : {p[1]} ptos : {p[2]} ")
            print("--------------------")

    elif op==3:
        print("----Actualizar nombre----")
        act=int(input("Ingrese Id para actualizar nombre : "))
        for p in lista[0]:
            if p==act:
                print("id encontrado")
                nombre=input("Ingrese nuevo nombre : ")
                
            
                
    elif op==4:
        with open('bbdd_equipo.csv','w',newline='')as bbdd_equipo:
            escritor_csv=csv.writer(bbdd_equipo)
            escritor_csv.writerows(['id','nombre','ptos'])
            escritor_csv.writerows(lista)
            print("Base de datos creada")

    elif op==5:
        cont=0
        with open ('bbdd_equipo.csv','r',newline='')as bbdd_equipo:
            lector_csv=csv.reader(bbdd_equipo)
            for fila in lector_csv:
                if cont==0:
                    cont=cont+1
                    continue
            i=int(fila[0])
            n=fila[1]
            p=int(fila[2])
            lis_chica=[i,n,p]
            lista.append(lis_chica)
        
    elif op==6:
        print("----Estadisticas----")
        total=promedio(acum_ptos,contador)
        print(f"Promedio puntos equipos : {total}")
        
        
                
