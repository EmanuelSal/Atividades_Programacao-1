# PROG1 - UFCG
# MATRICULA: 120210785 | DATA: 10/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA
# PROGRAMA QUE COMPARA DUAS STRING E CONTA OS CARACTERES DIFERENTES 

def compara_senhas(senha1, senha2):
    
    count = 0
    if len(senha1) <= len(senha2):
        for caracter in range(len(senha1)):
            if senha1[caracter] != senha2[caracter]:
                count += 1
    elif len(senha2) <= len(senha1):
        for caracter in range(len(senha2)):
            if senha2[caracter] != senha1[caracter]:
                count += 1


    return count


assert compara_senhas('nome123', 'nome') == 0
assert compara_senhas('aaa', 'bbb') == 3
assert compara_senhas('senha', 'Senha') == 1

