
cal1 = float(input("ingrese la primera calificacion: "))
if cal1 > 5:
    print("NOTA ERRONEA")
elif cal1 < 5:
    print("NOTA ERRONEA")
cal2 = float(input("ingrese la segunda calificacion: "))
if cal2 > 5:
    print("NOTA ERRONEA")
elif cal2 < 1:
    print("NOTA ERRONEA")
cal3 = float(input("ingrese la tercera calificacion: "))
if cal3 > 5:
    print("NOTA ERRONEA")
elif cal3 < 1:
    print("NOTA ERRONEA")
cal4 = float(input("ingrese la cuarta calificacion: "))
if cal4 > 5:
    print("NOTA ERRONEA")
elif cal4 < 1:
    print("NOTA ERRONEA")

matricula = float(input("ingrese el valor de la matricula: "))
descuento = (matricula*0.20)-matricula
promedio = (cal4+cal3+cal2+cal1)/4

if promedio > 5:
    print("LAS NOTAS INGRESADAS NO SON VALIDAS")
if promedio < 1:
    print("LAS NOTAS INGRESADAS NO SON VALIDAS")

if promedio >= 4:
    print(f"tu desempeno fue excelente y el costo de la mtricula es {descuento}")
elif promedio >= 3:
    print(f"tu desempeño fue bueno y es costo de la matricula es {matricula }")
elif promedio >= 1:
    print(f"tu desempeño fue deficiente y el costo de la matricula es {matricula }")