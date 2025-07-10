# Codinome da Equipe: quartafeira. Nome dos Integrantes: Caetano Vendrame Mantovani (ra: 135846), Lucas de Oliveira Fratus (ra:134698)

import sys
sys.setrecursionlimit(10000)


def quant_movimentos(pecas: list[int], n: int, h: int, folga: int):    
    if n == 2:
        # Caso base, no qual temos apenas duas peças, o que impossibilita a movimentação de qualquer uma delas
        if pecas[n-2] + folga <= h:
            return 0
        else:
            return -1
    else:
        resto = pecas[n-2] + folga - h
        # O índice n - 2 é utilizado por conta da restrição de que a ultima peça não pode ser movida
        if pecas[n-2] + folga > h:
            if pecas[n-2] + folga > h:
                com_folga = quant_movimentos(pecas, n - 1, h, resto)
            
                if com_folga == -1:
                    return -1
                else:
                    return (com_folga + 1)
        else:
            if pecas[n-2] + folga < h:
                sem_folga = quant_movimentos(pecas, n-1, h, 0)
                com_folga = quant_movimentos(pecas, n-1, h, resto)
                if sem_folga == -1 and com_folga == -1:
                    return -1
                elif sem_folga == com_folga:
                    return sem_folga
                else:
                    return com_folga + 1
            else:
                return quant_movimentos(pecas, n - 1, h, 0)


def main():
    while True:
        n, h = list(map(int, input().strip().split()))
        if n != -1 and h != -1:
            pecas = list(map(int, input().strip().split()))
            print(quant_movimentos(pecas, n, h, 0))
        else:
            break

main()
