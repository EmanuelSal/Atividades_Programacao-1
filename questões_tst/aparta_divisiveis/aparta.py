# PROGRAMAÇÃO 1 - UFCG - MINITESTE 8
# MATRÍCULA: 120210785 | DATA: 24/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA
# PROGRAMA QUE LEIA OS DIVISORES DE UM NÚMERO E ORGANIZE DE ACORDO COM A ESPECIFICAÇÃO

def aparta(nums, k):
    count = 0
    for valor in range(len(nums) -1):
        if nums[valor] % k == 0:
            if nums[valor + 1] % k != 0: 
                nums[valor], nums[valor + 1] = nums[valor + 1], nums[valor]
                count += 1
            if count == k: break

