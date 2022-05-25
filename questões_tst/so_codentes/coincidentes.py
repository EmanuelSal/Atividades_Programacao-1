


def so_coincidentes(M1, M2):
    matriz_nova = []
    linha = len(M1)
    coluna = len(M1[0]) 
    for valor in range(linha):
        matrix_aux = []
        for valor2 in range(coluna):
            if M1[valor][valor2] != M2[valor][valor2]:
                matrix_aux.append(0)
            else:
                matrix_aux.append(M1[valor][valor2])
        matriz_nova.append(matrix_aux)
    return matriz_nova


M1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M2 = [[10, 11, 12], [13, 14, 15], [7, 8, 9]]
M3 = [[1, 2, 3], [13, 14, 15], [16, 17, 18]]

assert so_coincidentes(M1, M2) == [[0,0,0],[0,0,0],[7,8,9]]
assert so_coincidentes(M1, M3) == [[1,2,3],[0,0,0],[0,0,0]]
