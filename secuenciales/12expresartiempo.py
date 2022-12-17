print("")
num_segundos=int(input("Digitar un numero expresado en segundos: "))

dias=((num_segundos//60)//60)//24
horas=((num_segundos//60)//60)%24
minutos=(num_segundos//60)%60
segundos=num_segundos%60

print("Dias: ",dias)
print("Horas: ",horas)
print("Minutos: ",minutos)
print("Segundos: ",segundos)
print("")
