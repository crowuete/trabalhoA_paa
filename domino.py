# Codinome da Equipe: quartafeira. Nome dos Integrantes: Caetano Vendrame Mantovani (ra: 135846), Lucas de Oliveira Fratus (ra:134698)

import sys
sys.setrecursionlimit(10000)


def quant_movimentos(pecas: list[int], n: int, h: int, folga: int, memo):    
    if (n-2, folga) in memo:
        return memo[(n-2, folga)]
    
    if n == 2:
        # Caso base, no qual temos apenas duas peças, o que impossibilita a movimentação de qualquer uma delas
        if pecas[n-2] + folga <= h:
            memo[(n-2, folga)] = 0
            return 0
        else:
            memo[(n-2, folga)] = -1
            return -1
    else:
        resto = pecas[n-2] + folga - h
        # O índice n - 2 é utilizado por conta da restrição de que a ultima peça não pode ser movida
        if pecas[n-2] + folga > h:
            com_folga = quant_movimentos(pecas, n - 1, h, resto, memo)
            if com_folga == -1:
                memo[(n-2,folga)] = -1
                return -1
            else:
                memo[(n-2,folga)] = com_folga + 1
                return (com_folga + 1)
        else:
            if pecas[n-2] + folga < h:
                # Faz duas chamadas da função, uma considerando a folga e a outra não
                sem_folga = quant_movimentos(pecas, n-1, h, 0, memo)
                com_folga = quant_movimentos(pecas, n-1, h, resto, memo)
                if sem_folga == -1 and com_folga == -1:
                    memo[(n-2,folga)] = -1
                    return -1
                elif sem_folga == com_folga:
                    memo[(n-2,folga)] = sem_folga
                    return sem_folga
                else:
                    memo[(n-2,folga)] = com_folga + 1
                    return com_folga + 1
            else: # Se pecas[n-2] + folga = h
                resp = quant_movimentos(pecas, n - 1, h, 0, memo)
                memo[(n-2,folga)] = resp
                return resp


def ler_entrada():
    n, h = input().split() # Lê a quantidade de peças(n) e a altura de cada peça(h)
    n = int(n)
    h = int(h)

    if n == -1 and h == -1:
        return n, h, []

    pecas_string = input().split()
    pecas = []
    for x in pecas_string:
        pecas.append(int(x))
    
    return n, h, pecas


def main():
    while True:
        n, h, pecas = ler_entrada()

        # Detecta o final da entrada
        if n == -1 and h == -1:
            break

        # Criação do dicionário para memoização
        memo = {}

        movimentos = quant_movimentos(pecas, n, h, 0, memo)

        print(movimentos)


if __name__ == '__main__':
    main()