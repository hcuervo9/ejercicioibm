peso = float(input ('Ingrese Peso: '))
altura = float(input('Ingrese estatura: '))
bmi = peso/(altura**2)
print('Su indice de masacorporal es '+ str(bmi))
if bmi >= 18.5 and bmi <= 24.9:
    print('su clasificacion es normal')
elif bmi >= 25 and bmi <= 29.9:
    print('ud se encuentra en sobrepeso')
elif bmi >= 30 and bmi <= 34.9:
    print('ud esta en obesidad grado 1')
elif bmi >= 35 and bmi <= 39.9:
    print('ud tiene obesidad grado 2')
elif bmi >= 40:
    print('ud tiene obesidad grado 3')

