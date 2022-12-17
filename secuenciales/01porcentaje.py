print("cuanto es el porcentaje de varones en el salon?")

var = int(input("ingrese numero de varones: "))
muj = int(input("ingrese numero de mujeres: "))
resultado = var + muj

phombre = var * 100 / resultado
pmujer = muj * 100 / resultado

print("El porcentaje de varones seria: ",format(phombre,".2f"),"%")
print("El porcentaje de mujeres seria: ",format(pmujer,".2f"),"%")
