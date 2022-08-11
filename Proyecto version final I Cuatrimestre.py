import os
#modulo de informes
nacionalcash=[0]
extranjerocash=[0]
tHorario1=[0, 0, 0]
tHorario2=[0, 0, 0]
tHorario3=[0, 0, 0]
tHorario4=[0, 0, 0]
maximostr=[0, 0, 0]
minstr=[0, 0, 0]
#modulo de reservas
horario1=[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
horario2=[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
horario3=[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
horario4=[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
factura=[]
creservas=[0]
#menu principal
def menuPrincipal():
    os.system("cls")
    print("\nBienvenido a Aventuras 'El paraiso'\n\nDigite 1 para ingresar al modulo de reservas\nDigite 2 para ingresar al modulo de facturas\nDigite 3 para ingresar al modulo de informes\nDigite 4 para salir del programa\n")
    menu=int(input("Digite el numero del menu al que quiera ingresar: "))
    if menu>5 or menu<1:
        print(menuIncorrecto())
    if menu==1:
        print(menuReservas())
    elif menu==2:
        print(moduloFactura())
    elif menu==3:
        print(moduloInformes())
    else:
        print(terminarPrograma())
#si se introduce mal el numero del menu
def menuIncorrecto():
    print("\nError, porfavor ingrese un numero de menu valido")
    print(menuPrincipal())
def menuReservas():
        os.system("cls")
        #reinicio de variables
        nacional_niño=0
        nacional_adultomayor=0
        nacional_adulto=0
        extranjero_niño=0
        extranjero_adultomayor=0
        extranjero_adulto=0
        #Ingreso de datos
        print("\nBienvenido al Módulo de Reservas\n\nA continuacion le vamos a pedir el numero de personas y el horario que desea reservar\n\nRecuerde que el maximo de personas por horario es 18\n\nLas opciones de horario son:\n\n1= 8:00 am\n2= 10:00 am\n3= 12:00 md\n4= 2:00 pm\n\n")
        nombre=input("Escriba su nombre completo: ")
        factura[creservas[0]][0]=nombre
        cedula=int(input("Digite los numeros de su cedula: "))
        factura[creservas[0]][1]=cedula
        numero_personas=int(input("Digite el numero de personas: "))
        numero_horario=int(input("Digite el numero del horario que desea reservar: "))
        #Este while es para cerciorarse que el usuario de un numero de personas y un numero de horario valido
        while ((numero_personas>18 or numero_personas<1) or (numero_horario>4 or numero_horario<1)):
          print("\nError, estas son las instrucciones, porfavor ingrese los datos de nuevo\nRecuerde que el maximo de personas por horario es 18\n\nLas opciones de horario son\n1= 8:00 am\n2= 10:00 am\n3= 12:00 md\n4= 2:00 pm\n")
          numero_personas=int(input("Digite el numero de personas: "))
          numero_horario=int(input("Digite el numero del horario que desea reservar: "))
          #usuarios_faltantes=numero_personas
          #Este if es para asignar el horario dependiendo del numero
        factura[creservas[0]][4]=numero_personas
        if numero_horario==1:
            horarioinf="8:00 am"
        elif numero_horario==2:
            horarioinf="10:00 am"
        elif numero_horario==3:
            horarioinf="12:00 md"
        else:
            horarioinf="2:00 pm"
        factura[creservas[0]][3]=horarioinf
        print("\nEspecifique si la persona es nacional o extranjera y si es niño o adulto mayor\n\n1= Nacional y 2= Extranjero\n1= Niño, 2= Adulto Mayor y 3= Adulto\n\n")
        #Este for es para sacar la nacionalidad y si son niños o adultos mayores(El numero de personas) mas adelante se usan las variables para sacar la cantidad de dinero    
        for i in range(numero_personas):
            nacionalidad=int(input("\nDigite el numero de la nacionalidad de la persona numero #"+str(i+1)+": "))
            condicion=int(input("Digite el numero de la condicion de la persona numero #"+str(i+1)+": "))        
            #Este while es para asegurarse que la persona cargue un dato correcto       
            while nacionalidad<1 or nacionalidad>2 or condicion<1 or condicion>3:           
                print("\nPorfavor ingrese un dato correcto, estas son las instrucciones:\n\n1= Nacional y 2= Extranjero\n1= Niño, 2= Adulto Mayor y 3= Adulto\n\n")
                nacionalidad=int(input("\nDigite el numero de la nacionalidad de la persona numero #"+str(i+1)+": "))
                condicion=int(input("Digite el numero de la condicion de la persona numero #"+str(i+1)+": "))
            if nacionalidad==1 and condicion==1:
                nacional_niño+=1
            elif nacionalidad==1 and condicion==2:
                nacional_adultomayor+=1
            elif nacionalidad==1 and condicion==3:
                nacional_adulto+=1
            elif nacionalidad==2 and condicion==1:
                extranjero_niño+=1
            elif nacionalidad==2 and condicion==2:
                extranjero_adultomayor+=1
            elif nacionalidad==2 and condicion==3:
                extranjero_adulto+=1 
        #variables para el registro de tipo de visitante y dinero generado
        #cantidades
        cant_nacionales=nacional_niño+nacional_adultomayor+nacional_adulto
        factura[creservas[0]][5]=cant_nacionales
        cant_extranjeros=extranjero_niño+extranjero_adultomayor+extranjero_adulto
        factura[creservas[0]][6]=cant_extranjeros
        cant_niños=nacional_niño+extranjero_niño
        factura[creservas[0]][7]=cant_niños
        cant_adultomayor=nacional_adultomayor+extranjero_adultomayor
        factura[creservas[0]][8]=cant_adultomayor
        cant_adultos=nacional_adulto+extranjero_adulto
        factura[creservas[0]][9]=cant_adultos
        #precios
        precio_adultos=(nacional_adulto*5000)+(extranjero_adulto*7000)
        factura[creservas[0]][12]=precio_adultos
        precio_niños=(nacional_niño*2500)+(extranjero_niño*3500)
        factura[creservas[0]][10]=precio_niños
        precio_adultomayor=(nacional_adultomayor*2500)+(extranjero_adultomayor*3500)
        factura[creservas[0]][11]=precio_adultomayor
        precio_total=precio_adultos+precio_adultomayor+precio_niños
        factura[creservas[0]][13]=precio_total
        #informes
        nacionalcash[0]+=(nacional_niño*2500)+(nacional_adultomayor*2500)+(nacional_adulto*5000)
        extranjerocash[0]+=(extranjero_adulto*7000)+(extranjero_niño*3500)+(extranjero_adultomayor*3500)
        #listas por si hay mas personas de las que se puede en la reserva y para el informe
        espaciosguardados=[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
        infoguardados=[[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]
        campos=[]
        #horario1
        if numero_horario==1: 
           personas=numero_personas
           if personas>0:
            for i in range(6): 
             if horario1[0][i]==0 and personas>0:
              horario1[0][i]=1
              personas-=1
              espaciosguardados[0][i]=1
              infoguardados[0][i]=1
           if personas>0:
            for i in range(6): 
             if horario1[1][i]==0 and personas>0:
              horario1[1][i]=1
              personas-=1
              espaciosguardados[1][i]=1
              infoguardados[1][i]=1
           if personas>0:
            for i in range(6): 
             if horario1[2][i]==0 and personas>0:
              horario1[2][i]=1
              personas-=1
              espaciosguardados[2][i]=1
              infoguardados[2][i]=1
           if personas>0:
            print("\nEn los telefericos faltan espacios para",personas,"personas. Tienen que ser menos de",str(numero_personas-personas),"o pueden probar otro horario...")
            for t in range(3):
              for e in range(6):
                  if espaciosguardados[t][e]==1:
                    horario1[t][e]=0
            print(menuPrincipal())
        #horario2    
        if numero_horario==2:
          personas=numero_personas
          if personas>0:
            for i in range(6): 
              if horario2[0][i]==0 and personas>0:
                horario2[0][i]=1
                personas-=1
                espaciosguardados[0][i]=1
                infoguardados[0][i]=1
          if personas>0:
            for i in range(6): 
              if horario2[1][i]==0 and personas>0:
                horario2[1][i]=1
                personas-=1
                espaciosguardados[1][i]=1
                infoguardados[1][i]=1
          if personas>0:
            for i in range(6): 
             if horario2[2][i]==0 and personas>0:
               horario2[2][i]=1
               personas-=1
               espaciosguardados[2][i]=1
               infoguardados[2][i]=1
          if personas>0:
            print("\nEn los telefericos faltan espacios para",personas,"personas. Tienen que ser menos de",str(numero_personas-personas),"o pueden probar otro horario...")
            for t in range(3):
               for e in range(6):
                   if espaciosguardados[t][e]==1:
                    horario2[t][e]=0
            print(menuPrincipal())
        #horario3
        if numero_horario==3:
          personas=numero_personas
          if personas>0:
            for i in range(6): 
              if horario3[0][i]==0 and personas>0:
                horario3[0][i]=1
                personas-=1
                espaciosguardados[0][i]=1
                infoguardados[0][i]=1
          if personas>0:
            for i in range(6): 
               if horario3[1][i]==0 and personas>0:
                 horario3[1][i]=1
                 personas-=1
                 espaciosguardados[1][i]=1
                 infoguardados[1][i]=1
          if personas>0:
             for i in range(6): 
                if horario3[2][i]==0 and personas>0:
                   horario3[2][i]=1
                   personas-=1
                   espaciosguardados[2][i]=1
                   infoguardados[2][i]=1
          if personas>0:
           print("\nEn los telefericos faltan espacios para",personas,"personas. Tienen que ser menos de",str(numero_personas-personas),"o pueden probar otro horario...")
           for t in range(3):
              for e in range(6):
                if espaciosguardados[t][e]==1:
                  horario3[t][e]=0
           print(menuPrincipal())
        #horario4
        if numero_horario==4:
           personas=numero_personas
           if personas>0:
            for i in range(6): 
              if horario4[0][i]==0 and personas>0:
                horario4[0][i]=1
                personas-=1
                espaciosguardados[0][i]=1
                infoguardados[0][i]=1
           if personas>0:
             for i in range(6): 
                if horario4[1][i]==0 and personas>0:
                   horario4[1][i]=1
                   personas-=1
                   espaciosguardados[1][i]=1
                   infoguardados[1][i]=1
           if personas>0:
             for i in range(6): 
               if horario4[2][i]==0 and personas>0:
                 horario4[2][i]=1
                 personas-=1
                 espaciosguardados[2][i]=1
                 infoguardados[2][i]=1
           if personas>0:
            print("\nEn los telefericos faltan espacios para",personas,"personas. Tienen que ser menos de",str(numero_personas-personas),"o pueden probar otro horario...")
            for t in range(3):
             for e in range(6):
                if espaciosguardados[t][e]==1:
                  horario4[t][e]=0
            print(menuPrincipal())
        #infos 
        for t in range(3):
          for e in range(6):
             #esto determina los campos que salen en la factura 
            if infoguardados[t][e]==1:
             string=("teleferico #"+str(t+1)+" asiento #"+str(e+1))
             campos.append(string)
        factura[creservas[0]][14]=(campos)
        #numero de reserva
        import random
        numero_reserva=random.randint(1,72)
        print("\nSU NUMERO DE RESERVA ES:",numero_reserva,"\nDirigase al modulo de facturas para ver su factura...")
        factura[creservas[0]][2]=numero_reserva
        creservas[0]=(creservas[0]+1)
        print(menuPrincipal())
def moduloFactura():
        os.system("cls")
        print("\nBienvenido al modulo de factura\n")
        numero_reserva_factura=int(input("Digite su numero de reserva: "))
        #Este while es por si el usuario ingresa un numero de reserva loquisimo    
        while numero_reserva_factura>72 or numero_reserva_factura<1:
            print("\nError, el numero de factura solo puede ser entre 1 y 72\nPorfavor ingrese un numero valido\n")
            numero_reserva_factura=int(input("Digite su numero de reserva: "))
        #esto revisa todas las facturas y manda la factura del numero de reservacion que se haya ingresado
        for i in range(creservas[0]):
            if factura[i][2]==numero_reserva_factura:
                 print("\n\nFACTURA\n\nTeleferico Aventuras 'El paraíso'\nNombre:",factura[i][0],"\nCedula:",factura[i][1],"\nReservacion #"+str(factura[i][2]),"\nHorario Reservado:",factura[i][3],"\n\nCantidad de personas:",factura[i][4],"\nNacionales:",factura[i][5],"\nExtranjeros:",factura[i][6],"\n\nNiños:",factura[i][7],"\nAdultos mayores:",factura[i][8],"\nAdultos:",factura[i][9],"\n\nPrecio total de los niños: ₡"+str(factura[i][10]),"\nPrecio total de los adultos mayores: ₡"+str(factura[i][11]),"\nPrecio total de los adultos: ₡"+str(factura[i][12]),"\nPrecio a pagar: ₡"+str(factura[i][13])+"\n\n")
                 for c in range(factura[i][4]):
                     print("Espacio de la persona #"+str(c+1)+" :",factura[i][14][c])
                 #proceso de la factura en el txt   
                 archivofactura=open("factura.txt","w")
                 archivofactura.write("FACTURA\n")
                 archivofactura.write("Teleferico Aventuras 'El paraíso'\n")
                 archivofactura.write("Nombre: "+factura[i][0])
                 archivofactura.write("\nCedula: "+str(factura[i][1]))
                 archivofactura.write("\nReservacion #"+str(factura[i][2]))
                 archivofactura.write("\nHorario Reservado: "+factura[i][3])
                 archivofactura.write("\n\nCantidad de Personas: "+str(factura[i][4]))
                 archivofactura.write("\nNacionales: "+str(factura[i][5]))
                 archivofactura.write("\nExtranjeros: "+str(factura[i][6]))
                 archivofactura.write("\n\nNiños: "+str(factura[i][7]))
                 archivofactura.write("\nAdultos mayores: "+str(factura[i][8]))
                 archivofactura.write("\nAdultos :"+str(factura[i][9]))
                 archivofactura.write("\n\nPrecio total de los niños: "+str(factura[i][10])+" colones")
                 archivofactura.write("\nPrecio total de los adultos mayores: "+str(factura[i][11])+" colones")
                 archivofactura.write("\nPrecio total de los adultos: "+str(factura[i][12])+" colones")
                 archivofactura.write("\nPrecio a pagar: "+str(factura[i][13])+" colones\n\n")
                 for c in range(factura[i][4]):
                      archivofactura.write("Espacio de la persona #"+str(c+1)+" : "+factura[i][14][c]+"\n")
                 archivofactura.close()
                 print("Su factura esta guardada en su computadora en el archivo factura.txt")
                 print(menuPrincipal())
        print("Ese numero de reservacion no existe...")
        print(menuPrincipal())
def moduloInformes():
       os.system("cls")
       #calculo de cuantos persona llegaron por teleferico
       totalp=0
       for t in range(3):
         suma=0
         for e in range(6):
           suma+=horario1[t][e]
           totalp+=horario1[t][e]
         tHorario1[t]=(suma)
       for t in range(3):
         suma=0
         for e in range(6):
            suma+=horario2[t][e]
            totalp+=horario2[t][e]
         tHorario2[t]=(suma)
       for t in range(3):
         suma=0
         for e in range(6):
           suma+=horario3[t][e]
           totalp+=horario3[t][e]
         tHorario3[t]=(suma)
       for t in range(3):
         suma=0
         for e in range(6):
             suma+=horario4[t][e]
             totalp+=horario4[t][e]
         tHorario4[t]=(suma)
       print("\nMODULO DE INFORMES")
       print("\nLlegaron",totalp,"personas en total!")
       print("\nA las 8:00am llegaron: ",str(tHorario1[0]+tHorario1[1]+tHorario1[2]),"\nA las 10:00am llegaron: ",str(tHorario2[0]+tHorario2[1]+tHorario2[2]),"\nA las 12:00md llegaron: ",str(tHorario3[0]+tHorario3[1]+tHorario3[2]),"\nA las 2:00pm llegaron: ",str(tHorario4[0]+tHorario4[1]+tHorario4[2]),"\n\nEn el teleferico 1 viajaron: ",str(tHorario1[0]+tHorario2[0]+tHorario3[0]+tHorario4[0]),"\n\nEn el teleferico 2 viajaron: ",str(tHorario1[1]+tHorario2[1]+tHorario3[1]+tHorario4[1]),"\n\nEn el teleferico 3 viajaron: ",str(tHorario1[2]+tHorario2[2]+tHorario3[2]+tHorario4[2]))
       maximo=(tHorario1[0]+tHorario1[1]+tHorario1[2])
       minimo=(tHorario1[0]+tHorario1[1]+tHorario1[2])
       #maximo
       for i in range(3):
               maximostr[i]=(tHorario1[i])
               horariomax=1
       if (tHorario2[0]+tHorario2[1]+tHorario2[2])>maximo:
           maximo=(tHorario2[0]+tHorario2[1]+tHorario2[2])
           horariomax=2        
           for i in range(3):
               maximostr[i]=(tHorario2[i])
       if (tHorario3[0]+tHorario3[1]+tHorario3[2])>maximo:
           maximo=(tHorario3[0]+tHorario3[1]+tHorario3[2])
           horariomax=3        
           for i in range(3):
               maximostr[i]=(tHorario3[i]) 
       if (tHorario4[0]+tHorario4[1]+tHorario4[2])>maximo:
           maximo=(tHorario4[0]+tHorario4[1]+tHorario4[2])
           horariomax=4        
           for i in range(3):
               maximostr[i]=(tHorario4[i])
       #minimo 
       for i in range(3):
               minstr[i]=(tHorario1[i])
               horariomin="8:00 am" 
       if (tHorario2[0]+tHorario2[1]+tHorario2[2])<minimo:
           minimo=(tHorario2[0]+tHorario2[1]+tHorario2[2])
           horariomin="10:00 am"       
           for i in range(3):
               minstr[i]=(tHorario2[i])
       if (tHorario3[0]+tHorario3[1]+tHorario3[2])<minimo:
           minimo=(tHorario3[0]+tHorario3[1]+tHorario3[2])
           horariomin="12:00 md"         
           for i in range(3):
               minstr[i]=(tHorario3[i]) 
       if (tHorario4[0]+tHorario4[1]+tHorario4[2])<minimo:
           minimo=(tHorario4[0]+tHorario4[1]+tHorario4[2])
           horariomin="2:00 pm"          
           for i in range(3):
               minstr[i]=(tHorario4[i])
       print("\nEl horario con menos personas fue el horario",horariomin,"con",minimo,"personas en total\n")
       for i in range(3):
            print("Tuvo",minstr[i],"personas en el teleferico #"+str(i+1))
       print("\nEl horario con mas personas fue el horario",horariomax,"con",maximo,"personas en total\n")
       for i in range(3):
            print("Tuvo",maximostr[i],"personas en el teleferico #"+str(i+1))
       print("\nDinero generado por clientes nacionales: ₡"+str(nacionalcash[0]))
       print("Dinero generado por clientes extranjeros: ₡"+str(extranjerocash[0]))
       print("Dinero generado en total: ₡"+str(extranjerocash[0]+nacionalcash[0]))
       #proceso del txt de informes
       archivoinformes=open("informe.txt","w")
       archivoinformes.write("MODULO DE INFORMES")
       archivoinformes.write("\n\nLlegaron " +str(totalp)+" personas en total!")
       archivoinformes.write("\n\nA las 8:00am llegaron: "+str(tHorario1[0]+tHorario1[1]+tHorario1[2])+"\nA las 10:00am llegaron: "+str(tHorario2[0]+tHorario2[1]+tHorario2[2])+"\nA las 12:00md llegaron: "+str(tHorario3[0]+tHorario3[1]+tHorario3[2])+"\nA las 2:00pm llegaron: "+str(tHorario4[0]+tHorario4[1]+tHorario4[2])+"\n\nEn el teleferico 1 viajaron: "+str(tHorario1[0]+tHorario2[0]+tHorario3[0]+tHorario4[0])+"\n\nEn el teleferico 2 viajaron: "+str(tHorario1[1]+tHorario2[1]+tHorario3[1]+tHorario4[1])+"\n\nEn el teleferico 3 viajaron: "+str(tHorario1[2]+tHorario2[2]+tHorario3[2]+tHorario4[2]))
       archivoinformes.write("\n\nEl horario con menos personas fue el horario "+str(horariomin)+" con "+str(minimo)+" personas en total\n\n")
       for i in range(3):
            archivoinformes.write("Tuvo "+str(minstr[i])+" personas en el teleferico #"+str(i+1)+"\n")
       archivoinformes.write("\nEl horario con mas personas fue el horario "+str(horariomax)+" con "+str(maximo)+" personas en total\n\n")
       for i in range(3):
            archivoinformes.write("Tuvo "+str(maximostr[i])+" personas en el teleferico #"+str(i+1)+"\n")
       archivoinformes.write("\nDinero generado por clientes nacionales: "+str(nacionalcash[0])+" colones")
       archivoinformes.write("\nDinero generado por clientes extranjeros: "+str(extranjerocash[0])+" colones")
       archivoinformes.write("\nDinero generado en total: "+str(extranjerocash[0]+nacionalcash[0])+" colones")
       archivoinformes.close()
       print("\nEl informe esta guardada en su computadora en el archivo informe.txt\n")
       print(menuPrincipal())
def terminarPrograma():
    os.system("cls")
    print("Gracias por usar el sistema de aventuras El Paraiso")
    exit()
#creacion de una gran matriz para todas las posibles facturas que se puedan crear
for i in range(72):
   factura.append([0]*15)   
print(menuPrincipal())
