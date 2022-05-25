
def ofuscador(linha):
    for letra in range(len(linha)):
        
     
        if letra >= 0 and linha[letra] == 'c':
            linha[letra] == "C"
        elif letra >= 0 and linha[letra] == 'd':
            linha[letra] == "D"
        elif letra >= 0 and linha[letra] == 'f':
            linha[letra] == "F"
        elif letra >= 0 and linha[letra] == 'h':
            linha[letra] == 'H'
        elif letra >= 0 and linha[letra] == 'j':
            linha[letra] == 'J'
        elif letra >= 0 and linha[letra] == 'k':
            linha[letra] == 'K'
        elif letra >= 0 and linha[letra] == 'm':
            linha[letra] == 'M'
        elif letra >= 0 and linha[letra] == 'n':
            linha[letra] == 'N'
        elif letra >= 0 and linha[letra] == 'p':
            linha[letra] == 'P'
        elif letra >= 0 and linha[letra] == 'q':
            linha[letra] == 'Q'
        elif letra >= 0 and linha[letra] == 'r':
            linha[letra] == 'R'
        elif letra >= 0 and linha[letra] == 't':
            linha[letra] == 'T'
        elif letra >= 0 and linha[letra] == 'u':
            linha[letra] =='U'
        elif letra >= 0 and linha[letra] == 'v':
            linha[letra] =='V'
        elif letra >= 0 and linha[letra] == 'w':
            linha[letra] == 'W'
        elif letra >= 0 and linha[letra] == 'x':
            linha[letra] == 'X' 
        elif letra >= 0 and linha[letra] == 'y':
            linha[letra] == 'Y'
        elif letra >= 0 and linha[letra] == 'z':
            linha[letra] == 'Z'
        
        
        
        if letra > 0 and linha[letra] == "a" or letra > 0 and linha[letra] == "A":
            linha[letra] == '4'
        elif letra > 0 and linha[letra] == "B" or letra > 0 and linha[letra] == "b":
            linha[letra] == '8'
        elif letra > 0 and linha[letra] == "E" or letra > 0 and linha[letra] == "e":
            linha[letra] == '3'
        elif letra > 0 and linha[letra] == "G" or letra > 0 and linha[letra] == "g":
            linha[letra] == '6'
        elif letra > 0 and linha[letra] == "letra" or letra > 0 and linha[letra] == "I":
            linha[letra] == '1'
        elif letra > 0 and linha[letra] == "L" or letra > 0 and linha[letra] == "letra":
            linha[letra] == '7'
        elif letra > 0 and linha[letra] == "s" or letra > 0 and linha[letra] == "S":
            linha[letra] == '5'
        elif letra > 0 and linha[letra] == "O" or letra > 0 and linha[letra] == "o":
            linha[letra] == '0'
        
        if linha[letra] == " ":
            linha[letra] == '*'

