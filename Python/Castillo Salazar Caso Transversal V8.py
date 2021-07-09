import numpy as np

## DECLARACION DE VARIABLES

age = 0
gender = "M"
diagnosis = ""
remedy = ""
name = ""
lastn = ""
rut = 0


## ARREGLOS PRINCIPALES

name = np.empty(5, dtype='object')
lastn = np.empty(5,dtype='object')
rut = np.empty(5,dtype='int')
age = np.empty(5,dtype='int')
gender = np.empty(5,dtype='object')
diagnosis = np.empty(5,dtype='object')
remedy = np.empty(5,dtype='object')

##DECLARAR FUNCIONES (INGRESAR DATOS-OPCION 1)
def enter_data(name,lastn,rut,age,gender,diagnosis,remedy,largo):
    for i in range(0,5):
        while True:
            name[i] = input(f"NOMBRE_PACIENTE {i+1}:   ").upper()
            if(name[i] == ""):
                print("- - -Ingrese nombre PACIENTE Nuevamente- - -")
            else:
                break

        while True:
            lastn[i] = input(f"APLLIDO_PACIENTE {i+1}:   ").upper()
            if(lastn[i]==""):
                print("- - -Ingrese Apellido PACIENTE nuevamente- - -")
            else:
                break

        while True:
            rut[i] = int(input(f"RUT_PACIENTE {i+1}:   "))
            if(rut[i] == ""):
                print("- - -Ingrese RUT PACIENTE Nuevamente- - -")
            else:
                break

        while True:
            age[i] = int(input(f"EDAD_PACIENTE {i+1}:   "))
            if(age[i] >= 0 and age[i] <= 120):
                break
            else:
                print("- - -Ingrese EDAD PACIENTE Nuevamente- - -")
        while True:
            gender[i] = input(f"GENERO_PACIENTE(F)(M) {i+1}:   ").upper()
            if(gender[i] == "M"):
                break
            elif(gender[i] == "F"):
                break
            else:
                print("- - -Ingrese Edad PACIENTE Nuevamente- - -")

        diagnosis[i] = input(f"DIAGNOSTICO_PACIENTE {i+1}:   ")
        remedy[i] = input(f"MEDICAMENTOS_PACIENTE {i+1}:   ")
        cont =input("INGRESAR OTRO PACIENTE???(S)(N):   ").upper()
        if(cont == "N"):
            break
        print("-----------------------------------------")


##DECLARAR FUNCIONES (BUSCAR DATOS-OPCION 2)
def find_patient(rut,largo):
    rut_buscado = int(input("RUT_PACIENTE:  "))
    ac = False
    for i in range(0,5):
            if(rut_buscado == rut[i]):
                ac = True
                ind = i
    if(ac == True):
        print(f"NOMBRE_PACIENTE: {name[ind]}")
        print(f"APELLIDO_PACIENTE: {lastn[ind]}")
        print(f"EDAD_PACIENTE: {age[ind]}")
        print(f"GENERO_PACIENTE: {gender[ind]}")
        print("-----------------------------------------")
    else:
        print("- - -RUT NO EXISTE- - -")
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("++++++++++CLINICA DUOC UC+++++++++++++++++")
        print("++++++++++++++++++++++++++++++++++++++++++")

##DECLARAR FUNCIONES (BUSCAR MEDICAMENTEOS-OPCION 3)
def medicine(rut,largo):
    rut_buscado = int(input("RUT_PACIENTE:  "))
    ac = False
    for i in range(0,5):
        if(rut_buscado == rut[i]):
            ac = True
            ind = i
    if(ac == True):
        print(f"REMEDIOS_PACIENTE {name[ind]} son: {remedy[ind]}")
        print("+++++++++++++++++++++++++++++++++++++++++")
    else:
        print("- - -RUT NO EXISTE- - -")
        print("+++++++++++++++++++++++++++++++++++++++++")

##DECLARAR FUNCIONES (ELIMINAR DATOS-OPCION 4)
def delete_data(rut,largo):
    rut_buscado = int(input("RUT PACIENTE:   "))
    ac = False
    for i in range(0,5):
        if(rut_buscado == rut[i]):
            ac = True
            ind = i
    if(ac == True):
        print("- - -FICHA ELIMINADA- - -")
        name[ind] = ""
        lastn[ind] = ""
        rut[ind] = 0
        age[ind] = 0
        gender[ind] = ""
        diagnosis[ind] = ""
        remedy[ind] = ""
    else:
        print("- - -RUT NO EXISTE- - -")
##DECLARAR FUNCIONES (LISTAR DATOS-OPCION 5)
def patient_list(name,lastn,rut,age,gender,diagnosis,remedy,largo):
    for i in range(0,5):
        print(f"RUT_PACIENTE es {i+1}: {rut[i]}")
        print(f"NOMNRE_PACIENTE {i+1}: {name[i]}")
        print(f"APELLIDO_PACIENTE  {i+1}: {lastn[i]}")
        print(f"EDAD_PACIENTE es {i+1}: {age[i]}")
        print(f"GENERO_PACIENTE  {i+1}: {gender[i]}")
        print("-----------------------------------------")




## MENSAJE DE INICIO

while True:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")    
    print("|   |||||||    |||   |||   |||||    ||||||||    |||   |||  |||||||||   |")
    print("|   |||  |||   |||   |||  ||   ||  |||          |||   ||| |||          |")
    print("|   |||  ||||  |||   ||| |||   ||| |||          |||   ||| |||          |")
    print("|   |||  ||||  |||   ||| |||   ||| |||          |||   ||| |||          |")
    print("|   |||  |||   |||   |||  ||   ||  |||          |||   ||| |||          |")  
    print("|   |||||||     |||||||    |||||    ||||||||     |||||||   |||||||||   |")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("-------------------------CLINICA DUOC UC--------------------------------")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

## MENU PRINCIPAL    
    print("(1) - FICHA PACIENTE")
    print("(2) - BUSCAR FICHA")
    print("(3) - BUSCAR MEDICAMENTO")
    print("(4) - ELIMINAR FICHA PACIENTE")
    print("(5) - LISTA PACIENTES ")
    print("(6) - SALIR")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    while True:
        while True:
            try:
                opcion = int(input("SELECCIONE UNA OPCION:  "))
                break
            except ValueError:
                print("- - - Ingresar Solo Numeros- - -")
        if(opcion>=1 and opcion<=6):
            break
        else:
            print("- - -OPCION NO VALIDA - - -")
            print("VALIDO (1)(2)(3)(4)(5)(6)")
## VALIDACION DE OPCIONES            
    if(opcion == 1):
        enter_data(name,lastn,rut,age,gender,diagnosis,remedy,5)

    if(opcion == 2):
        find_patient(rut,5)
                     
    if(opcion == 3):
        medicine(rut,5)
        
    if(opcion == 4):
        delete_data(rut,5)

    if(opcion == 5):
        patient_list(name,lastn,rut,age,gender,diagnosis,remedy,5)
## SALIDA O FIN DEL PROGRAMA
    if(opcion == 6):
        break
            
        
        
                
        
            
            
            
