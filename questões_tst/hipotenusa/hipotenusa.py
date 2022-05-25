# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 14/12/2021 | MATRÍCULA: 120210785
# EXERCÍCIO: PROGRAMA QUE LEIA OS VALORES  DOS CATETOS DE UM TRIÂNGULO RETâNGULO

#|ENTRADA|
cateto1 = float(input("Cateto 1? "))
cateto2 = float(input("Cateto 2? "))

#|CALCULOS|
hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** 0.5

#|SAIDA|
print(f"Hipotenusa: {hipotenusa:.1f}")
