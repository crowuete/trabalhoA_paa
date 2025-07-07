import sys

def main() -> None:
    input = sys.stdin.read
    linhas = input().splitlines()

    casos_teste: list[tuple[int, int, list[tuple[int, int]]]] = []
    i: int = 0

    while i < len(linhas):
        linha = linhas[i].strip()
        if linha:
            n, h = map(int, linha.split())
            tarefas: list[tuple[int, int]] = []
            for j in range(n):
                i += 1
                v, t = map(int, linhas[i].strip().split())
                tarefas.append((v, t))
            casos_teste.append((n, h, tarefas))
        i += 1

    for n, h, tarefas in casos_teste:
        resultado: int = arrumando_tarefas(h, tarefas)
        print(resultado)


def arrumando_tarefas(tempo_total: int, tarefas: list[tuple[int, int]]) -> int:
    # Ordena as tarefas por valor em ordem decrescente
    tarefas_ordenadas: list[tuple[int, int]] = sorted(tarefas, key=lambda tupla: tupla[0], reverse=True)
    # Calcula o valor total das tarefas e inicializa a lista de tarefas escolhidas
    valor_tarefas_total: int = sum(map(lambda tupla: tupla[0], tarefas_ordenadas))
    tarefas_escolhidas: list[int] = [0 for _ in range(tempo_total)]
    i: int = 0
    # Itera sobre as tarefas ordenadas e tenta alocá-las no tempo disponível
    # Se a tarefa não puder ser alocada no tempo exato, tenta alocá-la no tempo anterior
    # até encontrar um espaço livre ou esgotar o tempo
    while i < len(tarefas_ordenadas):
        tempo_tarefa_atual = tarefas_ordenadas[i][1] - 1
        adicionado: bool = False
        while not adicionado and 0 <= tempo_tarefa_atual:
            if tarefas_escolhidas[tempo_tarefa_atual] == 0:
                tarefas_escolhidas[tempo_tarefa_atual] = tarefas_ordenadas[i][0]
                adicionado = True
            tempo_tarefa_atual -= 1
        i += 1
    # Calcula o valor total das tarefas escolhidas e retorna a diferença entre o valor total e o valor das tarefas escolhidas
    valor_tarefas_escolhidas: int = sum(tarefas_escolhidas)
    return valor_tarefas_total - valor_tarefas_escolhidas

if __name__ == "__main__":
    main()
