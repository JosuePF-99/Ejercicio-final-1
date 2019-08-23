#!/usr/bin/python3
while True:
    print("listas")
    print("Tuplas")
    print("Diccionarios")
    print("salir")
    user_input = input(" :")
    if user_input == "salir":
        break
    elif user_input == "listas":
        print("\nEjercicios de listas")
        print("1). append + pop   + reverse ó sorted"+" :")#*
        print("2). insert + pop o remove + crear una nueva lista + formas de ordenarla"+" :")
        print("3). append o insert + cortar listas + pop o remove + sorted"+" :")
        print("4). usar add"+" :")
        print("salir"+" :")
        user_input = input("ingrese un numero 1-4 "+"  :")
        if user_input == "salir":
            break
        elif user_input == "1":#-------------------------------------------------->inicio lista opc #1------------
            print("\nHay una lista vacia ingrese los item's")
            a_list = ['cachucho']
            x = input("ingrese un item"+" :")
            y = input("ingrese un item"+" :")
            z = input("ingrese un item"+" :")
            w = input("ingrese un item"+" :")
            #-----------------------varibles de ingreso a la lista----------------------------------------------------
            a_list.append(x)
            a_list.append(y)
            a_list.append(z)
            a_list.append(w)
            #-----------en orden--------------------------------------------
            for i in range(len(a_list)):
                print(i,a_list[i])
            print("\n")
            print("desea eliminar un item? :")
            print("si")
            print("no")
            user_input2 = input(" :")
            if user_input2 == "si":#------------------------------>con pop()------------------------------------------
                for i in range(len(a_list)):
                    print(i,a_list[i])
                print("\n")
                print("cual desea eliminar? :")
                print("escojer un item valido a eliminar.")
                delet = int(input("item solor numero"+" :"))
                po = a_list.pop(delet)
                for i in range(len(a_list)):
                    print(i,a_list[i])
                print("\n")#---------------------------------------------------->pop()-------------------------------
                print("ahora se ordenara la lista")
                print("\n")
                print("cual metodo desea utilizar"+" :")
                print("1). reverse")
                print("2). sorted")
                user_input2 = input(" :")
                if user_input == "1":
                    print("lista ordenada con reverse"+" :")
                    a_list.sort(reverse=True)
                    for i in range(len(a_list)):
                        print(i,a_list[i])
                    print("\n")
                elif user_input2 == "2":
                    print("lista ordenada con sorted")
                    print(sorted(a_list))
                    for i in range(len(a_list)):
                        print(i,a_list[i])
                    print("\n")
                else:
                    print(" ")
                    print("\n")#----------------------------------------------------fin con pop()----------------------
                
            elif user_input2 == "no":#-------------------------->sin pop()
                print("ahora se ordenara la lista")
                print("\n")
                print("cual Metodo desea utilizar?"+" :")
                print("1). reverse")
                print("2). sorted")
                user_input2 = input(" :")
                if user_input2 == "1":#------------------>reverse()#2
                    print("listo ordenado con reverse"+" :")
                    a_list.sort(reverse=True)
                    for i in range(len(a_list)):
                        print(i,a_list[i])
                    print("\n")
                elif user_input2 == "2":#---------------->sorted()#2
                    print("Listo ordenado con sorted()")
                    print(sorted(a_list))
                    for i in range(len(a_list)):
                        print(i,a_list[i])
                    print("\n")

                else:
                    print("")
#------------------------------------------------final #lista opcion#1-------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
        elif user_input == "2":#------------------------------inicio listas con insert opc #2-------------------------------
            print("Hay una lista vacioa ingrese los item's"+" :")
            print("\n")
            b_list = []#-------> creacion de lista vacia
            #----------------------------#---------------------
            x = input("ingrese un item"+" :")
            xx = int(input("ingrese una coordenada"+" :"))
            y = input("ingrese un item"+" :")
            yy = int(input("ingrese una coordenada"+" :"))
            z = input("ingrese un item"+" :")
            zz = int(input("ingrese una coordenada"+" :"))
            #primero coordenada y despues item
            b_list.insert(xx,x)
            b_list.insert(yy,y)
            b_list.insert(zz,z)
            print("\n")
            print("producto final  :")
            for i in range(len(b_list)):
                print(i,b_list[i])
            print("\n")#----------------------------------------------fin con insert------------------------------
            print("Desea eliminar algun item"+" :")
            print("si")
            print("no")
            user_input2 = input(" :")
            if user_input2 == "si":#-------------------------------------------pop ó remove-------------------------
                print("\n")
                print("Cual Metodo desea utilizar"+" :")
                print("pop()")
                print("remove()")
                user_input2 = input(" :")
                if user_input2 == "pop":#------------------------inicio de pop opc #2-------------------------
                    print("\n")
                    for i in range(len(b_list)):
                        print(i,b_list[i])
                    print("\n")
                    print("cual desea eliminar?"+" :")
                    print("escoja un item valido a eliminar.")
                    delet2 = int(input("item solor numro"+" :"))
                    po_ped2 = b_list.pop(delet2)
                    print("se elimino",po_ped2)
                    print("\n")
                    for i in range(len(b_list)):
                        print(i,b_list[i])
                    print("\n")#-----------------------------------fin de pop opc#2----------------------------
                elif user_input2 == "remove":#------------->inincio de remove opc#2--------------------
                    print("\n")
                    for i in range(len(b_list)):
                        print(i,b_list[i])
                    print("\n:")
                    print("cual desea eliminar"+" :")
                    print("escoja un item valido a eliminar.")
                    removi = (input("item no ingrese numeros"+" :"))
                    b_list.remove(removi)
                    print("\n")
                    for i in range(len(b_list)):
                        print(i,b_list[i])#-------------------->fin de remove opc#2------------------
                    print("\n")
                else:
                    print("")

            elif user_input2 == "no":
                print("desea crear una nueva lista :")#-----opc#2-----crear una nueva lista y usuario le da nombre---------
                print("si")
                print("no")
                user_input2 = input(" :")
                if user_input2 == "si":
                    print("\n")
                    a = input("como desea llamar a la lista:")
                    a = []
                    print("desea ingresar algunos item's a la lista:")#-------------ingresar algunos items opc#2------
                    print("si")
                    print("no")
                    user_input2 = input(" :")
                    if user_input2 == "si":#--->inicio ingresar items#
                        print("\n")
                        x = input("item #1"+" :")
                        y = input("item #2"+" :")
                        z = input("item #3"+" :")
                        a.append(x)
                        a.append(y)
                        a.append(z)
                        print("\n")
                        print(a)#-------lista sin ordenar
                        print("\n")
                        for i in range(len(a)):#-------lista ordenada
                            print(i,a[i])
                        print("\n")#---------------->final ingresar items#
                    elif user_input2 == "no":# no
                        print("producto final")
                        for i in range(len(b_list)):
                            print(i,b_list[i])
                        print("\n")#final no
                    else:
                        print("\n")
                elif user_input2 == "no":#------------->usuario no quiso hacer nueva lista
                    print("ok.")
                else :
                    print(" ")

            else:
                    print("")
#--------------------------------------fin de #listas opcion #2---------------------------------------------------------               
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------opc #3-------------------------------------------------------------        
        elif user_input == "3":
            print("cual desea usar")
            print("1). append")
            print("2). insert")
            user_input2 = input(" :")
            if user_input2 == "1":
                print("append")
                my_lista = []
                #creando variables de entrada para append
                x = input(" :")
                y = input(" :")
                z = input(" :")
                #insertando variable a append()
                my_lista.append(x)
                my_lista.append(y)
                my_lista.append(z)
                for i in range(len(my_lista)):
                    print(i,my_lista[i])
                print("\n")
                #cortar lista
                print("desea cortar la lista")
                print("si")
                print("no")
                user_input2 = input(" :")
                if user_input2 == "si":
                    print(my_lista)
                    x = int(input("cortar de "+" :"))
                    y = int(input("cortar hasta"+" :"))
                    print(my_lista[x:y])
                    print("\n")
                elif user_input2 == "no":
                    print("\n")
                else:
                    print("\n")
                print("desea eliminar algun item"+" :")
                print("si")
                print("no")
                user_input2 = input(" :")
                if user_input2 == "si":
                    print("no lo eliminare")
                    print("\n")
                elif user_input2 == "no":
                    print("ok")
                    print("\n")
                else:
                    print("\n")

                #ahora con insert
            elif user_input2 == "2":
                print("insert()")
                my_lista = []
                print("ingrese item´s del 0 al 2")
                print("\n")
                #variables de entrada para insert
                x = input("item"+" :")
                xx = int(input("coordenada"+" :"))
                y = input("item"+" :")
                yy = int(input("coordenada"+" :"))
                z = input("item"+" :")
                zz = int(input("coordenada"+" :"))
                #insertando variable a insert
                my_lista.insert(xx,x)
                my_lista.insert(yy,y)
                my_lista.insert(zz,z)
                print("\nLista ordenada"+" :")
                for i in range(len(my_lista)):
                    print(i,my_lista[i])
                print("\n")
                #cortando la lista 
                print("\ndesea cortar la lista"+" :")
                print("si")
                print("no")
                user_input2 == input(" :")
                print("\n")
                if user_input2 == "si":
                    for i in range(len(my_lista)):
                        print(i,my_lista[i])
                    print("\n")
                    x = int(input("cortar de"+" :"))
                    y = int(input("cortar hasta"+" :"))
                    print(my_lista[x:y])
                    print("\n")
                elif user_input == "no":
                    print("\n")
                else :
                    print("\n")#------------------->final cortando la lista
                print("\n")
                print("desea eliminar algun item?"+" :")
                print("si")
                print("no")
                user_input2 = input(" :")
                if user_input2 == "si":
                    print("\n")
                    print("Que metodo desea utilizar?"+" :")
                    print("pop")
                    print("remove")
                    user_input2 = input(" :")
                    #usando el Metodo pop
                    if user_input2 == "pop":
                        print("\n")
                        for i in range(len(my_lista)):
                            print(i,my_lista[i])
                        print("\n")
                        x = int("ingrese un item valido"+" :")
                        po_ped = my_lista.pop(x)
                        print("\n")
                        for i  in range(len(my_lista)):
                            print(i,my_lista[i])
                        print("\nordenado con sorted")
                        print(sorted(my_lista))
                        print("\n")
                    #usando el metodo remove
                    elif user_input2 == "remove":
                        print("\n")
                        for i in range(len(my_lista)):
                            print(i,my_lista[i])
                        print("\n")
                        x = input("inggrese un item valido"+" :")
                        my_lista.remove(x)
                        print("\n")
                        for i in range(len(my_lista)):
                            print(i,my_lista[i])
                        print("\nordenado con sorted")
                        print(sorted(my_lista))
                        print("\n")
                    else :
                        print("\n")
                    

                elif user_input2 == "no":
                    print("\nOrdenando con sorted"+" :")
                    print(sorted(my_lista))
                    print("\n")
                else:
                    print("\n")
            else:
                print("\n")



                


                
        else:
            print("")
            



    elif user_input == "tuplas":
        print("\n")
    elif user_input == "diccionarios":
        print("\n")
    else:
        print("")
