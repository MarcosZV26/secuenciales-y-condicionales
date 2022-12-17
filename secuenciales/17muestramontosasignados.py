donacion=float(input("Ingresar el monto de la donacion: "))

centro_de_salud=donacion*0.25
comedor_infantil=donacion*0.35
escuela_infantil=donacion*0.25
asilo_ancianos=donacion*0.15

print("El centro de salud recibe s/.",format(centro_de_salud,".2f"))
print("El comedor infantil recibe s/.",format(comedor_infantil,".2f"))
print("La escuela infantil recibe s/.",format(escuela_infantil,".2f"))
print("El asilo de anciano recibe s/.",format(asilo_ancianos,".2f"))

