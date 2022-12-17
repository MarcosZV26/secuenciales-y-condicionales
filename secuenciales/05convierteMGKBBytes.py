gigabytes=int(input("Ingresar capacidad del disco en GB: "))

megabytes=gigabytes*1024
kilobytes=megabytes*1024
bbytes=kilobytes*1024

print("La capacidad del disco es ",gigabytes,"GB")
print("En megabytes es ",megabytes,"MB")
print("En kilobytes es ",kilobytes,"KB")
print("En bytes es ",bbytes,"B")
