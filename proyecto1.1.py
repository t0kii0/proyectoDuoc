import sys
def calculoDcto(valorTotal,descuento):
  descuento = (valorTotal * descuento/100)
  return descuento

asientos=[["|",1,2,3,4,5,6,"|"],
["|",7,8,9,10,11,12,"|"],
["|",13,14,15,16,17,18,"|"],
["|",19,20,21,22,23,24,"|"],
["|",25,26,27,28,29,30,"|"],
["------------------------------"],
["|",31,32,33,34,35,36,"|"],
["|",37,38,39,40,41,42,"|"]]
usuario=[]
registro=[]
valorNormal = 78900
valorVip = 240000
descuento = 15


print("*"*66)
print("\t\t\tBienvenido a Vuelos Duoc\n \t\t\t")
print(" 1.Ver asientos disponibles\n 2.Comprar asiento\n 3.Anular vuelo\n 4.Modificar datos de pasajero\n 5.Salir")
print()
print("*"*66)

op = 5
while op !=6:
 op = int(input("Por favor seleccione una opcion (1-5): "))
 
 print()
 if op == 1:
   print("\t\t asientos normales del 1 al 30 $78900")
   print("|----------------------------------------------------------------|")
   print("|\t 1  \t 2  \t 3  \t\t 4  \t 5  \t 6  \t |")
   print("|                                                                |")
   print("|\t 7  \t 8  \t 9  \t\t 10 \t 11 \t 12 \t |")
   print("|                                                                |")
   print("|\t 13 \t 14 \t 15 \t\t 16 \t 17 \t 18 \t |")
   print("|                                                                |")
   print("|\t 19 \t 20 \t 21 \t\t 22 \t 23 \t 24 \t |")
   print("|                                                                |")
   print("|\t 25 \t 26 \t 27 \t\t 28 \t 29 \t 30 \t |")
   print("|                                                                |")
   print("|_________\t\t _________|")
   print("|_________\t\t _________|")
   print("|                                                                |")
   print("|\t 31 \t 32 \t 33 \t\t 34 \t 35 \t 36 \t |")
   print("|                                                                |")
   print("|\t 37 \t 38 \t 39 \t\t 40 \t 41 \t 42 \t |")
   print()
   print("\t\t asinetos vip del 31 al 42 $240000")
   
 if op == 2:
  print("A escogido la opcion 2, complete el registro porfavor.") 
  print("PORFAVOR INGRESE SUS DATOS CORRECTOS O SI NO SE REINICIARA EL SISTEMA")
  print()
  nombrePasajero = str(input("Ingrese su nombre completo: "))
  usuario.insert((0), (nombrePasajero))
  rutPasajero = int(input("Ingrese su rut sin puntos ni digito verificador: "))
  if rutPasajero >=3000000 and rutPasajero <99999999:
   usuario.insert((1), (rutPasajero))
   telefonoPasajero = str(input("Ingrese su numero de telefono: "))
   if len(telefonoPasajero) == 9:
    usuario.insert((2), (telefonoPasajero))
    bancoPasajero = str(input("¿Pertenece a bancoDuoc?: "))
    if bancoPasajero.lower() == "si":
     esDuoc = True
    else:
     esDuoc = False
    asientoPasajero=int(input("Escoja un asiento: "))
    usuario.insert((3), (asientoPasajero))
    registro.insert(0, (usuario))
    print()
    for fila in asientos:
     for asiento in fila:
         if asiento == asientoPasajero:
             ind_asiento=fila.index(asiento)
             fila[ind_asiento] = "x"
    for i in asientos:
     print(i)
    print(registro)
    if asientoPasajero >= 1 and asientoPasajero <= 30:
     valorTotal = valorNormal
     if esDuoc:
      valorTotal = valorTotal - calculoDcto(valorTotal,descuento)
      print("A escogido el asiento n°", asientoPasajero, "con un valor de:", valorTotal)
     else:
      valorTotal = valorNormal
      print("A escogido el asiento n°", asientoPasajero, "con un valor de:", valorTotal)
    else:
     if asientoPasajero >= 31 and asientoPasajero <= 42:
      valorTotal = valorVip
      if esDuoc:
       valorTotal = valorTotal - calculoDcto(valorTotal,descuento)
       print("A escogido el asiento n°", asientoPasajero, "con un valor de:", valorTotal)
      else:
       valorTotal = valorVip
       print("A escogido el asiento n°", asientoPasajero, "con un valor de:", valorTotal)
   else:
     print("Ingrese un telefono valido de 9 digitos")
  else:
    print("ingrese un rut valido")
    print()
 
 if op == 3:
     
    
    print()
    print("opcion 3 (anular compra)")
    buscar = int(input("Ingrese el rut a consultar: "))
    if buscar == rutPasajero:
     print(registro)
     anulacion = str(input("¿Desea eliminar este registro?"))
     if anulacion.lower() == "si":
      registro.clear()
      print("registro eliminado")
    else:
     print("No existe registro de este rut.")
     print()
 
 if op == 4:
   print()
   opcion = 3
   while opcion !=4:
    opcion = int(input("Seleccione el dato a modificar: \n1-Nombre: \n2-telefono: \n3-salir al menu principal"))
    print()
    if opcion == 1:
      usuario.pop(0)
      nuevonombre = input("ingrese un nuevo Nombre: ")
      usuario.insert((0), nuevonombre)
    if opcion == 2:
      usuario.pop(2)
      nuevotelefono = input("Ingrese un nuevo Telefono: ")
      usuario.insert((2), nuevotelefono)
    if opcion == 3:
      print("Volver al menu principal")
      print(registro)
      print()
 
 if op == 5:
   print()
   sys.stderr.write("Gracias por elegir Vuelos Duoc")
   raise SystemExit(1)
