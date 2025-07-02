"""
Input

The input is composed of several test cases and ends with end of file. 
Each one describes a list of tasks and starts with two integers N (1 ≤N) and H (H ≤ 1000), which are, 
respectively, the number of tasks and the number of hours that the computer is available. 
Then follow N lines, each one with two integer v (1 ≤ v ≤ 1000) and t (1 ≤ t ≤ H) described above.

3 3
5 1
10 2
20 3
4 2
1 2 
2 1 
4 1 
2 2

Output
For each test case output a line with an integer representing the minimum lost money.
0
3
"""
# Falta o main()

def arrumando_tarefas(tempo_total: int, tarefas: list[tuple[int, int]]) -> int:
    tarefas_ordenadas: list[tuple[int, int]] = sorted(tarefas, key=lambda tupla: tupla[0], reverse=True)
    print(tarefas_ordenadas)
    valor_tarefas_total: int = sum(map(lambda tupla: tupla[0], tarefas_ordenadas))
    tarefas_escolhidas: list[int] = [0 for _ in range(tempo_total)]
    print(tarefas_escolhidas)
    # vou transformar esse for em um while, pois há casos que não estão sendo tratados por causa do tempo_total.
    # while que vai até tamanho total da lista *tarefas ou se a lista estiver completa (ex: variavel n de adições == len(tarefas_escolhidas))
    for i in range(0, tempo_total):
        tempo_tarefa_atual = tarefas_ordenadas[i][1] - 1
        adicionado: bool = False
        while not adicionado and 0 <= tempo_tarefa_atual:
            if tarefas_escolhidas[tempo_tarefa_atual] == 0:
                tarefas_escolhidas[tempo_tarefa_atual] = tarefas_ordenadas[i][0]
                adicionado = True
            tempo_tarefa_atual -= 1
    print(tarefas_escolhidas)
    valor_tarefas_escolhidas: int = sum(tarefas_escolhidas)
    return valor_tarefas_total - valor_tarefas_escolhidas

print(arrumando_tarefas(3, [(5, 1), (10, 2), (20, 3)]))
print(arrumando_tarefas(2, [(1, 2), (2, 1), (4, 1), (2, 2)]))
