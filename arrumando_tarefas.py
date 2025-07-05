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
    valor_tarefas_total: int = sum(map(lambda tupla: tupla[0], tarefas_ordenadas))
    tarefas_escolhidas: list[int] = [0 for _ in range(tempo_total)]
    i: int = 0
    while i < len(tarefas_ordenadas):
        tempo_tarefa_atual = tarefas_ordenadas[i][1] - 1
        adicionado: bool = False
        while not adicionado and 0 <= tempo_tarefa_atual:
            if tarefas_escolhidas[tempo_tarefa_atual] == 0:
                tarefas_escolhidas[tempo_tarefa_atual] = tarefas_ordenadas[i][0]
                adicionado = True
            tempo_tarefa_atual -= 1
        i += 1
    valor_tarefas_escolhidas: int = sum(tarefas_escolhidas)
    return valor_tarefas_total - valor_tarefas_escolhidas

print(arrumando_tarefas(3, [(5, 1), (10, 2), (20, 3)])) # 0
print(arrumando_tarefas(2, [(1, 2), (2, 1), (4, 1), (2, 2)])) # 3
print(arrumando_tarefas(4, [(10, 1), (20, 1), (30, 1), (40, 1)])) #60
print(arrumando_tarefas(2, [(5, 2), (10, 1), (7, 1), (8, 2), (9, 1)])) # 21
print(arrumando_tarefas(5, [(10, 5), (10, 1), (10, 3), (10, 2), (10, 4)])) # 0
print(arrumando_tarefas(6, [(10, 2), (20, 2), (5, 2), (7, 1), (25, 6), (30, 5), (15, 3)])) # 12
